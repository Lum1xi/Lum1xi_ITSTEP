from list_editor import *

while True:
    print('''
    1. Додати завдання
    2. Редагувати завдання
    3. Видалити завдання
    4. Переглянути всі завдання
    5. Вийти
    ''')
    choice = input('Введіть ваш вибір: ')
    if choice == '1':
        task = input('Введіть завдання: ')
        priority = input('Введіть пріоритет: ')
        status = input('Введіть статус: ')
        add_task(task, priority, status)
    elif choice == '2':
        print(view_all_tasks())
        print("")
        task_id = int(input('Введіть ID завдання: '))
        task = input('Введіть завдання: ')
        priority = input('Введіть пріоритет: ')
        status = input('Введіть статус: ')
        edit_task(task_id, task, priority, status)
    elif choice == '3':
        task_id = int(input('Введіть ID завдання: '))
        delete_task(task_id)
    elif choice == '4':
        print(view_all_tasks())
    elif choice == '5':
        break
    else:
        print('Невірний вибір')