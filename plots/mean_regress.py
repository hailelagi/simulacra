import numpy as np
import matplotlib.pyplot as plt
import random

#######################
# stochastic programs #
#######################

# fair two-die simulation
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads/numFlips


# Regression to the mean
def regressToMean(numFlips, numTrials):
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))

    extremes, nextTrials = [], []

    for i in range(len(fracHeads) - 1):
        # if > 1/3 or > 2/3 then it diverges from the mean 0.5
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i + 1])

    plt.plot(range(len(extremes)), extremes, 'ko', label="Extreme")
    plt.plot(range(len(nextTrials)), nextTrials, "k^", label="Next Trial")
    plt.axhline(0.5)
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) + 1)
    plt.xlabel("Extreme Example and Next Trial")
    plt.ylabel("Fraction Heads")
    plt.title("Regression to the Mean")
    plt.legend(loc="best")

    plt.show()

regressToMean(15, 40)