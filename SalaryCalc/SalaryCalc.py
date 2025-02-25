def calculate_salary(hourly_rate, hours_worked, tax):
    return (hourly_rate * hours_worked) - (hourly_rate * hours_worked * (tax / 100))