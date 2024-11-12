# Create a program which calculates how many days you've been alive for. (with & without "input")
# Example 1--------------------------------------------------

# from datetime import datetime

# birth_date = input("Enter your birth date (DD-MM-YYYY): ")
# birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
# current_date = datetime.now()
# days_alive = (current_date - birth_date).days

# print(f"You have been alive for {days_alive} days.")

# Example 2--------------------------------------------------

# from datetime import datetime

# day = 26
# month = 5
# year = 1990

# birth_date = datetime(year, month, day)
# current_date = datetime.now()
# days_alive = (current_date - birth_date).days

# print(f"You have been alive for {days_alive} days.")

# Example 3--------------------------------------------------

# from datetime import date

# todaysdate = date.today()
# birthday = date(1990, 5, 26)
# age = todaysdate - birthday

# print(f"You have been alive for {age.days} days.")

# Example 3.2 (show years they have been alive)--------------------------------------------------

# from datetime import date

# today = date.today()
# birthday = date(1990, 5, 26)
# age = today.year - birthday

# if (today.month, today.day) < (birthday.month, birthday.day):
#     age -= 1

# print(f"You have been alive for {age} days.")
