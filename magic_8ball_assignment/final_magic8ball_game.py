
import random
from colorama import Fore, Style, Back #* we have imported 'colorama' and 'random' library and used their functions

def game_function():    #* we are defining a function that will ask a question, that generates a random number and chooses an item from the relevant list according to set condition.
 input("What is your question?: ")   #user input 

 rdm_num = (random.randint(1,2))   # generation of random number between integers (1,2)- 50% chances of odd/even
 #print(rdm_num)
#* here are two lists, one good and bad, from which the program will randomly select depending on the number generated
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
# Ron suggested even_num = 2 and the randint be (1,3) allowing us to easily determine an odd or even number, 
# After discussion it was suggested that 'randint' being (1,2) would allow for a fairer game, while accomplishing the same task.
#* random.choice was a function we researched to allow us pull a random entry from the lists we have
 random_good = random.choice(good_response) # random.choice pulls a random entry from the list and stored in a variable which would be used ahead for colorama function/styling.
 random_bad = random.choice(bad_response) 
#* if-else condition and output with colorama effects.
 if rdm_num != even_num: #* This checks that the random number is not equal to "2" which is our even number, We decided to use an if statement rather than a while loop.
    print(Fore.RED+f"{random_bad}") # if it is not an even number it prints a [bad response]
 else:
    print (Fore.GREEN+f"{random_good}") # if it is an even number it prints a [good response]

 print(Style.RESET_ALL) # allows the terminal to reset the colour
#* we give the user a choice if they want to ask another question 
# variable used for specific user input and modified to match condition ahead
 repeat= input("Do you want to ask another question? (Y/N): ").strip().lower()
 while repeat != "y" and repeat != "n":  # recursion/ 'while loop' used to run until user input matches to given conditions 
   print("Invalid entry. Please type Y/N")
   repeat= input("Do you want to ask another question? (Y/N): ").strip().lower()
 if repeat == "y":  # revisit the initial function and repeat the whole process
  game_function ()
 elif repeat == "n":  # exit the program. Will use ascii
  print(r"""       Thank You 
         .-'-.
       /   _   \
       |  (8)  |
       \   ^   /
        '-...-'
      For Playing""")   # used ascii to show 8 ball.
# it gives this error message "unterminated string literal" as it cant ignore escape characters such as \.
# to avoid this, we used the "raw strings" prefix "r", "r" will help maintain proper formatting, while using triple quotes (""") handles multi-line strings.

 
game_function() # calling function() to start the program


#--------------------------------------------------------------------------------------------------------
# # shall i put the reflection question here. we can add our answers and then transfer it to a word doc?

# 1] what we did?
# -we planned the program requirements and structured a flowchart as per logic.
# -we created variables, lists (good and bad response)
# -used random library to generate a random integer number (randint)
# -we created a elif conditions to ask the question again
# -we used the colorama library to colour the good/bad response in green/red respectively
# -tried the ascii art for goodbye message to draw (magic 8 ball)
 
# 2] what we expected to happen?
# -to generate a random number and check whether the number is odd/even using modulus
# -random choice of item from appropraite list depending on the odd/ even number
# -we expected the item from good list be in green and bad list be in red
# -for ascii art to work and show magic 8 ball correctly

# 3] what happened?
# -we were getting a range of numbers and wanted to keep the proability fair, hence we chose to pick numbers between 1 and 2
# -we got correct output and crosschecked the number generated matched the elif conditions
# -we got correct colour texts as per the condition
# -ascii art got an error message "unterminated string literal" as it cant ignore escape characters such as \. 

# 4] action required/ taken
# -‘randint(1,2)’ between 1 and 2 (odd/even- with 50% probability)
# -‘function()’ was created in order to repeat the whole process as a block. 
# -we created a while loop to tackle invalid inputs
# -ascii art- we used the "raw strings" prefix "r", "r" will help maintain proper formatting, while using triple quotes (""") handles multi-line strings.
