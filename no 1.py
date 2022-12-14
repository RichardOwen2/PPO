import math
import random

def fungsi(x):
    return (-4 * x) * (math.sin(x))


def findGBest(x0, x1, x2):
    if (fungsi(x0) < fungsi(x1) and fungsi(x0) < fungsi(x2)):
        return x0
    elif (fungsi(x1) < fungsi(x0) and fungsi(x1) < fungsi(x2)):
        return x1
    elif (fungsi(x2) < fungsi(x0) and fungsi(x2) < fungsi(x1)):
        return x2


def PSO(x0, x1, x2, v0, c1, c2, r1, r2, w, iterasi=1, pBest0=None, pBest1=None, pBest2=None):
    if iterasi < 4:
        print("iterasi ke-", iterasi)
        print("x0 = ", x0)
        print("x1 = ", x1)
        print("x2 = ", x2)

        gBest = findGBest(x0, x1, x2)

        print("gBest = ", gBest)
        print()

        if (pBest0 == None and pBest1 == None and pBest2 == None):
            pBest0 = x0
            pBest1 = x1
            pBest2 = x2
        else:
            if fungsi(pBest0) > fungsi(x0):
                pBest0 = x0
            if fungsi(pBest1) > fungsi(x1):
                pBest1 = x1
            if fungsi(pBest2) > fungsi(x2):
                pBest2 = x2

        V0 = w*v0 + c1 * r1 * (pBest0 - x0) + c2 * r2 * (gBest - x0)
        V1 = w*v0 + c1 * r1 * (pBest1 - x1) + c2 * r2 * (gBest - x1)
        V2 = w*v0 + c1 * r1 * (pBest2 - x2) + c2 * r2 * (gBest - x2)

        print("V0 = ", V0)
        print("V1 = ", V1)
        print("V2 = ", V2)
        print()
        print("nilai minimum = ", fungsi(gBest))
        print()

        x0 = x0 + V0
        x1 = x1 + V1
        x2 = x2 + V2

        PSO(x0, x1, x2, v0, c1, c2, r1, r2, w, iterasi+1, pBest0, pBest1, pBest2)


PSO(0, math.pi/2, math.pi, 0, 1/2, 1, 1/2, 1/2, 1)
# PSO(random.uniform(0, math.pi), random.uniform(0, math.pi), random.uniform(0, math.pi), 0, 1/2, 1, random.randint(0,1), random.randint(0,1), 1)
