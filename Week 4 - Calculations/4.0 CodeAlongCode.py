# Let's do some Math!
a = 1
b = 2
c = 5
d = 7
e = 12
f = 15.02
g = 10.01
#h = int(input("Type in an integer: "))
#z = int(input("Tell them you want a number:"))
#i = float(input("Type in a decimal: "))

#Add
y = a + b + c + d
print(y)
#Subtract
y = a-b-c
print(y)
#Multiply
y = a*c
print(y)
#Divide - 2 ways integer and float
y = a/b
print(y)
y = a//b
print(y)
#Modulo
y = a%b
print(y)
y = d%e
print(y)
#Exponents
y = 2**3
print(y)
#PEMDAS
x = 43+13 - 9 / 3 * 7
print(x)
#recast type
x = int(x)
print(type(x))
print(float(x))
print(type(x))

v = 13.45672

print(float("{:.2f}".format(v)))
print(round(v, 2))
