"""
RECORD CHECK  -  my version
===========================

Name  :  Malak Hosa
Lane  :  IT
Date  :  2026-10-14

Run it:   python template.py

Reads hostname,GB used,GB total lines from servers.txt, checks each one,
prints a report and writes label,status lines to project_results.txt.
"""

# =================================================================== FUNCTIONS


def check_record(value, limit):
    """Return the difference, percent of limit used, and status for one record."""
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the full report for one record."""
    print(f"{label}: {value} / {limit} ({percent:.1f}%), "
          f"difference {difference:+.1f} -> {status}")


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


def save_results(path, results):
    """Write one label,status line per result to a new file."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")


# ====================================================================== STORE

try:
    records = load_records("servers.txt")
except FileNotFoundError:
    print("servers.txt was not found - starting with no records.")
    records = []

# =============================================================== PROCESS + OUTPUT

results = []
over_count = 0

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    results.append((record["label"], status))
    if status == "OVER LIMIT":
        over_count += 1

save_results("project_results.txt", results)
print(f"Records over limit: {over_count}")
