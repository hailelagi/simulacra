import random


def experiment(trials):
    single = 0
    for n in range(trials):
        x = random.choice((1, 2, 3, 4)) # P(1/4)
        y = random.choice((1, 2, 3, 4)) # P(1/4)

        # P(A + B) % 2 == 0
        if (x + y) % 2 == 0:
            single += 1
    # P(1/4 + 1/4 == even)

    return single/trials

print(experiment(1_000_000))
