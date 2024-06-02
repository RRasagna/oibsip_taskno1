import random
import string

# Asking the User to give the length of the password
Password_length = int(input("Enter the length of the Password:"))

# Asking the User to Select the Character type
print("""Select the Character Type: 
      1.Letters 
      2.Numbers 
      3.Characters 
      4.Exit """)

# creating an empty string
character_list = ""

while True:
    # Selecting the character type
    choice = int(input("Pick a Number:"))

    if choice == 1:
        # importing letters from string module
        character_list += string.ascii_letters
    elif choice == 2:
        # importing numbers from string module
        character_list += string.digits
    elif choice == 3:
        # importing special characters from string module
        character_list += string.punctuation
    elif choice == 4:
        break
    else:
        print("Enter Valid Option")

# creating an empty list
password = []

for i in range(Password_length):
    # Selecting a character from character_list
    random_character = random.choice(character_list)
    # adding the selected random character to the list password
    password.append(random_character)

# joining all the elements to a single string
print("The random password is: " + "".join(password))




