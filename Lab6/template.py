"""
RECORD CHECK  -  my version
===========================

Name  :  ss
Lane  :  Cyber Security
Date  :  04 November 2026

Run it:   python template.py

Reads login_attempts.csv (source_ip, failed_logins, total_attempts), works out
the failed-login percentage for each source IP, flags each one as OK / WARNING /
OVER LIMIT, then prints, groups, saves a report CSV and saves a bar chart.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# Read the data file (header row + 12 data rows).

df = pd.read_csv("login_attempts.csv")


# ================================================================= PROCESS
# percent = share of login attempts that failed, for each source IP.
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

# status: "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ================================================================== OUTPUT
# Threshold: the full DataFrame with the percent column.
print("ALL SOURCE IPs")
print(df)

# Typical: only the rows that are not "OK" (boolean filter, no loop).
print("\nNOT OK (WARNING or OVER LIMIT)")
print(df[df["status"] != "OK"])

# Excellent: count per status group.
counts = df.groupby("status")["source_ip"].count()
print("\nCOUNT PER STATUS")
print(counts)

# Excellent: save the full DataFrame to a new CSV.
df.to_csv("login_attempts_report.csv", index=False)

# Excellent: one bar chart of the counts per status, saved as a PNG.
counts.plot(kind="bar", color=["#2e7d32", "#c62828", "#f9a825"])
plt.title("Source IPs per status")
plt.xlabel("Status")
plt.ylabel("Number of source IPs")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("login_status_counts.png")
plt.close()


# ==========================================================================
# Before you finish:
#    [x] Checked percent/status by hand for one row:
#        10.0.0.12 -> 380 / 400 * 100 = 95.0, which is 90 or more but under 100,
#        so the status is WARNING (matches the output above).
#    [x] No "and"/"or" in any condition. The only condition is
#        df["status"] != "OK", so no & is needed.
#    [x] Every column in the code exists in login_attempts.csv with the same case:
#        source_ip, failed_logins, total_attempts (+ percent, status added here).
