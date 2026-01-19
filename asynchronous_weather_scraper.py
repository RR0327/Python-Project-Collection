import sqlite3
import asyncio
import httpx


# ===================== Database Layer =====================
class WeatherDB:
    def __init__(self, db_name="weather.db"):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()

    def _create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS weather (
                city TEXT NOT NULL,
                temperature REAL NOT NULL,
                description TEXT NOT NULL,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

    def insert_weather(self, city, temperature, description):
        self.cursor.execute(
            """
            INSERT INTO weather (city, temperature, description)
            VALUES (?, ?, ?)
            """,
            (city, temperature, description),
        )


# ===================== City Coordinates =====================
CITY_COORDINATES = {
    "London": (51.5072, -0.1276),
    "New York": (40.7128, -74.0060),
    "Tokyo": (35.6895, 139.6917),
    "Paris": (48.8566, 2.3522),
    "Berlin": (52.5200, 13.4050),
    "Sydney": (-33.8688, 151.2093),
    "Toronto": (43.6510, -79.3470),
    "Dubai": (25.2048, 55.2708),
    "Singapore": (1.3521, 103.8198),
    "Dhaka": (23.8103, 90.4125),
}


# ===================== Weather Fetching =====================
async def fetch_weather(client: httpx.AsyncClient, city: str, lat: float, lon: float):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    try:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

        weather = data.get("current_weather")
        if not weather:
            raise ValueError("Missing weather data")

        return {
            "city": city,
            "temperature": weather["temperature"],
            "description": f"Wind {weather['windspeed']} km/h",
        }

    except Exception as exc:
        print(f"[ERROR] Failed to fetch {city}: {exc}")
        return None


async def fetch_all_weather():
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [
            fetch_weather(client, city, lat, lon)
            for city, (lat, lon) in CITY_COORDINATES.items()
        ]
        results = await asyncio.gather(*tasks)
        return [r for r in results if r is not None]


# ===================== Persistence =====================
def save_weather_data(weather_data):
    with WeatherDB() as db:
        for entry in weather_data:
            db.insert_weather(
                entry["city"],
                entry["temperature"],
                entry["description"],
            )


# ===================== Entry Point =====================
if __name__ == "__main__":
    weather_results = asyncio.run(fetch_all_weather())
    save_weather_data(weather_results)
    print("Weather data fetched and saved successfully.")
