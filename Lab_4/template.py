"""RECORD CHECK — completed Week 4 mini-project (Cyber Security lane)."""
from pathlib import Path
import math

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "security_records.csv"
RESULTS_FILE = BASE_DIR / "security_results.txt"


def check_record(value, limit):
    """Calculate the difference, percentage of the limit and status."""
    difference = value - limit
    if limit == 0:
        percent = 0.0 if value == 0 else math.inf
    else:
        percent = (value / limit) * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print all details for one checked record."""
    percent_text = "not defined (limit is 0)" if not math.isfinite(percent) else f"{percent:.1f}%"
    print(
        f"{label}: value={value:g}, limit={limit:g}, "
        f"difference={difference:g}, percentage={percent_text}, status={status}"
    )


def load_records(path):
    """Load label,value,limit rows from a CSV-style text file."""
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(",")
            if len(parts) != 3:
                raise ValueError(f"Line {line_number} must contain label,value,limit")
            label, value, limit = parts
            records.append({"label": label.strip(), "value": float(value), "limit": float(limit)})
    return records


def write_results(path, results):
    """Write one label,status line per processed record."""
    with open(path, "w", encoding="utf-8") as file:
        for label, status in results:
            file.write(f"{label},{status}\n")


def print_summary(over_limit_count, total_count):
    """Print the final count of records that were over their limit."""
    print(f"OVER LIMIT records: {over_limit_count} of {total_count}")


def main():
    try:
        records = load_records(DATA_FILE)
    except FileNotFoundError:
        print(f"Could not find records file: {DATA_FILE}")
        records = []
    except ValueError as error:
        print(f"Could not read records file: {error}")
        records = []

    results = []
    over_limit_count = 0
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"], difference, percent, status)
        results.append((record["label"], status))
        if status == "OVER LIMIT":
            over_limit_count += 1

    write_results(RESULTS_FILE, results)
    print_summary(over_limit_count, len(records))
    print(f"Results saved to: {RESULTS_FILE.name}")


if __name__ == "__main__":
    main()
