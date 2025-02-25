import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.(com|ua|org|net|gov)$'
    return "Валідна пошта" if re.match(pattern, email) else "Помилка"

email = input("Введіть email: ")
print(validate_email(email))
