#Задача №7
print("Задача №7 \n Задание: Преобразовать строку с американским форматом даты в европейский. Например, 05.17.2016 преобразуется в 17.05.2016. \n Решение:")
print(" Американский формат даты: 03.11.1998")
date_american = '03.11.1998'
lst = date_american.split('.')
date_european = '%s.%s.%s' % (lst[1], lst[0], lst[2])
print(" Европейский формат даты:", date_european, "\n")
#----------------------------------------------------

#Задача №8
print("Задача №8 \n Задание: Написать программу, которая преобразует имя студента, ставя фамилию на первое место, а имя на второе. Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘. \n Решение:")
print(" Имя, Фамилия: Дмитрий Семков")
text = "Дмитрий Семков"
str = text.split(' ')
text2 = '%s %s' % (str[1], str[0])
print(" Фамилия, Имя:", text2, "\n")
#----------------------------------------------------

#Задача №9
print("Задача №9 \n Задание: Написать программу, которая преобразует имя переменной в формате snake_style в формат CamelizedStyle. \n"
      "          Для простоты считаем, что имя переменной всегда состоит из 3-х слов. \n"
      "          Например: ‘employee_first_name’ -> ‘EmployeeFirstName’ \n Решение:")
var = " language_programming _python"
print(var)
lst = var.split("_")
language = lst[0]
programming = lst[1]
python = lst[2]
result = language.title() + programming .title() + python.title()
print(result, "\n")
#----------------------------------------------------

#Задача №10
print("Задача №10 \n Задание: Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'. В этой строке указаны имя писателя и через символ * даты рождения и смерти. Даты указаны в формате YYYY-MM-DD. \n"
      "          Требуется написать программу, которая по переданной строке определит возраст писателя и вернет его имя и возраст. Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' \n"
      "          программа должна вернуть: 'Leo Tolstoy, 82'. Для строки 'Marcus Aurelius*121-04-26*180-03-17' вернуть 'Marcus Aurelius, 59'. Т.е. индексы символов разделителей ('*', '-')\n"
      "          незафиксированы! Месяцы и дни можно игнорировать. \n Решение:")
print(" Первый писатель: Leo Tolstoy*1828-08-28*1910-11-20")
text = "Leo Tolstoy*1828-08-28*1910-11-20"
lst = text.split('*')

name = lst[0]
birth_date = lst[1]
death_date = lst[2]

birth_date_lst = birth_date.split('-')
death_date_lst = death_date.split('-')

birth_year = birth_date_lst[0]
death_year = death_date_lst[0]

age = int(death_year) - int(birth_year)

print(" Возраст: %s, %d" % (name, age))
#------
print(" Второй писатель: Marcus Aurelius*121-04-26*180-03-17")
text1 = "Marcus Aurelius*121-04-26*180-03-17"
lst1 = text1.split('*')

name1 = lst1[0]
birth_date = lst1[1]
death_date = lst1[2]

birth_date_lst1 = birth_date.split('-')
death_date_lst1 = death_date.split('-')

birth_year = birth_date_lst1[0]
death_year = death_date_lst1[0]

age1 = int(death_year) - int(birth_year)

print(" Возраст: %s, %d" % (name1, age1))
#----------------------------------------------------
