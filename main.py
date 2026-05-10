def EatInOrTakeAway():
    EatingLocation = input("Eat in or Take Away?")
    while EatingLocation == 'Eat in' or EatingLocation == 'Take Away':
        if EatingLocation == 'Eat in':
            print("Order please")
        elif EatingLocation == 'Take Away':
            print("Order please")
        else:
            print("I don't get it")