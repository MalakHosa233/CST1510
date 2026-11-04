# FIXED.
# Error was: ValueError: too many values to unpack (expected 2)
# Cause: "note=server=east".split("=") gives THREE pieces but there are only two variables.
# Fix: use maxsplit - split("=", 1) splits on the first "=" only, so you always get two pieces.

piece = "note=server=east"
key, value = piece.split("=", 1)

print(key, value)
