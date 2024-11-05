# print("this is my variables file")

# print("All Around The World"[7].lower()) This will produce the 8th character in the string and make it lowercase


# Hard coded variables, = is a operator
# my_name = "Ron"
# my_age = 34
# is_a_learner = False
# favourite_drink = 'latte'

# print(my_name) # This will produce the name ron as it is now a variable of my_name 

# print(favourite_drink) # will print the favourite_drink variable which is a latte
# print("my favorite drink is", favourite_drink) # will print "my favourite drink is" along with the favourite_drink variable
# print(my_name,"'s favourite drink is'", favourite_drink) # will print the my_name variable before the "text" along with the favourite_drink variable after

# print(my_name,"'s favourite drink is" + favourite_drink) # the plus symbol is concatenation connecting the variables within the string

# print("my favourite drink is" + favourite_drink)
# print(my_name + "'s favourite drink is", + favourite_drink)
# print(my_name + "is" + my_age "their favourite drink is" + favourite_drink) # will produce an error as my_age is an integer

# print("{} is {} years old, and their favourite drink is {}".format(my_name, my_age, favourite_drink)) # dot method {} uses variables within the brackets
# print(f"{my_name} is {my_age} years old, and their favourite drink is {favourite_drink}") # the f string produces the same as the dot method, using f at the beginning to imply the format

# ---------Input Code---------

# user_name = input("Type your name here: > ") # the variable user_name is created using the input function

# print(f"Hello,{user_name}") # it is then printed using the f string to pull the variable user_name
# print(type(user_name)) # will print the user_name and provide the data type for the user_name: 'str' for string
# print(type(user_name)) # even if the user_name is 1234 it will still say the class is 'str' which is incorrect as 1234 is a integer

# print(3+7) # = 10, addition
# print(7-4) # = 3, subtraction
# print(3*2) # = 6, multiplication
# print(3**3) # = 27, to the power of
# print(15/3) # = 5.0, a normal division sum will give a floating point
# print(15%3) # = 0, gives the remainder of the division
# print(16%3) # = 1, gives the ramainder of 3 into 16

# balance = 100 # the variable balance is assigned a value
# amount_to_withdraw = 20 # the variable amount_to_withdraw is assigned a value
# print(balance)
# balance = balance - amount_to_withdraw # balance is reassign to be its value minus the amount_to_withdraw 
# balance -=amount_to_withdraw # balance is reassign to be its value minus the amount_to_withdraw

# balance =-amount_to_withdraw # [INCORRECT SYNTAX] will make balance equal minus the amount the withdraw
# print(balance)

# print("type in two numbers to multiply them")

# num1 = int(input("Number 1: > ")) # int at the beginning uses "casting" to allow an integer to be recognised
# num2 = int(input("Number 2: > ")) # int at the beginning uses "casting" to allow an integer to be recognised

# print(num1*num2)

