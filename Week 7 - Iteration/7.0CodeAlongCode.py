# while loop
# similar format to else

# check if a value is correct

guess = int(input("Enter a number between 1 and 10: "))

while guess != 9:
  print("That guess is incorrect, choose another number")
  guess = int(input("Enter a number between 1 and 10: "))

if guess == 9:
  print("You guessed correctly")


# counting

counter = 0
while counter < 10:
  print ("The counter value is " + str(counter))
  counter = counter + 1

counter2 = 0
while counter2 < 5:
  print("The counter2 value is " + str(counter2))
  counter2 += 1

counter3 = 10
while counter3 > 0:
  print("The counter3 value is " + str(counter3))
  counter3 -= 1
