import random
import string

# Generate list of characters
letters = list(string.ascii_letters)  # Includes both lowercase and uppercase
numbers = list(string.digits)         # Includes '0' to '9'
symbols = list("!#$%&@()*+")

def get_input(prompt, minimum):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            else:
                print(f"Please enter a value of {minimum} or more.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print("Welcome to the PyPassword Generator!")
nr_letters = get_input("How many letters would you like in your password? Enter 6 or more:\n", 6)
nr_numbers = get_input("How many numbers would you like? Enter 5 or more:\n", 5)
nr_symbols = get_input("How many symbols would you like? Enter 4 or more:\n", 4)

# Generate password list
pypassword_generator = ([random.choice(letters) for _ in range(nr_letters)] +
                        [random.choice(symbols) for _ in range(nr_symbols)] +
                        [random.choice(numbers) for _ in range(nr_numbers)])

# Shuffle the password list to ensure randomness
random.shuffle(pypassword_generator)

# Create the final password string
password_generated = "".join(pypassword_generator)
print(password_generated)