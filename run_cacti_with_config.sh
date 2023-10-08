#!/bin/bash

#Usage: run_cacti_with_config.sh 4 2048
associativity=$1
cache_sizes=$2
prefix="assoc_$1_size_$2"
filename="configs/cache_${prefix}.cfg"
logfilename="logs/log_${prefix}.txt"

cp "cache_test.cfg" "$filename"
echo "-size (bytes) $cache_sizes" >> "$filename"
echo "-associativity $associativity" >> "$filename"
./cacti -infile "$filename" >> $logfilename 2>&1
