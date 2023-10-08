#!/bin/bash
#sizes=( 4096 32768 131072 1048576 2097152 4194304 8388608 16777216 33554432 134217728 67108864 1073741824)
sizes=( 65536 262144)
for size in "${sizes[@]}" ; do
    bash run_cacti_with_config.sh 4 $size
done