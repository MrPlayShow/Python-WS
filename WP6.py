print("Калькулятор базовых математических действий.")
print("= = = Возможные математичесие действия = = =")
print("(+) - Математичесеое сложение")
print("(-) - Математическое вычитание")
print("(*) - Математическое умножение")
print("(/) - Математическое деление")
print("= = = = = = = = = = = = = = = = = = = = = = ")

number1 = int(input("Введите первое число :"))
number2 = int(input("Введите второе число :"))
action = str(input("Введите одно из предложенных действий : (+),(-),(*),(/)"))

if action == "+":
    print(number1 + number2)
elif action == "-":
 print(number1 - number2)
elif action == "*":
 print(number1 * number2)
elif action == "/":
 if number2 == 0:
  print("fail")
 else :
  print(number1 / number2)
 
input("Press enter for close programm")