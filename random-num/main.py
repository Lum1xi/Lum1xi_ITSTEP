import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 10 # Кількість спроб

    print("Ласкаво просимо до гри \"Вгадай число\"!")
    print("Я загадав число від 1 до 100.")
    print(f"У вас є {attempts} спроб, щоб його відгадати.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Спроба {attempt}: Введіть ваше число: "))

        if guess < number_to_guess:
            print("Більше!")
        elif guess > number_to_guess:
            print("Менше!")
        else:
            print(f"Вітаю! Ви вгадали число {number_to_guess} за {attempt} спроб.")
            break
    else:
        print(f"На жаль, ви використали всі спроби. Загадане число було {number_to_guess}.")

guess_the_number()
