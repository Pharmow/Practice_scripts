#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

n_letters = 8
n_numbers = 5
n_symbols = 3

password = ""
for letter in range(1, 9):
  password += random.choice(letters)
for number in range(1, 6):
  password += random.choice(numbers)
for symbol in range(1, 4):
  password += random.choice(symbols)
print(password)


password = []
for letter in range(1, 9):
  password.append(random.choice(letters))
for number in range(1, 6):
  password.append(random.choice(numbers))
for symbol in range(1, 4):
  password.append(random.choice(symbols))
# print(password)
random.shuffle(password)

password_list = ""
for character in password:
  password_list += character
  
print(password_list)
