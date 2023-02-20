#!/bin/bash
# If we got no arguments, print usage and exit
if [ $# -eq 0 ]; then
  echo "Usage: cr.sh <file> [-noin]"
  exit 1
fi

# If the -noin flag is set, run without piping in the in file, else pipe it in
if [ "$2" = "-noin" ]; then
  g++ -O1 $1 && ./a.out && rm a.out
else
  g++ -O1 $1 && ./a.out < in && rm a.out
fi