#! /bin/bash

#echo out1
#./run.py -f examples/hw2_a.ps -s 1.5 > out1.xpm
#echo out2
#./run.py -f examples/hw2_a.ps -m -250 -n -200 > out2.xpm
#echo out3
#./run.py -f examples/hw2_b.ps -a 170 -b 100 -c 270 -d 400 > out3.xpm
#echo out4
#./run.py -f examples/hw2_b.ps -s 2.0 > out4.xpm
#echo out5
#./run.py -f examples/hw2_c.ps -a 200 -b 100 -c 375 -d 400 > out5.xpm
#echo out6
#./run.py -f examples/hw2_c.ps -a 275 -b 100 -c 550 -d 502 > out6.xpm
#echo out7
#./run.py -f examples/hw2_b.ps -d 270 -c 435 -b 170 -a 100 -r 17 > out7.xpm
#echo out8
#./run.py -f examples/hw2_b.ps -a -135 -b -53 -c 633 -d 442 > out8.xpm
#echo out9
#./run.py -f examples/hw2_c.ps -a -150 -b -475 -c 123 -d -65 > out9.xpm

echo HW3
echo out31
./run.py -f examples/hw3_split.ps -a 0 -b 0 -c 500 -d 500 -j 0 -k 0 -o 500 -p 500 -s 1.0 -m 0 -n 0 -r 0 > out31.xpm

echo out32
./run.py -f examples/hw3_split.ps -a 50 -b 0 -c 325 -d 500 -j 0 -k 110 -o 480 -p 410 -s 1.0 -m 0 -n 0 -r 0 > out32.xpm

echo out33
./run.py -f examples/hw3_split.ps -a 10 -b 10 -c 550 -d 400 -j 10 -k 10 -o 500 -p 400 -s 1.2 -m 6 -n 25 -r 8 > out33.xpm

echo out34
./run.py -f examples/hw3_split.ps -a 0 -b 62 -c 500 -d 479 -j 139 -k 0 -o 404 -p 461 -s 0.85 -m 300 -n 0 -r 75 > out34.xpm

echo out35
./run.py -f examples/hw3_split.ps -a 275 -b 81 -c 550 -d 502 -j 123 -k 217 -o 373 -p 467 -r -37 > out35.xpm

echo out36
./run.py -f examples/hw3_split.ps -a -135 -b -53 -c 633 -d 842 -j 101 -p 415 -s 3.6 -m -23 -n 0 -r 0 > out36.xpm
