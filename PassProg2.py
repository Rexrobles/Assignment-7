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
password = input("Please enter \33[96m\33[1mPASSWORD\33[0m : ")

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
        print("Your \33[36m\33[1mPASSWORD\33[0m is \33[1m\33[95mVALID\33[0m!")
    if (upper < 1 ):
        print("Oh no! Your password must contain \33[36m\33[1m\33[3matleast one capital letter.\33[0m") 
    if (digit < 1 ):
        print("Oh no! Your password must contain \33[36m\33[1m\33[3matleast one number.\33[0m")
    if (SpclChar < 1 ):
        print("Oh no! Your password must contain \33[36m\33[1m\33[3matleast one special character.\33[0m")
    if (lower <= 1 and SpclChar <= 1 and digit <= 1 and upper <=1):
        print("Sorry! The \33[36m\33[1mPASSWORD\33[0m you have entered is \33[33m\33[1mINVALID\33[0m")
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
            
    print ("Oh no! Your password must have \33[96m\33[1m\33[3matleast fifteen characters.\33[0m")
    if (digit < 1):
        print("Oh no! Your password must contain \33[36m\33[1m\33[3matleast one number.\33[0m")
    if (SpclChar < 1):
         print("Oh no! Your password must contain \33[36m\33[1m\33[3matleast one special character.\33[0m")
    if (upper < 1):
        print("Oh no! Your password must contain \33[36m\33[1m\33[3matleast one capital letter.\33[0m")
        
print("Sorry! The \33[36m\33[1mPASSWORD\33[0m you have entered is \33[33m\33[1mINVALID\33[0m")
