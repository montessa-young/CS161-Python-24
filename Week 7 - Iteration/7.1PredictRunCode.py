# Example code 1

# Add comments to each line to say if it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
answer = input()

while answer != "Paris":
    print("Incorrect! Try again.")
    answer = input("What is the capital of France?")

print("Correct!")

# The loop will repeat until the user inputs the correct answer which in this case is Paris.

# Example code 2

counter = 1

while counter < 5:
    print("This code is inside the loop")
    counter += 1

# The print code will repeat until the counter hits 4 because of the condition set.
