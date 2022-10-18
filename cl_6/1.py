while True:
    name = input("Как вас зовут? ")
    age = input("Сколько вам лет? ")
    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод")
    elif int(age) < 10:
        print(f"Привет, шкет {name}")
    elif int(age) <= 18:
        print(f"Как жизнь {name}?")
    elif int(age) < 100:
        print(f"Что желаете {name}?")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")  # все остальное


    answer = input("Желаете выйти? (Y/Д): ")
    if answer.upper() in ('Y', 'Д'):
        break