# Left_And_Right_Justified_Text_Alignment,    ## <br> ##change edit-mode by click "raw" button, then it can be copy-pate into your linux terminal to run!  
#Victor's Text Alignment for both left and right justification  for Any Western languages 
# quick hack:
#!/bin/bash -x 
# step 1. 
git clone https://github.com/bayvictor/Left_And_Right_Justified_Text_Alignment.git;
cd Left*;
chmod +x *.sh; 
# step2. running without command line argument.
./noarg.sh;           ## script content: python3 left_and_right_justified.py >noarg.sh.log.txt 2>&1  ## <br> <br>
echo "above line testing for para=\"This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.\" case."   ##  <br> <br>
# step 3. read filename page_size, align to stdout. 
#step 3. running with command line argument, argv1=txt_filename, argv2=page_width ## <br> <br>  
echo "we are going to aligning from input file=\"test.txt\", with pagelen=arg3."  ##  <br> <br>
echo "control-c to break, any other key to continue aligning file."; read readline ## <br> <br>
./debug.sh;           ## script content : python3 left_and_right_justified.py test.txt 40   "\x28W+\x29\\-"  > debug.sh.log.txt 2>&1  ## <br> <br>

