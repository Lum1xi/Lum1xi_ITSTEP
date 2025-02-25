import re

def validate_phone(phone):
    pattern = r'^\+380\d{9}$'
    return "Валідний номер" if re.match(pattern, phone) else "Помилка"

phone = input("Введіть номер телефону: ")
print(validate_phone(phone))
