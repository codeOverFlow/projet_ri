#!/bin/bash

mkdir clean_test
mkdir clean_test/$1
rm -fr clean_test/*/clean_*

for f in `ls test/$1`
do
   touch clean_test/${1}/${f}
   ./clean.py test/${1}/${f} > clean_test/${1}/${f}
done
