def currency_converter(amount, currency):
    rates = {"USD": 39, "EUR": 42, "PLN": 9.5}
    return amount / rates[currency] if currency in rates else "Невідома валюта"

uah = float(input("Введіть суму в грн: "))
currency = input("Виберіть валюту (USD, EUR, PLN): ").upper()
print(f"Сума у {currency}: {currency_converter(uah, currency):.2f}")
