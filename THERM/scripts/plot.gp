#!/usr/bin/env bash


echo -e "
plot 'F.dat' u (\$2/(1.0+\$2)):3 w lp t 'Fa', 'F.dat' u (\$2/(1.0+\$2)):4 w lp t 'Fb'
pause -1
" > to_plot

gnuplot to_plot