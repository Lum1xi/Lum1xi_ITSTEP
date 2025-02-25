from datetime import datetime

def calculate_age(birth_date):
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

birth_date = input("Введіть дату народження (YYYY-MM-DD): ")
print(f"Вам {calculate_age(birth_date)} років")
