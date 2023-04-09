rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n")

choice = int(choose)

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

compchoice = random.randint(0, 2)

print("Computer chose:")
if compchoice == 0:
  print(rock)
elif compchoice == 1:
  print(paper)
elif compchoice == 2:
  print(scissors)
# print(scissors)

if choice == 0 and compchoice == 2:
  print("You win")
elif choice == 1 and compchoice == 0:
  print("You win")
elif choice == 2 and compchoice == 1:
  print("You win")
elif choice == 0 and compchoice == 1:
  print("You lose")
elif choice == 1 and compchoice == 2:
  print("You lose")
elif choice == 2 and compchoice == 0:
  print("You lose")
elif choice == compchoice:
  print("Play again")
elif choice > 2 or choice < 0:
  print("You typed an invalid number, You lose!")
  
