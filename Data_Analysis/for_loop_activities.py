# Activity 1: create a for loop printing hello world 13 times

# for i in range(1, 14):
#     print("Hello World")

# ---------------------------------------------------------------
# Activity 2: create a while loop printing hello world 13 times

# i = 1
# while i < 14:
#     print("Hello World")
#     i +=1
#     print()

# ---------------------------------------------------------------
# Activity 3: Nested for loop, print the multiplication from 1 to 12 ex "1x1 upto 12x12"

# for i in range(1,13):
#     for j in range(1,13):
#         print(f"{i} x {j} = {i * j}")

# ---------------------------------------------------------------
# Activity 4: small log-in program,  user can't login until they type this password: St@t1st1cs
    # Add a limit to this ("stretch activity")

# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:
#     password = input("Type your password: ")
#     if password == "St@t1st1cs":
#         print("Welcome Back")
#         break
#     else:
#         attempts += 1
#         print("Password Incorrect")
#         print(f"You have {max_attempts - attempts} remaining attempt(s)")
      
# if attempts == max_attempts:
#         print("max attempts reached")

# ---------------------------------------------------------------
# Activity 5 - create a parameter which asks for a name then says happy birthday "name"

# def birthday(name):
#     print(f"Happy Birthday to {name}")

# birthday(input("What is your name: "))

# ---------------------------------------------------------------
# Activity 6 - modify code to allow for more parameters with a updated order count 

order_count = 1

def take_order(topping, size, extra ):
     global order_count
     print(f"{order_count} - {topping} Pizza {size} inch with extra {extra}")
     order_count += 1

take_order("Pineapple", "14", "cheese")
take_order("Pepperoni", "12", "cheese")

# ---------------------------------------------------------------
# Activity 7 - find the mean in this data set

# dataset = [34,67,5,81,2,45,9,23,55,41,42,84,109, 109, 109]

