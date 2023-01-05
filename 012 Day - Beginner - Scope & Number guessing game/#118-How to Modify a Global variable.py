# Modifying Global Scope

enemies = 1


# def increase_enemies():
#     global enemies   # we are saying that we use Global Variable in this function
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Instead of changing Global variable we are defining to it this function
def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")
