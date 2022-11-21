# -*- coding: utf-8 -*-
"""Toderinde_PasswordGenerator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1POqQFVPL4ookx6nGRkbwKRMRNmUNt_2D
"""

import string
import random
# characters to generate password from
alphabets=list(string.ascii_letters)
digits=list(string.digits)
characters=list(string.ascii_letters+string.digits+"!,@,#,$,%,^,&,*,-,+")
special_characters=list("!,@,#,$,%,^,&,*,-,+")
def generate_random_password():
        # length of password from the user
        length= int(input("Enter password length: "))
    #number of character types
        alphabets_count = int(input ("Enter alphabets count in password: "))
        digits_count= int(input("Enter digits count in password: "))
        special_characters_count=int(input("Enter special characters count in password: "))
        characters_count=alphabets_count+digits_count+special_characters_count
       ## check the total length with characters sum count
	## print not valid if the sum is greater than length
        if characters_count>length:
                print("Characters total count is greater than the password length")
                return
              ## initializing the password
        password=[]
        ## picking random alphabets
        for  i in range(alphabets_count):
                password.append(random.choice(alphabets))
                ## picking random digits
        for i in range(digits_count):
                password.append(random.choice(digits))
               ## picking random alphabets

      ## if the total characters count is less than the password length
	## add random characters to make it equal to the length
        for i in range(special_characters_count):
                password.append(random.choice(characters))
        if characters_count<length:
                random.shuffle(characters)
                for i in range(length-characters_count):
                        password.append(random.choice(characters))
        ## shuffling the result password
        random.shuffle(password)
        ## converting the list to string
	## printing the list
        print("".join(password))
#While loop is added to your code to check whether the user want to create a password or not.
print("Do you want to create password then choose yes else no:")
input1=input()
while input1=="yes":
        generate_random_password()
        print("Do you want to create password then choose yes else no:")
        input1=input()