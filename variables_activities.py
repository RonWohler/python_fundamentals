# ---------Cash Machine Test---------

# balance = 100
# amount_withdrawn = int(input("Withdraw Amount: > "))

# balance -=amount_withdrawn
# print(f"you have withdrawn: £{amount_withdrawn}, your current balance is: £{balance}")

# ---------Activity 1 name/age/color---------

# name = input("What is your name: > "))
# age = int(input("What is your age: > "))
# favourite_color = input("What is your favourite color: > ").lower()

# print(f"Hello,{name} you are {age} and your favourite color is {favourite_color}, correct?")

# ---------Activity 2 use of operators - num1 (operator) num2---------

# num1 = int(input("please enter a number: > "))
# num2 = int(input("please enter a second number: > "))

# print(f"{num1} plus {num2} = {num1 + num2}") # combined the sum of the 2 numbers using {num1 + num2} and so on
# print(f"{num1} minus {num2} = {num1 - num2}")
# print(f"{num1} divided by {num2} = {num1 / num2}")
# print(f"{num1} times {num2} = {num1 * num2}")
# print(f"{num1} ** {num2} = {num1 ** num2}")
# # print(f"{num1} % (modulus) {num2} = {num1 % num2} ") 

# # ---------Activity 3 Apple/Banana Shop---------

# apple_price = 25
# banana_price = 50

# apples_wanted = int(input("how many apples would you like: > "))
# bananas_wanted =  int(input("how many bananas would you like: > "))

# apples_cost = apples_wanted * apple_price
# print(f"cost of apples = {apples_cost}p")

# bananas_cost = bananas_wanted * banana_price
# print(f"cost of bananas = {bananas_cost}p")

# print (f"Total Cost = {bananas_cost + apples_cost}p") # this will provide the total cost

# total = bananas_cost + apples_cost

# print(f"You bought {apples_wanted} apples") 
# print(f"You bought {bananas_wanted} bananas")
# print(f"Your total is: £{total/100:.2f}") # this method provides the total cost to 2 decimal places - (/100:.2f) denotes 2 decimal places

# ---------Activity 4 password length checking---------

# password = input("Enter your password: ") # this ask for a user to enter a password
# p_len = len(password) # this funtion p_len will find the length of the entered password
# print(p_len) # this will print the length
# if p_len <= 8:
#     print("The password is too short") # if the password 
# else:
#     print(password)

# ---------Activity 5 fizzbuzz variable---------

# num = int(input("please enter a number: > "))

# if num % 3 == 0 and num % 7 == 0:
#         print("fizzbuzz")
# elif num % 3 == 0:
#         print("fizz")
# elif num % 7 == 0:
#         print("buzz")
# else:
#         print(num)

# # ---------Activity 4 "London"---------

# def check_first_last_same(word):
#     if word[0] == word[-1]:
#         return True
#     else:
#         return False

# example_word1 = "radar"
# example_word2 = "hello"

# result1 = check_first_last_same(example_word1)
# result2 = check_first_last_same(example_word2)

# ---------Activity 5---------

