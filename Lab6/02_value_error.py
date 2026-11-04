# FIXED.
# Error was: ValueError: All arrays must be of the same length
# Cause: "label" had 3 values but "value" only had 2. Added the missing third value.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 45],
})

print(df)
