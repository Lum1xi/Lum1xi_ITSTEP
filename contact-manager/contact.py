contact_dic = {}  # {Name: {"Phone": "+380123456789", "Email": "example@example.com"}}

def display_contacts():
    if not contact_dic:
        return "У вас поки що немає контактів."
    result = "Ваші контакти:\n"
    for name, details in contact_dic.items():
        result += f"Ім'я: {name}, Телефон: {details['Phone']}, Email: {details['Email']}\n"
    return result

def add_contact(name: str, phone: str, email: str):
    if not phone.startswith("+") or len(phone) != 13 or not phone[1:].isdigit():
        return "Номер телефону був введений невірно."

    if name in contact_dic:
        return "Цей користувач уже є в ваших контактах."

    contact_dic[name] = {"Phone": phone, "Email": email}
    return f"Контакт {name} успішно додано!"

def search_contact(name: str):
    if name in contact_dic:
        details = contact_dic[name]
        return f"Ім'я: {name}, Телефон: {details['Phone']}, Email: {details['Email']}"
    return "Контакт не знайдено."
