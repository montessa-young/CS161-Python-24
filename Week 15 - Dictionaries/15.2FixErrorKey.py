# Fix all the errors in the code, so it successfully runs and properly prints the Quidditch roster

quidditch_dict = {
    "Harry Potter": "Gryffindor",
    "Fred Weasley": "Gryffindor",
    "Cedric Diggory": "Hufflepuff",
    "Zacharias Smith": "Hufflepuff",
    "Vincent Crabbe": "Slytherin",
    "Draco Malfoy" : "Slytherin",
    "Roger Davies": "Ravenclaw",
    "Cho Chang": "Ravenclaw"}

print(quidditch_dict)

print("Remove Cedric Diggory from roster: ")
quidditch_dict.pop("Cedric Diggory")
print(quidditch_dict)

print("Print only the names of the students in the Hufflepuff team: ")
for key, value in quidditch_dict.items():
    if value == "Hufflepuff":
        print(key)