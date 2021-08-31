import numpy as np
import matplotlib.pyplot as plt


def readdump(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    readflag = False
    y = []
    for line in data:
        if "ATOMS id" in line:
            readflag = True
            continue
        if not readflag:
            continue
        a = line.split()
        y.append(float(a[2]))
    return y


dump = readdump("test.lammpstrj")
input = np.arange(-10, 20, 1)

for x, y in zip(input, dump):
    print(f"{x} {y}")
