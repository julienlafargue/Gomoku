#!/bin/bash
clear ; make
if [ -d $1]; then
    x=$(find ./tests/)
else
    x=$(find $1)
fi
for name in $x; do
    if [ -d $name ] || [ "$name" = "./tests/blankPatter" ]; then
        continue
    fi
    echo $name
    ./pbrain-gomoku-ai < $name
    echo
done
