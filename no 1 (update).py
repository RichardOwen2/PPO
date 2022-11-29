import math
import random

def fungsi(x):
    return (-4 * x) * (math.sin(x))


def findGBest(xn):
    sample = []
    index = 0
    while (index < len(xn)):
        sample.append(fungsi(xn[index]))
        index += 1

    return sample.index(min(sample))


def PSO(xn, v0, c1, c2, r1, r2, w, iterasi=1, pBest=None):
    if iterasi < 4:
        print("iterasi ke-", iterasi)

        index = 0
        while(index < len(xn)):
            print("x" + str(index) + " = ",end="")
            print(xn[index])
            index += 1

        gBest = xn[findGBest(xn)]
        print("gBest = ", gBest)

        if (pBest == None):
            pBest = xn
        else:
            index = 0
            while (index < len(xn)):
                if fungsi(pBest[index]) > fungsi(xn[index]):
                    pBest[index] = xn[index]
                index += 1

        V = []
        index = 0
        while (index < len(xn)):
            V.append(w*v0 + c1 * r1 * (pBest[index] - xn[index]) + c2 * r2 * (gBest - xn[index]))
            index += 1

        index = 0
        while (index < len(xn)):
            print("V"+ str(index) + " = ",end="")
            print(V[index])
            index += 1

        print()
        print("nilai minimum = ", fungsi(gBest))
        print()

        index = 0
        while (index < len(xn)):
            xn[index] = xn[index] + V[index]
            index += 1

        PSO(xn, v0, c1, c2, r1, r2,w, iterasi+1, pBest)


# PSO(0, math.pi/2, math.pi, 0, 1/2, 1, 1/2, 1/2, 1)

index = 0
data_xn = []
while (index < 10):
    data_xn.append(random.uniform(0, math.pi))
    index += 1

PSO(data_xn, random.uniform(0,1), 0, 1/2, 1, random.randint(0,1), random.randint(0,1), 1)