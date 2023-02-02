with open(r"file1.txt", "r") as file1:
    numbers1 = [int(item) for item in file1.readlines()]

with open(r"file2.txt", "r") as file2:
    numbers2 = [int(item) for item in file2.readlines()]

result = [number for number in numbers1 if number in numbers2]

# Write your code above 👆

print(result)
