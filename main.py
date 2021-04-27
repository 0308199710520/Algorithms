from random import randint


def birthday_prob(n):
    birthdays = []
    for _ in range(n):
        birthdays.append(randint(0, 366))

    if len(birthdays) == len(set(birthdays)):
        return 0

    else:
        return 1


y = 1000000
prob_calc = 0
for _ in range(y):
    prob_calc += birthday_prob(23)

print((prob_calc / y) * 100)
