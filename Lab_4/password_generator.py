import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Easy version - letters, then symbols, then numbers
password = ""
for _ in range(nr_letters):
    password += random.choice(letters)
for _ in range(nr_symbols):
    password += random.choice(symbols)
for _ in range(nr_numbers):
    password += random.choice(numbers)
print(f"Easy password: {password}")

# Hard version - shuffled order
password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)  # in place, returns None
password = "".join(password_list)
print(f"Hard password: {password}")
