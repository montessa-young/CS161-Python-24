x = int(input("Enter a number: "))
y = "start"
if x < 5:
    print("The number is less than 5")
    y = "first if"
elif x < 10:
    print("The number is less than 10")
    y = "first elif"
elif x < 20:
    print("The number is less than 20")
    y = "second elif"
elif x < 30:
    print("The number is less than 30")
    y = "third elif"
elif x < 40:
    print("The number is less than 40")
    y = "fourth elif"
else:
    print("The number is out of range")
    y = "else"

print(y)
