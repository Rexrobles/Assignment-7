# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 

# Greetings
print("Hello! This Program Will Calculate How many Words, Vowels and Consonants are in the input sentence")

# ask input from the user
Sentence = input("Please enter a sentence you like: ")

# word counter
word_ = Sentence.split()

# variables
vowels=0
word=0
consonants=0

#Converting the string to lower case 
str = Sentence.lower();  
for i in range(0,len(Sentence)):   
    # vowel counter
    if str[i] in ('a','e','i','o','u'):  
        vowels = vowels + 1;  
    # consonant counter
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        consonants = consonants + 1;    

