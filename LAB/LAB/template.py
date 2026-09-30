over_limit_count = 0

while True:
	hostname = input("Hostname (or 'quit' to stop): ")
	if hostname.lower() == "quit":
		break

	used = float(input("GB used: "))
	total = float(input("GB total: "))

	free = total - used
	percent = used / total * 100

	if percent >= 100:
		status = "OVER LIMIT"
		over_limit_count += 1
	elif percent >= 90:
		status = "WARNING"
	else:
		status = "OK"

	print("==================================")
	print(f"  RECORD CHECK  -  {hostname}")
	print("==================================")
	print(f"  Used        : {used:10.2f}")
	print(f"  Total       : {total:10.2f}")
	print(f"  Free        : {free:10.2f}")
	print(f"  Percent     : {percent:10.2f} %")
	print(f"  Status      : {status:>10}")
	print("==================================")

print(f"OVER LIMIT records: {over_limit_count}")
