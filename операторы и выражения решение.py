print('Задача 1.', "✣" * 50)

import math

a, b = map(int, input("Введите два целых числа через пробел: ").split())

print("Сумма a и b:", a + b)
print("Разность a и b:", a - b)
print("Произведение a и b:", a * b)
print("Частное от деления a на b:", a / b)
print("Остаток от деления a на b:", a % b)
print("Десятичный логарифм a:", math.log10(a))
print("Результат возведения a в степень b:", a ** b)
print("Квадратный корень из a:", math.sqrt(a))
print("Результат умножения e на b:", math.e * b)

print()
print('Задача 2.', "✣" * 50)

# Создаем список с шагом 3

lst = list(range(1, 20, 3))
print("Список:", lst)

# 1. Выводим длину списка
print("Длина списка:", len(lst))

# 2. Выводим все элементы списка, начиная со второй позиции
print("Элементы списка, начиная со второй позиции:", lst[1:])

# 3. Выводим все четные элементы списка
print("Четные элементы списка:", [x for x in lst if x % 2 == 0])

# 4. Выводим все элементы списка, делящиеся на 5 без остатка
divisible_by_5 = [x for x in lst if x % 5 == 0]
if divisible_by_5:
    print("Элементы списка, делящиеся на 5 без остатка:", divisible_by_5)
else:
    print("Элементов, делящихся на 5, нет")

# 5. Сортируем список в порядке убывания
lst.sort(reverse=True)
print("Список, отсортированный в порядке убывания:", lst)

# 6. Рассчитываем квадраты элементов списка
squares = list(map(lambda x: pow(x, 2), lst))
print("Квадраты элементов списка:", squares)

# 7. Выводим элементы списка в обратном порядке
print("Элементы списка в обратном порядке:", lst[::-1])

# 8. Рассчитываем выборочное среднее
n = len(lst)
mean = sum(lst) / n

print("Выборочное среднее:", mean)

print()
print('Задача 3.', "✣" * 50)

# Можно представить информацию в виде списка кортежей,
# каждый из которых будет содержать день недели и температуру воздуха:


temperatures = [('понедельник', 12.0), ('вторник', 12.0), ('среда', 17.0), ('четверг', 17.0),
                ('пятница', 14.3), ('суббота', 11.9), ('воскресенье', 12.0)]

fahrenheit_temperatures = []
for temp in temperatures:
    celsius_temp = temp[1]
    fahrenheit_temp = round(9/5 * celsius_temp + 32, 2)
    fahrenheit_temperatures.append((celsius_temp, fahrenheit_temp))
print(*fahrenheit_temperatures)

# - Чтобы найти день(дни) с максимальной/минимальной температурой, можно использовать функции `max()` и
# `min()`, примененные к списку кортежей. Для вывода только названия дня можно использовать индекс 0:


max_temp = max(temperatures, key=lambda x: x[1])[0]
min_temp = min(temperatures, key=lambda x: x[1])[0]
print(f"Максимальная температура была - {max_temp}, минимальная - {min_temp}")

# - Среднее значение температуры за неделю можно вычислить, пройдя циклом по списку и суммируя значения температур,
# а затем разделив на количество элементов:


average_temp = sum([temp[1] for temp in temperatures])/len(temperatures)
print(f"Средняя температура за неделю: {int(average_temp)} celsius")

# - Модальное значение - это значение, которое встречается в списке наибольшее количество раз.
# Для решения этой задачи можно использовать библиотеку `collections` и ее метод `Counter()`:


from collections import Counter

c = Counter([temp[1] for temp in temperatures])
mode_temp = c.most_common(1)[0][0]
print(f"Модальное значение температуры: {mode_temp}")

# - Чтобы вывести список "прохладных" и "теплых" дней,
# можно пройтись циклом по списку и проверять условие с помощью оператора `if`.
# Для удобства можно создать два списка:


cool_days = []
warm_days = []

for temp in temperatures:
    if temp[1] < 14:
        cool_days.append(temp[0])
    else:
        warm_days.append(temp[0])

print("Прохладные дни:", ", ".join(cool_days))
print("Теплые дни:", ", ".join(warm_days))

print()
print('Задача 4.', "✣" * 50)

disc = ['Алгебра', 'Геометрия', 'Топология']
student = ['Сидоров', 'Иванов', 'Петров', 'Иванова']
grades_student = [[2, 4, 4], [3, 4, 4], [3, 3, 3], [5, 5, 5]]

#1. С помощью методов `dict()` и `zip()`:

grades_dict = dict(zip(student, grades_student))
print(grades_dict)

#2. С помощью цикла `for` и метода `enumerate()`:

grades_dict = {}
for i, name in enumerate(student):
    grades_dict[name] = dict(zip(disc, grades_student[i]))
print(grades_dict)

#3. Для нахождения фамилий круглых отличников:

for name, grades in grades_dict.items():
    if all(grade == 5 for grade in grades.values()):
        print(name)

#Для нахождения студентов, несдавших сессию:

for name, grades in grades_dict.items():
    if any(grade < 3 for grade in grades.values()):
        print(name)

print()
print('Задача 5.', "✣" * 50)

#Решение задачи с использованием цикла `while`:


n = int(input("Введите число от 3 до 50: "))
sum_even = 0
i = 2

while i < n:
    if i % 2 == 0:
        sum_even += i
    i += 2

print("Сумма четных чисел, меньших -", n, "равна:", sum_even)

print()
print('Задача 6.', "✣" * 50)

text = """Взвейтесь кострами, синие ночи!

Мы пионеры - дети рабочих

Близится время светлых годов

Клич пионера: "Всегда будь готов!"

Радостным шагом с песней веселой

Мы выступаем за комсомолом

Близится время светлых годов

Клич пионера: "Всегда будь готов!"

Мы поднимаем красное знамя

Дети рабочих, смело за нами!

Близится время светлых годов

Клич пионера: "Всегда будь готов!"

Взвейтесь кострами, синие ночи!

Мы пионеры - дети рабочих

Близится время светлых годов

Клич пионера: "Всегда будь готов!"

Клич пионера: "Всегда будь готов!" """

# Приведение к нижнему регистру
text = text.lower()

# Считаем количество строк
num_lines = len(text.split('\n'))
print("Количество строк в тексте:", num_lines)

# Считаем количество предложений
num_sentences = 0
for char in text:
    if char in ('.', '!', '?'):
        num_sentences += 1
print("Количество предложений в тексте:", num_sentences)

# Считаем количество уникальных слов и создаем частотную таблицу
word_freq = {}
words = text.split()
for word in words:
    if word.isalpha():
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
num_unique_words = len(word_freq)
print("Количество уникальных слов в тексте:", num_unique_words)

# Выводим частотную таблицу
print("Частотная таблица:")
for word, freq in word_freq.items():
    print(word, ":", freq)

# Считаем количество уникальных букв
unique_letters = set(text.replace('\n', '').replace(' ', ''))
num_unique_letters = len(unique_letters)
print("Количество уникальных букв в тексте:", num_unique_letters)












