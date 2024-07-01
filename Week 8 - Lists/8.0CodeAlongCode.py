# Create a list of strings
countries = ["United States", "Germany", "Poland", "Thailand", "Mexico", "Portugal"]
# Create a list of numbers
numbers = [1,3,5,7,9,11]
# Explain indexing, start counting at 0

# Print functions
# Print the whole list
print(countries)

# Print a specific item in the list
print(countries[2])
print(numbers[3])

# Let the user pick
userchoice = int(input("Enter the number of the item in the list, start counting with 0: "))
print(countries[userchoice])

# Lists are mutable (you can change them)
# Add to the end
countries.append("Spain")
print(countries)

# Insert in a specific place
countries.insert(2, "France")
print(countries)

# Replace
countries[1] = "Ireland"
print(countries)

# Remove Items
countries.remove("France")
print(countries)

# Remove Last item in list
countries.pop()
print(countries)

# String Concatenation with Lists
countries[4] = countries[4] + " is the best"
print(countries)

# Do some Math with integer Lists
numbers[0] +=2
print(numbers)

total = numbers[3] * numbers[4]
print(total)

othernumbers = [1.234, 5.678, 4.57]
print(othernumbers)

othertotal = othernumbers[1] + othernumbers[2]
print(othertotal)

# Check for item in the list using if statement
if "United States" in countries:
    print("United States is in the list")

# Could let user input something to search
userselection = input("insert your search term: ")

if userselection in countries:
    print("We found " + userselection + " in the list.")
else:
    print("That item wasn't found")

