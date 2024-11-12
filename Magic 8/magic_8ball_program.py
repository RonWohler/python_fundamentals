# Create an 8ball program

# Create two lists - one of "good" results and one of "bad" results.
# allow for input.
# after the question is asked, gen a random number; odd = bad, even = good.
# use a random method to pick a random fortune from the appropriate list and print it out.

# Use Colorama to display bad fortunes in red text and good fortunes in green text.

# --------------------------------------------------------------------------------First Itteration--------------------------------------------------------------------------------

# While writing this code we used LiveShare along with sharing our screen to help in the collaborate effort.

# import random
# from colorama import Fore, Style, Back # we have imported colorama and random library and used their functions

# def function():
# # here are two lists, one good and bad, from which the program will randomly select depending on the number generated
#  good_response = ["It is certain", # A list of common good responses for a magic 8ball
#                  "It is decidedly so",
#                  "Without a doubt",
#                  "Yes definitely",
#                  "You may rely on it"]

#  bad_response = ["Don't count on it", # A list of common bad responses for a magic 8ball
#                 "My reply is no",
#                 "My sources say no",
#                 "Outlook not so good",
#                 "Very doubtful",
#                 ]

#  even_num = 2

# # Ron suggested even_num = 2 and the randint be (1,3) allowing us to easily determine an odd or even number, After discussion it was suggested that randint being (1,2) would allow for a fairer game, while accomplishing the same task.

#  random_good = random.choice(good_response) # random.choice pulls a random entry from the list (good_response)
#  random_bad = random.choice(bad_response) # random.choice was a function we researched to allow us pull a random entry from the lists we have

# input("What is your question?: ")

#  rdm_num = (random.randint(1,2)) 


#  if rdm_num != even_num: # This checks that the random number is not equal to "2" which is our even number, We decided to use an if statement rather than a while loop in this instance.
#     print(Fore.RED+f"{random_bad}") # if it is not an even number it prints a random [bad response] in red
#  else:
#     print (Fore.GREEN+f"{random_good}") # if it is an even number it prints a random [good response] in green

#  print(Style.RESET_ALL) # allows the terminal to reset the colour

# repeat= input("Do you want to ask another question? (Yes/No): ").strip().lower()
# if repeat == "yes":
#  function ()
# else:
#  print ("Thank you for using Magic 8")
 
# function()

# ------Test Print Functions--------
# print(f"{rdm_num}") # this is an random number check
# print(Style.RESET_ALL) # resets the color for test purposes
# print('back to normal now') # checks if the color has changed for test purposes


# --------------------------------------------------------------------------------Second Itteration--------------------------------------------------------------------------------

import random
from colorama import Fore, Style, Back # we have imported colorama and random library and used their functions

def function():
 input("What is your question?: ")

 rdm_num = (random.randint(1,2)) 
 print(rdm_num)
# here are two lists, one good and bad, from which the program will randomly select depending on the number generated
 good_response = ["It is certain", # A list of common good responses for a magic 8ball
                 "It is decidedly so",
                 "Without a doubt",
                 "Yes definitely",
                 "You may rely on it"]

 bad_response = ["Don't count on it", # A list of common bad responses for a magic 8ball
                "My reply is no",
                "My sources say no",
                "Outlook not so good",
                "Very doubtful",
                ]

 even_num = 2

# Ron suggested even_num = 2 and the randint be (1,3) allowing us to easily determine an odd or even number, After discussion it was suggested that randint being (1,2) would allow for a fairer game, while accomplishing the same task.

 random_good = random.choice(good_response) # random.choice pulls a random entry from the list (good_response)
 random_bad = random.choice(bad_response) # random.choice was a function we researched to allow us pull a random entry from the lists we have

 if rdm_num != even_num: # This checks that the random number is not equal to "2" which is our even number, We decided to use an if statement rather than a while loop.
    print(Fore.RED+f"{random_bad}") # if it is not an even number it prints a [bad response]
 else:
    print (Fore.GREEN+f"{random_good}") # if it is an even number it prints a [good response]

 print(Style.RESET_ALL) # allows the terminal to reset the colour

 repeat= input("Do you want to ask another question? (Y/N): ").strip().lower()
 while repeat != "y" and repeat != "n":
   print("Invalid entry. Please type Y/N")
   repeat= input("Do you want to ask another question? (Y/N): ").strip().lower()
 if repeat == "y":
  function ()
 elif repeat == "n":
   print(r"""       Thank You 
         .-'-.
       /   _   \
       |  (8)  |
       \   ^   /
        '-...-'
      For Playing""")
 
# function()

# -------ascii test----------- 

# this code wont print

# print("Thank You 
#       .-'-.
#     /   _   \
#     |  (8)  |
#     \   ^   /
#      '-...-'
#     For Playing")

# it gives this error message "unterminated string literal" as it cant ignore escape characters such as \.
# to avoid this, we used the "raw strings" prefix "r", "r" will help maintain proper formatting, while using triple quotes (""") handles multi-line strings.

# print(r"""       Thank You 
#          .-'-.
#        /   _   \
#        |  (8)  |
#        \   ^   /
#         '-...-'
#       For Playing""")

# -------ascii test----------- 



