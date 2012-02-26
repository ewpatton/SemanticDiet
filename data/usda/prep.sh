#!/bin/bash

URL=`cat dataset.txt`
FILE=`cat dataset.txt | perl -ne 'if (m/(([^\/]+))$/) { print "$1"; }'`
NAME=`echo "$FILE" | cut -d. -f 1`
EXT=`echo "$FILE" | cut -d. -f 2`

# We can use $NAME as the directory name since USDA includes revision numbers in the
# filename. You could alternately use curl -I to obtain the Last-Modified date and
# manipulate it into the DD-MMM-YYYY format used in many csv2rdf examples.
echo "mkdir -p source/usda-gov/nutrient-database/version/$NAME/{source,manual}"
mkdir -p source/usda-gov/nutrient-database/version/$NAME/{source,manual} || exit -1

