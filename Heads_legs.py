# Запитуємо ввести кількість голів і кількість ніг
heads = input('Input number of the heads: ')
legs = input('Input number of the legs: ')

# Переводимо дані із "str" в "int"
heads = int(heads)
legs = int(legs)

# Створюємо словник для додавання даних в нього
animals = {}

# Перевіряємо введені дані
# Якщо кількість ніг чи голів від'ємна - виводимо "Немає розв'язків"
if heads < 0 or legs < 0:
    print('No solutions')
# Якщо кількість ніг чи голів дорівнює 0, то відповідно кількість курей має бути 0 і корів - 0
elif heads == 0 or legs == 0:
    animals['Chickens'] = 0
    animals['Cows'] = 0
    print(animals)

# Якщо всі числа додатні рахуємо по формулі: cows = (legs - 2 * heads) / 2; chickens = heads - cows
else:
    x = (legs - 2 * heads)
# Перевіряємо цю частину формули чи не від'ємне значення, якщо від'ємне - виводимо "Немає розв'язків"
    if x < 0:
        print('No solutions')
# Далі перевіряємо остачу від ділення на 2
    else:
        y = x % 2
# Якщо остача не дорівнює 0 - виводимо "Немає розв'язків"
# Якщо остача дорівнює 0 - продовжуємо розв'язувати задачу
        if y == 0:
            cows = int(x / 2)
            chickens = heads - cows
# Якщо кількість курей від'ємна - виводимо "Немає розв'язків"
            if chickens < 0:
                print('No solutions')
# Всі інші значення додаємо в словник і виводимо отримані значення
            else:
                animals['Chickens'] = chickens
                animals['Cows'] = cows
                print(animals)
        else:
            print('No solutions')
