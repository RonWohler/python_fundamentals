# ---------------List Activity 1---------------

# Use a method to find out how many of the folloeing items I've ordered

# egg
# kale
# stamps
# carrot
# orangejuice

# shopping_list = [
#     "apple",
#     "carrot",
#     "pizza",
#     "carrot",
#     "dog food",
#     "orange juice",
#     "egg",
#     "kale",
#     "carrot",
#     "kale",
#     "orange juice",
#     "kale",
#     "toilet roll",
#     "stamps",
#     "noodles",
#     "pasta sauce",
#     "egg",
#     "pasta sauce" ]

# print(f"eggs ordered is",shopping_list.count('egg')) # and so

# ---------------Website addition/removal Activity 2---------------

# websites = [
#     "Youtube.com",
#     "Reddit.com",
#     "ChatGPT.com",
# ]

# print(websites)

# websites.append("Twitch.com") # will insert twitch.com on the end
# websites.insert(0, "Chess.com") # will add Chess.com at index position 0
# print(websites)

# websites.pop() # will remove the last item on the list
# print(websites)

# ---------------Methods, Activity 3---------------

# print(websites)

# websites.remove("Youtube.com") # removes youtube from the list
# print(websites)
# websites.reverse() # reverses the order of the list
# print(websites)
# websites.sort() # sorts the list
# print(websites)
# x = websites.count("Chatgpt.com") # counts the amount of an item
# print(x)

# additional_websites = ["Twitter.com", "Facebook.com"]

# websites.extend(additional_websites) # will add the contents of one list to another
# print(websites)

# ---------------Data Combination/Dictionary, Activity 4---------------

# countries = ["England", "Spain", "Ethiopia", "Iran"]

# languages = ["English", "Spanish", "Amharic", "Farsi"]

# cl_dict = dict(zip(countries, languages))
# print(cl_dict)

# --------------- Animal Search, Activity 5---------------

# create a program which allows a user to search for a animal to recieve its child name

animals = {
    "Cow":"Calf",
    "Cat":"Kitten",
    "Sheep":"Lamb",
    "Frog":"Tadpole",
    "Dog":"Puppy"
} # our animals dictionary


def find_name(animal_name): # Function that takes an animal name as input and returns the name of its baby
    animal_name = animal_name.title() # Converts the input to Title case

    if animal_name in animals: # Checks if the animal name exists in our animals dictionary
        return "A baby " +  animal_name  + " is called a "  +  animals[animal_name] # if you it will return
    else:
        return "This animal is not in our dictionary" # if not found it will return

user_animal = input("Name an animal: >") # asks for the input
print(find_name(user_animal)) # This will print the animals name that is found 

# test_animals = ["cat", "SHEEP", "Bird", "frog"]
# for animal in test_animals:
#     print(find_name(animal))