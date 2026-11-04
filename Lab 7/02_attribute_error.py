# FIXED.
# Error was: AttributeError: 'float' object has no attribute 'strip'
# Cause: float(value_text) turned the text into a number, and .strip() is a string method.
# Fix: strip the text (value_text) while it is still a string. Convert to a number after.

value_text = "87"
value = float(value_text)

cleaned = value_text.strip()
print(cleaned)
print(value)
