#!/bin/bash
#Command to create a new python file with baseline for being able to read the lines
# Usage: new <filename>
if [ -e $1 ]; then
  echo "File $1 already exists!"
else
  echo "import sys
lines = list(map(str.strip, sys.stdin.readlines()))">> $1
fi