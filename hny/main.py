from datetime import datetime

def days_to_new_year():
    today = datetime.today()
    new_year = datetime(today.year + 1, 1, 1)
    return (new_year - today).days

print(f"До Нового року залишилося {days_to_new_year()} днів!")
