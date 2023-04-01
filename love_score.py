# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

n1 = (name1.lower()) + (name2.lower())

ct1 = n1.count("t") + n1.count("r") + n1.count("u") + n1.count("e")

ct2 = n1.count("l") + n1.count("o") + n1.count("v") + n1.count("e")

true = str(ct1)
love = str(ct2)

ls = int(true + love)

if ls < 10 or ls > 90:
    print(f"Your score is {ls}, you go together like coke and mentos.")
elif ls >= 40 and ls <= 50:
    print(f"Your score is {ls}, you are alright together.")
else:
    print(f"Your score is {ls}.")
