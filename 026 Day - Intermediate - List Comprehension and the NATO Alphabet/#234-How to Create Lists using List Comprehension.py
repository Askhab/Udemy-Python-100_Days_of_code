# numbers = [1, 2, 3]
# new_list1 = []
#
# for n in numbers:
#     add_1 = n + 1
#     new_list1.append(add_1)

# new_list2 = [num + 1 for num in numbers]

# print(new_list2)

# doubled_num = [num * 2 for num in range(1, 5)]
# print(doubled_num)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)
