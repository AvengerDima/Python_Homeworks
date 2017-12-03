import math

#Задача №14
print("Задача №14 \n Задание: Написать функцию, которая будет проверять четность некоторого числа. \n Решение:")
def is_even(numbers):
    if numbers % 2 == 0:
        print('True')
    else:
        print('False')
is_even(6)
#----------------------------------------------------
#Задача №15
print("Задача №15 \n Задание: Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости. Каждая окружность задается координатами центра и радиусом. \n Решение:")
x1 = 6
x2 = 3
y1 = 9
y2 = 8
r1 = 1
r2 = 5

def cirles_intersection(x1, y1, r1, x2, y2, r2):
    center = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    d = center
    return (d < r1 + r2 and (r1 - r2)) or (d == r1 + r2) or (r1 == d + r2) or (d == 0 and r1 == r2)

if cirles_intersection(x1, y1, r1, x2, y2, r2):
    print("Окружность пересекается.")
else:
    print("Окружность не пересекается.")
# ----------------------------------------------------
# Задача №16
print("Задача №16 \n Задание: Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда. \n Решение:")
def have_trains_crashed(v1, v2):
    if 4 / v1 >= 6 / v2:
        print("Поезда столкнутся")
    else:
        print("Поезда не столкнутся")
have_trains_crashed(50, 30)
# ----------------------------------------------------