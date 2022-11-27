def fungsi(xy):
    x = xy[0]
    y = xy[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def findGBest(xy0, xy1, xy2):
    if (fungsi(xy0) < fungsi(xy1) and fungsi(xy0) < fungsi(xy2)):
        return xy0
    elif (fungsi(xy1) < fungsi(xy0) and fungsi(xy1) < fungsi(xy2)):
        return xy1
    elif (fungsi(xy2) < fungsi(xy0) and fungsi(xy2) < fungsi(xy1)):
        return xy2


def PSO(xy0, xy1, xy2, v0, c1, c2, r1, r2, w, iterasi=1, pBest0=None, pBest1=None, pBest2=None):
    print("iterasi ke-", iterasi)
    print("x0y0 = ", xy0)
    print("x1y1 = ", xy1)
    print("x2y2 = ", xy2)

    gBest = findGBest(xy0, xy1, xy2)

    print("nilai minimum = ", gBest)
    print()

    if iterasi < 3:
        turunan_xy0 = fungsi(xy0)
        turunan_xy1 = fungsi(xy1)
        turunan_xy2 = fungsi(xy2)

        if (pBest0 == None and pBest1 == None and pBest2 == None):
            pBest0 = xy0
            pBest1 = xy1
            pBest2 = xy2
        else:
            if fungsi(pBest0) > turunan_xy0:
                pBest0 = xy0
            if fungsi(pBest1) > turunan_xy1:
                pBest1 = xy1
            if fungsi(pBest2) > turunan_xy2:
                pBest2 = xy2

        V0 = [w*v0[0] + c1 * r1 * (pBest0[0] - xy0[0]) + c2 * r2 * (gBest[0] - xy0[0]), w*v0[1] + c1 * r1 * (pBest0[1] - xy0[1]) + c2 * r2 * (gBest[1] - xy0[1])]
        V1 = [w*v0[0] + c1 * r1 * (pBest1[0] - xy1[0]) + c2 * r2 * (gBest[0] - xy1[0]), w*v0[1] + c1 * r1 * (pBest1[1] - xy1[1]) + c2 * r2 * (gBest[1] - xy1[1])]
        V2 = [w*v0[0] + c1 * r1 * (pBest2[0] - xy2[0]) + c2 * r2 * (gBest[0] - xy2[0]), w*v0[1] + c1 * r1 * (pBest2[1] - xy2[1]) + c2 * r2 * (gBest[1] - xy2[1])]

        xy0 = [xy0[0] + V0[0], xy0[1] + V0[1]]
        xy1 = [xy1[0] + V1[0], xy1[1] + V1[1]]
        xy2 = [xy2[0] + V2[0], xy2[1] + V2[1]]

        PSO(xy0, xy1, xy2, v0, c1, c2, r1, r2,w, iterasi+1, pBest0, pBest1, pBest2)


PSO([1, 1], [-1, -1], [2, 1], [0, 0], 1, 1/2, 1, 1, 1)
