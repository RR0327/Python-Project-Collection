# Explanation

1. **Code Objective and Purpose**

- _Objective:_ To fetch real-time weather data for multiple global cities simultaneously and store that information in a structured database.

- _Purpose:_ It solves the "bottleneck" problem. Instead of waiting for one city's data to finish before starting the next, it fetches all of them at once, making it incredibly fast.

2.  **Line-by-Line Explanation**

    **The Database Layer (WeatherDB)**

- _class WeatherDB::_ Manages the SQLite database.

- \_ \_**enter**\_ \_ and \_ \_**exit**\_ \_: These make the class a Context Manager. It allows you to use the **with** statement, which automatically handles opening the connection, saving changes (commit), or undoing them (rollback) if an error occurs.

\_**create_table:** Ensures the database has the right "columns" (City, Temp, Description, Time) before you try to save anything.

**The Networking Layer (fetch_weather)**

- _async def fetch_weather(...):_ The async keyword tells Python this function can "pause" while waiting for the internet, allowing other code to run in the meantime.

- _httpx.AsyncClient:_ An advanced tool for making web requests that supports asynchronous operations.

- _await client.get(url):_ This is where the "pause" happens. The script sends the request and waits for the Open-Meteo API to respond.

- _response.json():_ Converts the raw text from the internet into a Python dictionary.

**The Orchestrator (fetch_all_weather)**

- _tasks = [...]:_ Creates a list of "to-do" items for every city in your list.

- _asyncio.gather(\*tasks):_ This is the Concurrency Engine. It fires off all the web requests at the same time and waits for all of them to return their results.

**The Persistence Layer**

- _def save_weather_data:_ Takes the list of results and uses the WeatherDB class to write them permanently to the **weather.db** file.

3. **How the Code Works (The Architecture)**
   The code follows a "**Fetch-Then-Save**" workflow:

i.) **Preparation:** The script identifies the coordinates (Latitude/Longitude) for 10 cities.

ii.) **Concurrency:** Using asyncio, it opens 10 "lanes" of communication to the weather API simultaneously.

iii.) **Data Extraction:** It pulls the current temperature and wind speed from the JSON response provided by the API.

iv.) **Batch Saving:** Once all responses are back, it opens the SQLite database and writes all the entries in one session.

4. **Key Concepts and Best Practices**

- _Asynchronous I/O:_ This is the star of the show. If each request took 1 second, a normal script would take 10 seconds. This script takes ~1 second total because it does them in parallel.

- _Context Management:_ By using \_ \_**enter**\_ \_ and \_ \_**exit**\_ \_, the code ensures that the database connection is always closed properly, even if the program crashes. This prevents "Database Locked" errors.

- _Error Handling:_ The **try...except** block in the fetcher ensures that if the internet goes down for one city (e.g., London), the script doesn't stop; it just skips London and continues with the others.

- _Separation of Concerns:_ The code is divided into three distinct parts: Database logic, API logic, and Execution logic. This makes it very easy to test or modify one part without breaking the others.

# Asynchronous Weather Scraper checklist project, demonstrating:

- **asyncio** for concurrency

- **httpx.AsyncClient** for async HTTP requests

- Fetching weather data for 10 cities simultaneously

- Custom Context Manager for database handling

- SQLite database (lightweight, no setup required)

  This is interview-ready and follows real-world async design patterns.

# Asynchronous Weather Scraper (AsyncIO + httpx)

_Project Checklist Coverage_

- Asynchronous API calls

- Concurrent fetching (10 cities at once)

- Custom context manager for DB connection

- Persistent storage (SQLite)

- Clean separation of concerns

# Architecture Overview

asyncio
├── fetch_weather() (async HTTP calls)
├── gather() (concurrent execution)
└── save_to_db() (via Context Manager)

WeatherDB (Context Manager)
└── SQLite Connection

_Install Dependencies_

pip install httpx
