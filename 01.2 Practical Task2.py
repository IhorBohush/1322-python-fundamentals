# Запитуємо користувача ввести два числа
a = input('Введіть перше число: a=')
b = input('Введіть друге число: b=')

# Перетворюємо введені значення типу 'str' на тип даних 'float', щоб не виникало помилки,
# коли користувач введе дробове число
a = float(a)
b = float(b)

# Виводимо результат додавання
print('a + b =', a + b)

# Виводимо результат віднімання
print('a - b =', a - b)

# Виводимо результат множення
print('a * b =', a * b)

# Виводимо результат ділення
print('a / b =', a / b)

# Виводимо результат піднесення до степеню
print('a ** b =', a ** b)

# Виводимо результат цілочисельного ділення
print('a // b =', a // b)

# Виводимо результат остачі ділення
print('a % b =', a % b)
