import  math

#Задача №11
print("Задача №11 \n Задание: Написать функцию, которая будет переводить градусы в радианы. Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов. \n Решение:")
def radians(degrees):
    answer = (degrees * math.pi) / 180
    return answer
x = 40
answer = radians(x)
print("Косинус угла: 40° =", math.cos(answer))

y = 45
answer = radians(y)
print("Косинус угла: 45° =", math.cos(answer))

z = 60
answer = radians(z)
print("Косинус угла: 60 =°", math.cos(answer))
#----------------------------------------------------

#Задача №12
print("Задача №12 \n Задание: Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в консоли, без использования операторов цикла. Реализовать задачу без использования строк. \n Решение:")
def number_n(three_digits_number):

    a = three_digits_number // 100
    b = three_digits_number % 100 // 10
    c = three_digits_number % 10
    sum_of_digits = a + b + c
    print(" Сумма цифр трехзначного числа = %d" % (sum_of_digits))
    return  sum_of_digits
print(" Трехзначное число: 160")
answer = number_n(160)
#----------------------------------------------------

#Задача №13
print("Задача №13 \n Задание: Пользователь вводит длины катетов прямоугольного треугольника. Написать функцию, которая вычислит площадь треугольника и его периметр. Результат работы функции вывести на печать. \n Решение:")
#Формула Герона
def triangle_and_perimeter(catheter_a, catheter_b):
    square = (catheter_a * catheter_b) / 2
    hypotenuse_c = math.sqrt((catheter_a)**2) + ((catheter_b)**2)
    p = hypotenuse_c + catheter_a + catheter_b
    print(" Площадь треугольника равна: %.2f \n Периметр треугольника равен: %.2f" % (square, p))
    return square, p
catheter_a = 10
catheter_b = 10
answer = triangle_and_perimeter(catheter_a, catheter_b)
#----------------------------------------------------

