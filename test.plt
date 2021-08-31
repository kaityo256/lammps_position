set term pngcairo
set out "test.png"

set xlabel "Input"
set ylabel "Dump"

unset key
plot "test.dat" pt 6
