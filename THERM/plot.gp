#!/usr/bin/env bash


tmp=`echo $PWD`
STECH=${tmp##*/S}


echo -e "
name1=\"map.dat\"
name2=\"T_1000.dat\"

#plot name1 u 1:((\$3+\$5)/(\$3+\$5+\$7+\$9+\$11+\$13)) w p pt 7 ps 4 lc 1 t 'new',name2 u 8:((\$2+\$3)/(\$2+\$3+\$4+\$5+\$6+\$7)) w lp lc -1 pt 6 ps 4 t 'old'
#plot name1 u 15:((\$3+\$5)/(\$3+\$5+\$7+\$9+\$11+\$13)) w p pt 7 ps 4 lc 1 t 'new',name2 u 1:((\$2+\$3)/(\$2+\$3+\$4+\$5+\$6+\$7)) w lp lc -1 pt 6 ps 4 t 'old'
#v atoms
#plot name1 u 15:((\$3)/(\$3+\$7+\$11)) w p pt 7 ps 4 lc 1 t 'new',name2 u 1:((\$2)/(\$2+\$4+\$6)) w lp lc -1 pt 6 ps 4 t 'old'
#plot name1 u 15:((\$5)/(\$5+\$9+\$13)) w p pt 7 ps 4 lc 1 t 'new',name2 u 1:((\$3)/(\$3+\$5+\$7)) w lp lc -1 pt 6 ps 4 t 'old'
#ni atoms
#plot name1 u 15:((\$7)/(\$3+\$7+\$11)) w p pt 7 ps 4 lc 1 t 'new',name2 u 1:((\$4)/(\$2+\$4+\$6)) w lp lc -1 pt 6 ps 4 t 'old'
#plot name1 u 15:((\$9)/(\$5+\$9+\$13)) w p pt 7 ps 4 lc 1 t 'new',name2 u 1:((\$5)/(\$3+\$5+\$7)) w lp lc -1 pt 6 ps 4 t 'old'
#al atoms
#plot name1 u 15:((\$11)/(\$3+\$7+\$11)) w p pt 7 ps 4 lc 1 t 'new',name2 u 1:((\$6)/(\$2+\$4+\$6)) w lp lc -1 pt 6 ps 4 t 'old'
plot name1 u 15:((\$13)/(\$5+\$9+\$13)) w p pt 7 ps 4 lc 1 t 'new',name2 u 1:((\$7)/(\$3+\$5+\$7)) w lp lc -1 pt 6 ps 4 t 'old'


#plot 'up.dat' u 1:((\$7+\$9)/(\$3+\$5+\$7+\$9+\$11+\$13)) w lp,'down.dat' u 1:((\$11+\$13)/(\$3+\$5+\$7+\$9+\$11+\$13)) w lp
#plot 'up.dat' u 1:((\$9)/(\$3)) w lp t 'tdi'
#print $STECH
#plot 'up.dat' u 1:(\$15-$STECH) w lp t 'up','I.dat' u 1:3 w lp, 'II.dat' u 1:3 w lp
pause -1
" > to_plot

gnuplot to_plot