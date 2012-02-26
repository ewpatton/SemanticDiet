#!/bin/bash

if [[ "$CSV2RDF4LOD_HOME" = "" ]]; then
    echo '$CSV2RDF4LOD_HOME is not set. Please source the csv2rdf environment before running this script.'
    exit -1
fi

export CSV2RDF4LOD_CONVERT_DATA_ROOT=`pwd`/source

source ./prep.sh || exit -1

SELF=`basename $0`
GITHASH=`git log -- $SELF | head -n 1 | cut -d' ' -f 2 | cut -b 33-40`
SCRIPT=`echo "$SELF" | sed 's/\./-/g'`

cd source/usda-gov/nutrient-database/version/$NAME/source
pcurl.sh "$URL" -n $NAME -e $EXT || exit -1
punzip.sh "$NAME.$EXT" || exit -1
FILES=`ls *.txt`
for FILE in $FILES
do
    sed 's/"/\"/g' < "$FILE" | sed 's/~/"/g' | sed 's/\^/,/g' | "../manual/$FILE"
    . justify.sh "$FILE" "../manual/$FILE" $SCRIPT-$GITHASH --history
done
