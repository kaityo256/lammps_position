import numpy as np
import matplotlib.pyplot as plt


def readdump(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    readflag = False
    x = []
    index = []
    for i, line in enumerate(data):
        if "ATOMS id" in line:
            readflag = True
            continue
        if "ITEM: BOX BOUNDS" in line:
            xlo, xhi = data[i+1].split()
            xlo = float(xlo)
            xhi = float(xhi)
            continue
        if not readflag:
            continue
        a = line.split()
        x.append(float(a[2]))
        index.append(int(a[0])-1)
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[index[i]] = x[i]
    return y, xlo, xhi


dump, xlo, xhi = readdump("test.lammpstrj")
input = np.arange(xlo, xhi, 1)

for x, y in zip(input, dump):
    print(f"{x} {y}")
