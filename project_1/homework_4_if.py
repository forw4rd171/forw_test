while True:
    name = input("Как вас зовут?: ")
    age = int(input("Сколько вам лет?"))
    if age <= 0:
        print("Ошибка, повторите ввод")
    elif age > 0 and age < 10:
        print("Привет шкет," + name)
    elif age >= 10 and age <= 18:
        print("Привет ", name, ", как жизнь? ")
    elif age > 18 and age < 100:
        print("Что желаете,", name, "?")
    elif age > 100:
        print("Вы лжёте, в наше время столько не живут.")
    end = input("Хотите выйти?(Д/Y)")
    if end == 'Д':
        break
    elif end == 'Y':
        break



