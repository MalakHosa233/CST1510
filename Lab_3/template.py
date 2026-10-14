"""
RECORD CHECK  -  my version
===========================

Name  :  Malak Hosa
Lane  :  Cyber
Date  :  14/10/2026

Inputs: source IP (text), failed logins (number), total attempts (number)

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value against limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered record check report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  {'Failed':<12}: {value:>10.2f}")
    print(f"  {'Attempts':<12}: {limit:>10.2f}")
    print(f"  {'Difference':<12}: {difference:>10.2f}")
    print(f"  {'Percent':<12}: {percent:>10.2f} %")
    print(f"  {'Status':<12}: {status:>10}")
    print("=" * 34)


# ============================================== INPUT / PROCESS / OUTPUT LOOP
over_limit_count = 0

while True:
    # INPUT
    label = input("Source IP (or 'quit' to stop): ")
    if label.lower() == "quit":
        break
    value = float(input("Failed logins: "))
    limit = float(input("Total attempts: "))

    # PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit_count += 1

    # OUTPUT
    print_report(label, value, limit, difference, percent, status)

print(f"\nRecords over limit: {over_limit_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#        (10.0.0.5 / 12 / 400 -> OK, 10.0.0.9 / 95 / 100 -> WARNING,
#         10.0.0.7 / 120 / 100 -> OVER LIMIT)
#    [x] Run it with a total of 0 and note the error (do not fix it yet)
#        Error: ZeroDivisionError: float division by zero
#        It happens inside check(), on (value / limit) when limit is 0.
#    [x] Check every function does one job - status_of decides, check
#        calculates, print_report prints
