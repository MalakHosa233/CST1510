# FIXED.
# Error was: TypeError (can't divide text by numbers)
# Cause: "value" held numbers stored as text ("87", "120", "45") - .dtypes shows object/str.
# Fix: convert the column to numbers with .astype(int) before doing the maths.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})

print(df.dtypes)                       # before: value is text
df["value"] = df["value"].astype(int)  # the fix
print(df.dtypes)                       # after: value is int64

df["percent"] = (df["value"] / df["limit"]) * 100
print(df)
