# Import the random module here
from random import choice
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(f"{choice(names)} is going to buy the meal today!")
