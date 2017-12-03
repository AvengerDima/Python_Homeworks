import math
import random

#Задача №17
print("Задача №17 \n Задание: Написать функцию решения квадратного уравнения. \n Решение:")
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = None
        return x1, x2
    else:
        x1 = None
        x2 = None
        return x1, x2
print(solve_quadratic_equation(5, 10, -15))
#----------------------------------------------------
#Задача №18
print("Задача №18 \n Задание: Каждому символу в таблице символов Unicode соответствует число. Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам, стоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’. \n Решение:")
first = 'x'
last = 'z'

def sum_symbol_codes(first, last):
    first_ord = ord(first)
    last_ord = ord(last)
    if first_ord <= last_ord:
        lower_bound = first_ord
        upper_bound = last_ord
    else:
        lower_bound = last_ord
        upper_bound = first_ord
    sum_symbol = 0
    for symbol in range(lower_bound, upper_bound + 1):
        sum_symbol += symbol
    return sum_symbol


print(" Число:" ,sum_symbol_codes(first, last))
#----------------------------------------------------
#Задача №19
print("Задача №19 \n Задание: Написать функцию для поиска разницы между максимальным и минимальным числом среди num_limit случайно сгенерированных чисел в указанном числовом диапазоне. \n Решение:")
print(" Поиск максимального значения:")
def find_max_of_n(num_limit, lower_bound, upper_bound):
    curr_max = lower_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print(' Рандомное число: ', rand_number)
        if rand_number > curr_max:
            curr_max = rand_number

    return curr_max

result = find_max_of_n(5, 100, 300)
print(" Максимальное значение: %d" % result)
print("---------------")
print(" Поиск минимального значения:")
def find_min_of_n(num_limit, lower_bound, upper_bound):
    curr_min = upper_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print(' Рандомное число: ', rand_number)
        if rand_number < curr_min:
            curr_min = rand_number

    return curr_min

result = find_min_of_n(5, 100, 500)
print(" Минимальное значение: %d" % result)
#----------------------------------------------------
#Задача №20
print("Задача №20 \n Задание: Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди 100 случайно сгенерированных чисел в произвольном числовом диапазоне. Т.е. от суммы четных чисел вычесть сумму нечетных чисел. \n Решение:")
def diff_even_odd(num_limit, lower_bound, upper_bound):
    even_sum = 0
    odd_sum = 0
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print(' Рандомное число: ', rand_number)
        if rand_number % 2 == 0:
            even_sum += rand_number
        else:
            odd_sum += rand_number

    print(" Сумма четных чисел: %d" % even_sum)
    print(" Сумма нечетных чисел: %d" % odd_sum)
    return even_sum - odd_sum

print(diff_even_odd(100, 10, 100))
#----------------------------------------------------
