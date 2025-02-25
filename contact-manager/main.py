from contact import *


def main():
    while True:
        print("1. Додавання нових контактів: \n2. Знайти контакт: \n3. Список контактів")
        choise = input("Що робимо: ")
        if choise == "1":
            print(add_contact(input("\nВведіть імя"), input("Введыть номер телефону"), input("Введіть email")))
        elif choise == "2":
            print(search_contact(input("\nВведіть імя")))

        elif choise == "3":
            print(display_contacts())
main()