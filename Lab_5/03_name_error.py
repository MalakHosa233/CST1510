# FIXED.
# Error was: NameError: name 'status' is not defined
# Why: status is a method that belongs to the object, so it cannot be called on
# its own. It needs the object in front of it.
# Fix: r.status() instead of status().

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)
print(r.status())
