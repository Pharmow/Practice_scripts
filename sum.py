# Initialize sum variable
total = 0

# Loop through numbers from 1 to 999
for num in range(1, 1000):
    # Check if the number is divisible by 3 or 5
    if num % 3 == 0 or num % 5 == 0:
        # If it is, add it to the sum
        total += num

# Print the sum
print("The sum of all the multiples of 3 or 5 below 1000 is:", total)
