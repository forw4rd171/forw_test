import random
random_value = random.randint(0,100)
attempt = 0
print ("Отгадайте число от 0 до 100, у вас есть 10 попыток.")
for i in range(1,11):
    choice = int(input("Введите число: "))
    if choice > random_value:
        print("Слишком много")
    elif choice < random_value:
        print("Слишком мало")
    else:
        print(f"Правильно! Количество попыток - {i}")
        break
    attempt += 1

if attempt >=10:
    print("Попытки исчерпаны!Было загадано:(random_value)")