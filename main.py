from field import water




def print_battle_field():
    for row in water:
        for col in row:
            print(col, end=" ")
        print()

print_battle_field()