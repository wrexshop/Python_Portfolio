# Day 5 Project - Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

def getChars(char_list, count):
    if count > 0:
        for i in range (1, count+1):
            password.append(random.choice(char_list))
    return password

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

getChars(letters, nr_letters)
getChars(numbers, nr_numbers)
getChars(symbols, nr_symbols)

# Randomize the order of the chars
random.shuffle(password)

# Convert the list into a string
password = ''.join(password)

# Display password to the user
print("Here is your randomized passowrd: {}".format(password))
