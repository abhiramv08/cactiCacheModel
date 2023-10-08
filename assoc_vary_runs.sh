#!/bin/bash
assocs=( 0 1 2 4 8 16 32 64)
for assoc in "${assocs[@]}" ; do
    bash run_cacti_with_config.sh $assoc 524288
done