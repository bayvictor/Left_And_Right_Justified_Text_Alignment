#!/bin/bash -x 
#timestamp
date +%F-%T | sed -e 's|\:|-|g' | sed -e 's|\/|-|g'


#python3 left_and_right_justified.py test.txt 20 "\(\W\)+"  > debug.sh.log.txt 2>&1 

#time python3 left_and_right_justified.py test.txt 20   "\x28W+\x29\\-"  

time python3 left_and_right_justified.py test.txt 40   "\x28W+\x29\\-"  > debug.sh.log.txt 2>&1 
#timestamp
date +%F-%T | sed -e 's|\:|-|g' | sed -e 's|\/|-|g'

vim debug.sh.log.txt


