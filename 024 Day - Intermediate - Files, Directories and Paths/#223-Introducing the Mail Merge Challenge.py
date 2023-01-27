with open(r"Input/Letters/starting_letter.txt", "r") as origin:
    origin = origin.readlines()

with open(r"Input/Names/invited_names.txt", "r") as names:
    names = names.readlines()


def clear_string(arr):
    clear_list = []
    for i in arr:
        if i == "\n":
            del i
        else:
            clear_list.append(i.strip("\n"))
    return clear_list


origin = clear_string(origin)
names = clear_string(names)

for i in range(len(names)):
    with open(rf"Output/ReadyToSend/letter_for_{names[i]}.txt", "w") as new_letter:
        for j in origin:
            if "[name]" in j:
                j = j.replace("[name]", f"{names[i]}")
            new_letter.writelines([j, "\n\n"])
