#!/bin/bash -x 
#timestamp
date +%F-%T | sed -e 's|\:|-|g' | sed -e 's|\/|-|g'
if  test -z "$2" ; then
        echo "missing txt_filename page_size "
        echo "usage: $0 <fn> <page_zie> "
        echo "e.g.:  $0 test2.txt  40"
        exit 1  
fi

time python3 left_and_right_justified.py $1 $2   "\x28W+\x29\\-"  > $0.$1.$2.log.txt 2>&1 

#timestamp
date +%F-%T | sed -e 's|\:|-|g' | sed -e 's|\/|-|g'

vim $0.$1.$2.log.txt 


