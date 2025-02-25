from SalaryCalc import calculate_salary
tax=20
def salary_calc():
    print("Ласкаво просимо до Калькулятора Зарплат")
    print("Введіть ваше ім'я")
    name = input()
    print("Введіть кількість відпрацьованих годин")
    hours = int(input())
    print("Введіть ставку за годину")
    rate = int(input())
    print(f"В працівника {name}  Зарплата: {calculate_salary(hourly_rate=rate, hours_worked=hours, tax=tax)} Після відрахування податку {tax}%")
salary_calc()
