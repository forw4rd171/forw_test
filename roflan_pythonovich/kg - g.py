a = input("Введите kg:")

value = int(a.replace('kg', '').replace('g', '').replace('t', ''))

if "kg" in a:
    print(str(value / 1000) + "t")
    print(str(value * 1000) + "g")

elif "g" in a:
    print(str(value / 1000) + "kg")
    print(str(value / 100000) + "t")

elif "t" in a:
    print(str(value * 1000) + "kg")
    print(str(value / 1000000) + "g")