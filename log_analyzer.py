import time
import csv
from functools import wraps
from pathlib import Path


# -------------------- Timing Decorator --------------------
def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(
            f"Function '{func.__name__}' executed in "
            f"{end_time - start_time:.4f} seconds"
        )
        return result

    return wrapper


# -------------------- CSV Generator --------------------
def process_large_csv(file_path, target_column):
    """
    Generator that reads a CSV file line by line
    and yields values from a specific column.
    """
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        if target_column not in reader.fieldnames:
            raise ValueError(f"Column '{target_column}' not found in CSV file")

        for row in reader:
            yield row[target_column]


# -------------------- Log Analyzer --------------------
@time_logger
def analyze_logs(file_path):
    """
    Analyzes a large CSV log file and returns
    all entries with status = 'ERROR'.
    """
    extracted_data = []

    for value in process_large_csv(file_path, "status"):
        if value == "ERROR":
            extracted_data.append(value)

    return extracted_data


# -------------------- Entry Point --------------------
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    FILE_PATH = BASE_DIR / "large_logs.csv"

    if not FILE_PATH.exists():
        raise FileNotFoundError(f"CSV file not found at: {FILE_PATH}")

    errors = analyze_logs(FILE_PATH)
    print(f"Total ERROR entries found: {len(errors)}")
