# FIXED.
# Error was: AttributeError: 'Record' object has no attribute 'value'
# Why: __init__ stored the number as self.amount, so r.value does not exist.
# Fix: store it as self.value, the name the rest of the program uses.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)
