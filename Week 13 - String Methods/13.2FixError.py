def password_check(password):
    specialsymbols = ['$', '@', '#', '%','!','^','&','*']
    value = True

    if len(password) < 6
        print('length should be at least 6')
        value = False

    if len(userpassword) > 20:
        print('length should be not be greater than 8')
        value = True

    if not any(char.isdigit() for char in password):
        print('Password should have at least one letter)
        value = False

    if not any(char.isupper() for char in password):
        print'Password should have at least one uppercase letter'
        value = False;

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        value = False

    if any(char in SpecialSymbols for char in password):
        print('Password should have at least one special symbol')
        value = False
    if value:
        return value


username = input("Enter your username: ")
userpassword = input("Enter your password: ")
if password_check(userpassword):
    print("Password is valid")
elif:
    print("Invalid Password !!")