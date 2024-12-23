# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# In Python a function is defined using the def keyword:

def my_function():
    print("Hello from a function")

# To call a function, use the function name followed by parenthesis:

# The function must be defined above the call.

my_function()


# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with two arguments (fname,lname):

def name_function(fname, lname):
    print(fname + " " + lname)


name_function("Lucy", "Young")

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# name_function("Lucy", "Kay", "Young")

# Can add a default value for an argument

def age(age = 12):
    print("I am " + str(age))


age()
age(11)

# Can ask for user input and then use those variables as arguments in a function.

user_first_name = input("Please enter your first name: ")
user_last_name = input("Please enter your last name: ")
name_function(user_first_name, user_last_name)
