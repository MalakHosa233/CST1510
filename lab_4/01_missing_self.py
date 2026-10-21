# FIXED.
# Error was: TypeError: Record.status() takes 1 positional argument but 2 were given
# Why: when you call r.status(95), Python automatically passes the object (r) as
# the first argument. So status() received r AND 95, but only had one parameter.
# Fix: every method's first parameter must be self; the 95 then goes to percent.

class Record:
    def status(self, percent):
        return percent

r = Record()
print(r.status(95))
