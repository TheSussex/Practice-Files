favourite_foods = {
    'breakfast': 'rice and plenty meat',
    'lunch': 'garri, kuli and cooold water',
    'dinner': 'semo and egusi with ogufe',
    'snacks': 'chinchin and sausage roll',
}

print("I like to eat " + favourite_foods['breakfast'].title() + " in the morning.")

for time, food in favourite_foods.items():
    print("\nFor " + time.lower() + "," + " I like to eat " + food.title() + ".")

for food in favourite_foods.values():
    print(food.title())

if 'dinner' not in favourite_foods.keys():
    print("What do you eat for brunch?")

    # nesting is storing a set of dictionaries in a list or a list of items as a value in a dictionary.

else:
    print("You don't eat much right?")