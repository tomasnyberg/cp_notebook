#!/bin/bash
# Take 1 argument
if [ $# -ne 1 ]; then
  echo "Usage: cr <filename>, compiles and runs with "in" as input, removes afterwards"
  exit 1
fi
# compile the file with the name given with g++
g++ -O1 $1 && ./a.out < in && rm a.out