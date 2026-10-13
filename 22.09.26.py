'''number = 10
number += 5
print(number) 
number -= 3
print(number)
number *= 4
print(number)'''

'''
first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(round(third_number)) #0, без round будет 0.40002000000000004
'''

'''
print(2.0001 + 0.1) #2.1001000000000003
'''
'''
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number)) #2
'''

'''first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 4)) #Округление до 4 знака после запятой'''

'''print(round(2.49)) #2
print(round(2.51)) #3'''

'''print(round(2.5)) #2 Тут округление идет до ближайшего четного числа
print(round(3.5)) #4 Тут округление идет до ближайшего четного числа

print(round(2.554, 2)) # 2.55
print(round(2.5551, 2)) # 2.56
print(round(2.554999, 2)) # 2.55
print(round(2.499, 2)) # 2.5'''

#Начальное число 5, вам необходимо протащить по всем функциям присвоения перевести в float а потом округлить до сотых с помощью функции round
'''Задача на оценку'''
number = 5 #Изначальная переменнная
number += 3 #Присвоение сложение
print(number) #Вывод с присвоением сложения
number -= 2 #Присвоение вычитания
print(number) #Вывод с присвоением вычитания
number *= 4 #Присвоение умножения
print(number) #Вывод с присвоением умножения
number /= 3 #Присвоение деления
print(number) #Вывод с присвоением деления
number **= 2 #Присвоение степени
print(number) #Вывод с присвоением степени
number //= 5 #Присвоение целочисленного деления
print(number) #Вывод с присвоением уелочисленного деления
number %= 9 #Присвоение остатка от деления
print(round(number, 2)) #Вывод с округлением до сотых

