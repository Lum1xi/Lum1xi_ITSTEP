numbers = []

for _ in range(5):
    number = int(input("Введіть число: "))
    numbers.append(number)

max_number = max(numbers)
min_number = min(numbers)

print(f"Найбільше число: {max_number}")
print(f"Найменше число: {min_number}")