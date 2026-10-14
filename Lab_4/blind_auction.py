bids = {}
keep_bidding = True

while keep_bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? £"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == "no":
        keep_bidding = False
    elif other_bidders == "yes":
        print("\n" * 100)

highest_bid = 0
winner = ""
for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The winner is {winner} with a bid of £{highest_bid}.")
