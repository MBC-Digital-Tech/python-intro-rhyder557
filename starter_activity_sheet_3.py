# starter program week 3 - perhaps this could be a task

def cooking():
    print("Meal planner")
    print()

    # change these to your favourite meals
    print("1. Chicken curry ")
    print("2. Veggie lasagne")
    print("3. Burger and salad")
    # add one more meal here
    print()
    # adapt the next line to add in the 4.
    print("Which of these meals is your favourite? (1, 2 or 3) ")
    # combine the line above and below into one command that accepts an integer instead of a string.
    answer = input()
    # adapt the if else block to include the fourth meal and compares integers instead of strings.
    if answer == "1":
        print("Chicken curry coming up")
    elif answer == "2":
        print("Veggie lasagne coming up")
    else:
        print("Burger and salad coming up!")
    print("Enjoy!")
    
# add a command to run the function above.

