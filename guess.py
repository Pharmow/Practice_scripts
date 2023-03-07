numbers = [23, 28, 45, 65, 34, 76, 42, 49, 57, 86, 34, 53, 98, 25, 15]

while True:
    guess = input("Enter your guess: ")
    
    try:
        guess = float(guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if guess in numbers:
        print("Congratulations! You picked a winning number:", guess)
        break
    else:
        print("Better luck next time.")
