import numpy as np


class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0


def save_file(filename, atoms, lo, hi):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write(f"{lo} {hi} xlo xhi\n")
        f.write(f"{lo} {hi} ylo yhi\n")
        f.write(f"{lo} {hi} zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
    print("Generated {}".format(filename))


if __name__ == "__main__":
    lo = -10
    hi = 20
    atoms = []
    for x in np.arange(lo, hi, 1):
        atoms.append(Atom(x, 0, 0))
    save_file("test.atoms", atoms, lo, hi)
