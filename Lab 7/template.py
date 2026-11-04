"""
RECORD CHECK  -  my version
===========================

Name  :  Malak Hosa
Lane  :  Cyber Security
Date  :  04 November 2026

Run it:   python template.py

Reads messy login records from raw_logins.txt, cleans and parses each one into
a dict, flags repeated failed logins, and prints a one-line summary.
"""

# Flag a record when the login FAILED and there were this many attempts or more.
ATTEMPT_LIMIT = 10


# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean one messy raw record and return a dict with clean keys and converted values."""
    cleaned = raw_line.strip().lower()          # whole line: no outer spaces/tabs, all lower case
    fields = {}
    for piece in cleaned.split(","):            # split into key=value pieces
        key, value = piece.split("=", 1)        # maxsplit 1: split on the first "=" only
        fields[key.strip()] = value.strip()     # clean both sides of each piece
    return {
        "src": fields["src"],
        "attempts": int(fields["attempts"]),    # text -> whole number
        "result": fields["result"],
    }


def status_of(attempts, result):
    """Return "FLAGGED" if a failed login had ATTEMPT_LIMIT attempts or more, otherwise "OK"."""
    if result == "failed" and attempts >= ATTEMPT_LIMIT:
        return "FLAGGED"
    return "OK"


# ====================================================================== INPUT
# Raw, messy records live in raw_logins.txt (varied spacing, case and a tab, plus
# one line with a value that is not a number).
raw_records = []
with open("raw_logins.txt") as file:
    for line in file:
        if line.strip():                        # skip blank lines
            raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
parsed_count = 0
flagged_count = 0
failed_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
    except (ValueError, KeyError) as error:     # a line that does not parse must not crash the run
        print(f"Could not parse: {raw_record.strip()}  ({error})")
        failed_count += 1
        continue

    status = status_of(record["attempts"], record["result"])
    print(f"{record}  ->  {status}")
    parsed_count += 1
    if status == "FLAGGED":
        flagged_count += 1

print(f"\nSummary: {parsed_count} records parsed, {flagged_count} flagged, {failed_count} could not be parsed.")

