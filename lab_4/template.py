"""
RECORD CHECK  -  my version
===========================

Name  :  Malak Hosa
Lane  :  Cyber
Date  :  21/10/2026

Data file line:  source IP, failed logins, total attempts   e.g. 10.0.0.5,12,400

Run it:   python template.py
"""

# ====================================================================== CLASS
class Record:
    """One record: a source IP with its failed logins and total attempts."""

    def __init__(self, label, value, limit):
        """Store the label, value and limit on this object."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return this record's value as a percentage of its limit."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK for this record."""
        percent = self.percent()
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("records.txt was not found - starting with no records.")
    records = []


# ==================================================================== OUTPUT
over_limit_count = 0

for record in records:
    status = record.status()          # call once, then reuse the variable
    if status == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  {'Failed':<12}: {record.value:>10.2f}")
    print(f"  {'Attempts':<12}: {record.limit:>10.2f}")
    print(f"  {'Percent':<12}: {record.percent():>10.2f} %")
    print(f"  {'Status':<12}: {status:>10}")
    print("=" * 34)

print(f"\nRecords over limit: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers by hand
#        (12/400 = 3%, 95/100 = 95%, 120/100 = 120%, 45/60 = 75%, 91/100 = 91%)
#    [x] Check every method only reads/changes its OWN object (self) -
#        percent() and status() only use self.value and self.limit
#    [x] Check every method and __init__ has a one-line docstring
#    [x] Checked r1 and r2 are independent: changing records[0].value did not
#        change records[1].value
