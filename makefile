all: run


run:
	python3 generate_config.py
	lmp_serial < test.input
	python3 check.py > test.dat
	gnuplot test.plt


clean:
	rm -f test.atoms test.lammpstrj log.lammps test.dat

