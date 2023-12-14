import random


# Функция для генерации математического примера
def generate_example():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    return a, b, operation

# Функция для проверки ответа пользователя
def check_answer(a, b, operation, user_answer):
    if operation == '+':
        correct_answer = a + b
    elif operation == '-':
        correct_answer = a - b
    elif operation == '*':
        correct_answer = a * b
    else:
        correct_answer = a / b
    return float(user_answer) == correct_answer

# Функция для самого теста и подведения итогов
def run_test():
    score = 0
    for _ in range(10):
        a, b, operation = generate_example()
        print(f" {a} {operation} {b}?")
        user_answer = input("Ваш ответ: ")
        if check_answer(a, b, operation, user_answer):
            print("")
            score += 1
        else:
            print("Неправильно")
    print(f"У вас получилось {score}/10 правильных ответов.")

run_test()
