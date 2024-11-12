# Returns the absolute value of a number
# print(abs(-5))  # Output: 5

# Converts a value to an integer
# print(int(3.8))  # Output: 3

# Converts a value to a floating-point number
# print(float(10))  # Output: 10.0

# Returns the length of a string, list, tuple, etc.
# print(len("Hello"))  # Output: 5

# Finds the largest number in a list or set of arguments
# print(max(3, 7, 2))  # Output: 7

# Finds the smallest number in a list or set of arguments
# print(min(3, 7, 2))  # Output: 2

# Rounds a floating-point number to the nearest integer
# print(round(3.6))  # Output: 4

# Returns the sum of all items in an iterable (list, tuple, etc.)
# print(sum([1, 2, 3, 4]))  # Output: 10

# Converts a number or string to a string type
# print(str(123))  # Output: "123"

# Returns True if all elements in an iterable are True
# print(all([True, True, False]))  # Output: False

# Returns True if any element in an iterable is True
# print(any([False, False, True]))  # Output: True

#------------------------------------------------------------------------------

# def greet(): # 'def' is used to define a new function, It specifies the function name, parameters (if any), and the block of code to execute.
#     print("Hello, world!")

# greet() # calling the funtion will execute its code block.

#------------------------------------------------------------------------------

# def say_something(something): # the funtion (say_something) has a parameter (something)
#     print(f"{something}")

# say_something("hello") # "hello" is the arguement that fills in the parameter
# say_something("This is a arguement filling in a parameter")

#------------------------------------------------------------------------------

# def cash_withdrawal(amount, accnum):
#     print(f"You have withdrawn £{amount} from account:{accnum}")

# cash_withdrawal(300, 123456789)
# cash_withdrawal(50, 987654321)

#------------------------------------------------------------------------------

# make a funtion called take order, funtion needs 2 parameters [size, type of drink]
# print, reciept. "you have ordered a "" size of drink"

# def take_order(size, drink_type):
#     print(f"You have ordered a {size} size {drink_type}.")
          
# take_order("large", "Coffee")
# take_order("small", "Tea")

#------------------------------------------------------------------------------

# this code uses a global variable, allows for a variable to be changed within a function.
# balance = 500

# def cash_withdrawal(amount, accnum):
#     global balance # Defines balance as a global variable
#     print(f"Your current balance is: £{balance}")
#     print(f"You have withdrawn £{amount} from account:{accnum}")
#     balance -= amount
#     print(f"Your new balance is: £{balance}")

# cash_withdrawal(300, 123456789)
# cash_withdrawal(150, 123456789)

#------------------------------------------------------------------------------
