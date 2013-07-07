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
    if [ `basename $table` = "DATA_SRC.txt" ]; then
	csvD="manual/`basename $table`_D.csv"
	csvS="manual/`basename $table`_S.csv"
	echo "$table -> $csvD + $csvS"
	cat $table | egrep '^~D' | sed 's/"/\\"/g; s/~/"/g; s/\^/,/g' > $csvD
	justify.sh $table $csvD redelimit &> /dev/null
	cat $table | egrep '^~S' | sed 's/"/\\"/g; s/~/"/g; s/\^/,/g' > $csvS
	justify.sh $table $csvS redelimit &> /dev/null
    else
	csv="manual/`basename $table`.csv"
	echo "$table -> $csv"
	cat $table | sed 's/"/\\"/g; s/~/"/g; s/\^/,/g; s/µ/Î¼/g' > $csv
	justify.sh $table $csv redelimit &> /dev/null
    fi
done

cr-create-conversion-trigger.sh -w manual/DATA_SRC.txt_D.csv manual/DATA_SRC.txt_S.csv manual/SRC_CD.txt.csv manual/DERIV_CD.txt.csv manual/NUTR_DEF.txt.csv
