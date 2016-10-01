#!/usr/bin/bash

lista=`ls zstech*`

echo $lista

for i in $lista; do
pt1="."		#./data/$i"
#pt2="."	#/GEN_DOWN"	#/data/$i"

#echo $i
echo " 
files=\""$lista"\"
plot '$i' u 1:(\$5/(\$4+\$5)) w lp,'$i' u 1:(\$4/(\$4+\$5)) w lp,'$i' u 1:(\$3/(\$3+\$4+\$5)) w lp
#plot '$pt1/E.dat' u 1:3
#plot '$pt1/N.dat' u 1:((\$5+\$6)/(\$5+\$6+\$7+\$8)) #,'$pt2/N.dat' u 1:((\$5+\$6)/(\$7+\$8))
#plot '$pt1/N.dat' u 1:((\$3+\$4)/(\$3+\$4+\$5+\$6+\$7+\$8)),'$pt2/N.dat' u 1:((\$3+\$4)/(\$3+\$4+\$5+\$6+\$7+\$8))
#plot for [ name in files ] name u 1:(\$4/(\$4+\$5)) w lp 
#plot for [ name in files ] name u 1:(\$5/(\$4+\$5)) w lp

#name u 1:(\$3/(\$3+\$4+\$5)) w lp

pause -1

" > to_plot

gnuplot to_plot

done
