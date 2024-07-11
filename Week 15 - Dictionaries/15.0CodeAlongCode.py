thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964}

#Print a dictionary
print("Print a dictionary: ")
print(thisdict)
print()

#Print a specific value from a dictionary
print("Print a specific value from a dictionary - example model: ")
print(thisdict["model"])
print()

#Print all the keys in a dictionary
print("Print the keys in a dictionary")
print(thisdict.keys())
print()

#Print all the values in a dictionary
print("Print all the values in a dictionary:")
print(thisdict.values())
print()

#Print all the items in a dictionary
print("Print all the items in a dictionary")
print(thisdict.items())
print()

#Loop through a dictionary, print a list
print("Loop through a dictionary, print a list")
for x in thisdict.items():
    print(x)
print()

#Loop through a dictionary using the items() method print strings
print("Loop through a dictionary, print strings")
for x, y in thisdict.items():
    print(x, y)
print()

#Dictionary Length
print("Length of dictionary: ")
print(len(thisdict))
print()

#Use the dict() method to make a dictionary
print("Use the dict() method to make a dictionary")
dict2 = dict(name = "John", age = 36, country = "Norway")
print(dict2)
print()

#Change a value in a dictionary
print("Change a value in a dictionary")
dict2["age"] = 37
print(dict2)
print()

#Add items to a dictionary
print("Add items to a dictionary")
dict2["weight"] = 200
print(dict2)
print()

#Remove items from a dictionary
print("Remove items from a dictionary")
dict2.pop("age")
print(dict2)
print()

#Remove last item from a dictionary
print("Remove last item from a dictionary")
dict2.popitem()
print(dict2)
print()

#Clear a dictionary
dict3 = {"name" : "Teacher",
  "country" : "United States"}
print("Clear a dictionary")
dict3.clear()
print(dict3)
print()

#Check if a key exists in a dictionary
print("Check if a key exists in a dictionary")
print("Does the dictionary have the key 'name'?")
print(dict2.get("name"))
print()

#Get the value of the "model" key.
print("Get the value of the 'model' key: ")
print(thisdict.get("model"))
print()
# or assign to a new variable
model = thisdict.get("model")
print(model)
print()