import matplotlib.pyplot as plt
import random

def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(("H", "T")) == "H":
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue

    plt.title("Difference between heads and tails")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of flips")
    plt.ylabel("Abs(#Heads - #Tails)")
    plt.plot(xAxis, diffs, "ko")
    plt.figure()
    plt.title("Heads/Tails Ratios")
    plt.xlabel("Number of Flips")
    plt.xscale("log")
    plt.ylabel("#Heads/#Tails")
    plt.plot(xAxis, ratios, "ko")

    plt.show()

random.seed(0)
flipPlot(4, 20)
