# FIXED.
# Error was: KeyError: 'Value'
# Cause: the column is called "value" (lower case), not "Value".

import pandas as pd

df = pd.DataFrame({"label": ["R-001", "R-002"], "value": [87, 120], "limit": [100, 100]})

print(df["value"])
