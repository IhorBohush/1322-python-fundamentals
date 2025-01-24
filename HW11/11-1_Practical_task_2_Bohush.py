def number_day():
    while True:
        try:
            number = input('Enter number "1-7" or "q" to exit: ')
            match number:
                case '1': day = 'Monday'
                case '2': day = 'Tuesday'
                case '3': day = 'Wednesday'
                case '4': day = 'Thursday'
                case '5': day = 'Friday'
                case '6': day = 'Saturday'
                case '7': day = 'Sunday'
                case 'q':
                    print('Good by!')
                    break
                case _: raise ValueError('Wrong data')
            print(day)
        except ValueError as e:
            print(e)


number_day()
