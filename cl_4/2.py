num = input('Введите 5 разных чисел, разделенных запятыми:')
lst = [int(n) for n in num.split(',')]
print([n for n in lst if (int(n)%2) == 0])
print(str(num)[::-1])