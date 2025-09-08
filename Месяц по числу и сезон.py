# #Какое время года сейчас по числу.
A = int(input("Введите число от 1 до 12 :"))
if A == 1:
 print("Месяц","Январь")
if A == 2:
 print("Месяц","Февраль")
if A == 3:
 print("Месяц","Март")
if A == 4:
 print("Месяц","Апрель")
if A == 5:
 print("Месяц","Май")
if A == 6:
 print("Месяц","Июнь")
if A == 7:
 print("Месяц","Июль")
if A == 8:
 print("Месяц","Август")
if A == 9:
 print("Месяц","Сентябрь")
if A == 10:
 print("Месяц","Октябрь")
if A == 11:
 print("Месяц","Ноябрь")
if A == 12:
 print("Месяц","Декабрь")
if A > 0 and A <= 2 or A == 12:
 print("Сезон :","Зима")
if A >= 3 and A <= 5:
 print("Сезон :","Весна")
if A >= 6 and A <= 8:
 print("Сезон :","Лето")
if A >= 9 and A <= 11:
 print("Сезон :","Оосень")
if A > 12 or A <= 0:
 print("error, not found")

input("Press enter for close programm")