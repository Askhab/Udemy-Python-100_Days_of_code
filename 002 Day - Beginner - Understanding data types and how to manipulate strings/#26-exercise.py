# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator.")
pre_bill = float(input("What was the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
peoples = float(input("How many people to split the bill? "))
percent_amount = round(pre_bill * (percent / 100), 2)
total_bill = round((pre_bill + percent_amount) / peoples, 2)
total_bill = "{:.2f}".format(total_bill)

print(f"Each person should pay: {total_bill}")
