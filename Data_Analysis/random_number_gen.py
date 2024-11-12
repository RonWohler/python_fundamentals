import random

# print(random.random()) # gives a random number between 0-1

# print(int(random.uniform(1,10)))

my_number = 13
rdm_number = (random.randint(1,50))

while rdm_number != my_number:
    print(f"my number {my_number} & the rdm {rdm_number} dont match")
    rdm_number = (random.randint(1,50))
print(f"my number {my_number} & the rdm {rdm_number} do match")

