import random

def fungsi(xy):
    x = xy[0]
    y = xy[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def findGBest(xyn):
    sample = []
    index = 0
    while (index < len(xyn)):
        sample.append(fungsi(xyn[index]))
        index += 1

    return sample.index(min(sample))


def PSO(xyn, v0, c1, c2, r1, r2, w, iterasi=1, pBest=None):
    if iterasi < 4:
        print("iterasi ke-", iterasi)

        index = 0
        while(index < len(xyn)):
            print("xy" + str(index) + " = ",end="")
            print(xyn[index])
            index += 1

        gBest = xyn[findGBest(xyn)]
        print("gBest = ", gBest)

        if (pBest == None):
            pBest = xyn
        else:
            index = 0
            while (index < len(xyn)):
                if fungsi(pBest[index]) > fungsi(xyn[index]):
                    pBest[index] = xyn[index]
                index += 1

        V = []
        index = 0
        while (index < len(xyn)):
            V.append([w*v0[0] + c1 * r1 * (pBest[index][0] - xyn[index][0]) + c2 * r2 * (gBest[0] - xyn[index][0]), w*v0[1] + c1 * r1 * (pBest[index][1] - xyn[index][1]) + c2 * r2 * (gBest[1] - xyn[index][1])])
            index += 1

        index = 0
        while (index < len(xyn)):
            print("V"+ str(index) + " = ",end="")
            print(V[index])
            index += 1

        print()
        print("nilai minimum = ", fungsi(gBest))
        print()

        index = 0
        while (index < len(xyn)):
            xyn[index][0] = xyn[index][0] + V[index][0]
            xyn[index][1] = xyn[index][1] + V[index][1]
            index += 1

        PSO(xyn, v0, c1, c2, r1, r2,w, iterasi+1, pBest)


# PSO([[1, 1], [-1, -1], [2, 1]], [0, 0], 1, 0.5, 1, 1, 1)

index = 0
data_xyn = []
while (index < 10):
    data_xyn.append([random.randint(-5,5), random.randint(-5,5)])
    # data_xyn.append(random.uniform(-5,5), random.uniform(-5,5)])
    index += 1

PSO(data_xyn, [random.uniform(0,1),random.uniform(0,1)], 1, 1/2, random.uniform(0,1), random.uniform(0,1), 1)