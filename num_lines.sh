#!/bin/bash

# go through each .py file and add the number of lines together and print the total

num_lines=0

files=$(ls *.py)

for file in $files
do
	num_lines=$((num_lines + $(wc -l $file | awk '{print $1}')))
done

echo "Total number of lines: $num_lines"
