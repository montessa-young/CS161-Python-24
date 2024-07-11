shirtdict = {"brand": "Carhartt",
            "size": "Large",
            "color": "brown",
            "stock": 200}
#

shirtdict["size"] = "Medium"
print(shirtdict)
#

shirtdict["stock"] = shirtdict["stock"] - 1
print(shirtdict["stock"])
#

print(len(shirtdict))
#

print(shirtdict["color"])
#

for x in shirtdict.items():
    print(x)
#

shirtdict["length"] = "long"
print(shirtdict)
#

shirtdict.pop("brand")
print(shirtdict)
#

print(shirtdict.get("size"))
#

variable = shirtdict.get("size")
print(variable)
# specifically what is different from the above code that uses get()?
#
