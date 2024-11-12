# # Create a Magic 8ball program

# # Create two lists - one of "good" results and one of "bad" results.
# # allow for input.
# # after the question is asked, gen a random number; odd = bad, even = good.
# # use a random method to pick a random fortune from the appropriate list and print it out.

# # Use Colorama to display bad fortunes in red text and good fortunes in green text.

# import random

# good_response = ["It is certain", # A list of common good responses for a magic 8ball
#                  "It is decidedly so",
#                  "Without a doubt",
#                  "Yes definitely",
#                  "You may rely on it"]

# bad_response = ["Don't count on it", # A list of common bad responses for a magic 8ball
#                 "My reply is no",
#                 "My sources say no",
#                 "Outlook not so good",
#                 "Very doubtful",
#                 ]

# even_num = 2
# rdm_num = (random.randint(1,2)) 
# # Ron suggested even_num = 2 and the randint be (1,3) allowing us to easily determine an odd or even number, Joe suggested that randint being (1,2) would allow for a fairer game, while accomplishing the same task.
# # We could use modulus but we have chosen to go with a variable check as our random number can only be 1 or 2.

# rdm_good = random.choice(good_response) # *random.choice pulls a random entry from the list (good_response)
# rdm_bad = random.choice(bad_response) # random.choice was a 

# input("What is your question?: ")

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
# to avoid this, I used the "raw strings" prefix "r", "r" will help maintain proper formatting, while using triple quotes (""") handles multi-line strings.

print(r"""       Thank You 
         .-'-.
       /   _   \
       |  (8)  |
       \   ^   /
        '-...-'
      For Playing""")

# -------ascii test----------- 

