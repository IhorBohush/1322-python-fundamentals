def age_status():
    while True:
        try:
            age = input('Enter your age or "q" to exit: ')
            if age != "q":
                age = int(age)
                if age <= 0:
                    raise ValueError(f'That is not a positive number: {age}')
                elif age % 2 == 0:
                    print('Your age is an even number')
                else:
                    print('Your age is an odd number')
            else:
                break
        except ValueError as e:
            print(e)


age_status()
