# There is no Block Scope

game_level = 3


def create_enemy():
    enemies = ["Skeletons", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]


print(new_enemy)   # Error - because if statement doesn't have local scope and inside function it has function's local scope
