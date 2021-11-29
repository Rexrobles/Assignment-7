# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# output: Valid
# Tip: loop through each character of the input then process it letter by letter

# Greetings
print("Hello! This Program will you if your password is valid")

# ask input from the user
password = input("Please enter your password: ")

character = len(password)
SpclChar, upper, lower, digit = 0, 0, 0, 0

# condition
if (len(password) >=15):
    for i in password:
        if (i.islower()):
            lower +=1
        if (i.isdigit()):
            digit +=1
        if (i.isupper()):
            upper +=1
        if (i == "#" or i == "@" or i == "=" or i == "!" or i == "$" or i == "&" or i == "%" or i == "'" or i == "*" or i == "()" or i == "+ " or i == "." \
        or i == "|" or i == """^""" or i == "{" or i == "}" or i == "[" or i == "]" or i == "_" or i == "~" or i == "," or i == "?" or i == "+"):
            SpclChar += 1
            
    if (lower >= 1 and upper >= 1 and SpclChar >= 1 and digit >= 1):
        print("Your password is: ")
    if (upper < 1 ):
        print("Oh no! Your password must contain atleast one capital letter.")
    if (digit < 1 ):
        print("Oh no! Your password must contain atleast one number.")
    if (SpclChar < 1 ):
        print("Oh no! Your password must contain atleast one special character.")
    if (lower <= 1 and SpclChar <= 1 and digit <= 1 and upper <=1):
        print("Sorry! The password you have enter is invalid")
else:
    for i in password:
        if (i.islower()):
            lower +=1
        if (i.isdigit()):
            digit +=1
        if (i.isupper()):
            upper +=1
        if (i == "#" or i == "@" or i == "=" or i == "!" or i == "$" or i == "&" or i == "%" or i == "'" or i == "*" or i == "()" or i == "+ " or i == "." \
        or i == "|" or i == """^""" or i == "{" or i == "}" or i == "[" or i == "]" or i == "_" or i == "~" or i == "," or i == "?" or i == "+"):
            SpclChar += 1
            
    print ("Oh no! Your password must have atleast fifteen characters.")
    if (digit < 1):
        print ("Oh no ! Your password must contain atleast one number.")
    if (SpclChar < 1):
         print("Oh no ! Your password must contain atleast one special character.")
    if (upper < 1):
        print("Oh no ! Your password must contain atleast one capital letter.")
        
print("Sorry! The PASSWORD you have entered is INVALID")
