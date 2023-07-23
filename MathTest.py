import random

first_factor = int(random.random() * 10)
second_factor = int(random.randint(10, 99))
print(f"Enter answer: {first_factor} * {second_factor} = ", end="")
cp_sum = first_factor * second_factor
i = 0
correct_answer = False

while i < 3:
    input_sum = int(input())
    if input_sum != cp_sum:
        print("Your answer is wrong. Try again.")
        i += 1
    else:
        print("Your answer is right.")
        correct_answer = True
        break

if not correct_answer:
    print("You made too many mistakes.")

