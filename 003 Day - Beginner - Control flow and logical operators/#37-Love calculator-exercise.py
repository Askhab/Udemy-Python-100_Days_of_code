# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
whole_name = name1 + name2
love_number = int(str(whole_name.count("t") + whole_name.count("r") + whole_name.count("u") + whole_name.count("e")) + str(whole_name.count("l") + whole_name.count("o") + whole_name.count("v") + whole_name.count("e")))

if love_number <= 10 or love_number >= 90:
    print(f"Your score is {love_number}, you go together like coke and mentos.")
elif 40 <= love_number <= 50:
    print(f"Your score is {love_number}, you are alright together.")
else:
    print(f"Your score is {love_number}.")
