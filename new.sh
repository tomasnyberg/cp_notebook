#!/bin/bash
#Command to create a new python file with baseline for being able to read the lines
# Usage: new <filename> to create a baseline file with name filename.py
# If you add the -t flag it will add the stuff needed to do deep recursion (some threading magic)

first=$1
second=$2

#Check if first is -t
if [ $first = "-t" ]
then
    #Check if second is empty
    if [ -z $second ]
    then
        echo "Please enter a filename"
        exit 1
    else
        #Create file
        touch $second.py
        #Create file with baseline
        echo "import sys, threading" >> $second.py
        echo "lines = list(map(str.strip, sys.stdin.readlines()))" >> $second.py
        echo "sys.setrecursionlimit(10**9)" >> $second.py 
        echo "threading.stack_size(10**8)" >> $second.py
        echo " " >> $second.py
        echo "def solve():" >> $second.py
        echo "    pass" >> $second.py
        echo "threading.Thread(target=solve).start()" >> $second.py
        exit 0
    fi
else
    #Create file
    touch $first.py
    #Create file with baseline
    echo "import sys" >> $first.py
    echo "if sys.argv[-1] == '--debug':" >> $first.py
    echo "   sys.stdin = open('in')" >> $first.py
    echo "lines = list(map(str.strip, sys.stdin.readlines()))" >> $first.py
    echo "# TODO Remember to add int wrapping if using dict" >> $first.py
    exit 0
fi
if [ -e $1 ]; then
  echo "File $1 already exists!"
else

