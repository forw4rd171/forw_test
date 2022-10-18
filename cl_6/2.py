input_value = int(input("введите число:"))
q = 0
result = 0
while input_value > q:
    q = q + 1
    if q % 3 == 0:
        continue

    result += q ** 3

print("result to while", result)

result = 0
for item in range(1, input_value + 1):
    if item % 3 == 0:
        continue
    result += item**3

print("result to for", result)