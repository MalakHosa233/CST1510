# FIXED.
# Error was: ValueError: could not convert string to float: 'unknown'
# Cause: used=unknown - the text "unknown" is not a number, so float() cannot convert it.
# Fix: catch the ValueError, so one bad field does not crash the whole line.

raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=")
    try:
        print(key, float(value))
    except ValueError:
        print(key, "is not a number:", value)
