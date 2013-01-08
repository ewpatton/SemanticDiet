#!/bin/bash
#
# This script copies files in source/ and stores their modified versions in manual/.
# This script also constructs the conversion trigger (e.g., with cr-create-conversion-trigger.sh -w manual/*.csv)
# When this file is in a cr:directory-of-versions, it is invoked by retrieve.sh.
#   The conversion cockpit as the current working directory when this script is invoked.
#
# See https://github.com/timrdf/csv2rdf4lod-automation/wiki/Automated-creation-of-a-new-Versioned-Dataset
#     https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger
#     https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-cockpit

#cat source/NUTR_DEF.txt | sed 's/^~/"/;  s/~\^~/","/g;  s/~.*$/"/g' > manual/NUTR_DEF.txt.csv
#cat source/WEIGHT.txt   | sed 's/~//g; s/^/"/; s/\^\^/^/g; s/\^/","/g; s/,"[^"]*$//' > manual/WEIGHT.txt.csv

for table in `find source -name "*.txt"`; do
   csv="manual/`basename $table`.csv"
   echo "$table -> $csv"
   cat $table | sed 's/"/\\"/g; s/~/"/g; s/\^/,/g' > $csv
   justify.sh $table $csv redelimit &> /dev/null
done

cr-create-conversion-trigger.sh -w manual/*.csv
