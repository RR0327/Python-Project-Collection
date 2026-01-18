# Explanation

1. Code Objective and Purpose
   Objective: To extract specific data (errors) from a large CSV log file without consuming excessive computer memory (RAM).

Purpose: To provide a reusable "Log Analyzer" framework that can handle files larger than the system's memory by reading them line-by-line rather than all at once.

2. Line-by-Line Explanation
   The Timing Decorator
   @wraps(func): A helper that ensures the function keeps its original identity (name, docstring) after being "wrapped" by the decorator.

start_time = time.perf_counter(): Starts a high-precision timer before the function runs.

result = func(\*args, \*\*kwargs): Executes the actual function being timed.

f"{end_time - start_time:.4f} seconds": Calculates and prints the total duration formatted to 4 decimal places.

The CSV Generator
def process_large_csv(...): This is a Generator. It uses the yield keyword.

csv.DictReader(csvfile): Maps the information in each row to a dictionary where keys are the column headers.

if target_column not in ...: A safety check to ensure the user requested a column that actually exists.

yield row[target_column]: This is the most important line. Instead of returning a massive list, it "gives back" one value at a time to the caller and pauses, saving memory.

The Log Analyzer
@time_logger: Applies the timing decorator to this function.

for value in process_large_csv(...): This loop pulls values from the generator one by one.

if value == "ERROR": Filters the data to find only the log entries we care about.

Main Execution
Path(**file**).resolve().parent: A modern way to find the folder where the script is currently saved.

if not FILE_PATH.exists(): Prevents the script from crashing if the large_logs.csv file is missing.

3. How the Code Works (The Architecture)
   The script uses a "Pipeline" approach to data processing.

Trigger: The main block calls analyze_logs.

Profiling: The time_logger decorator intercepts the call and starts its clock.

Streaming: analyze_logs asks the process_large_csv generator for the next value.

On-Demand Reading: The generator reads exactly one line from the hard drive, sends the "status" value back, and then goes to sleep.

Filtering: analyze_logs checks if that one value is "ERROR". If yes, it saves it; if no, it discards it.

Reporting: Once the end of the file is reached, the decorator stops the clock and the total count of errors is printed.

4. Why is this code "Good"?
   Memory Efficiency: If you had a 10GB log file, a standard list would crash a normal computer. This code only keeps one row in memory at a time.

Scalability: Because it reads line-by-line, it takes the same amount of RAM to process a 1MB file as it does a 100GB file.

Clean Design: The logic for "timing" (meta-data), "reading" (IO), and "analyzing" (logic) are completely separated into different functions. This makes the code very easy to maintain.
