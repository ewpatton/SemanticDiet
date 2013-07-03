#!/bin/bash
#
#3 <#> a <http://purl.org/twc/vocab/conversion/ConversionTrigger> ;
#3     rdfs:seeAlso <https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger>,
#3                  <https://github.com/timrdf/csv2rdf4lod-automation/blob/master/bin/cr-create-convert-sh.sh> .
#
# datasetID versionID (lastModDate):
# nutrient-database release-25 ()
#--------------------------------------------------------------

CSV2RDF4LOD_HOME=${CSV2RDF4LOD_HOME:?"not set; source csv2rdf4lod/source-me.sh or see https://github.com/timrdf/csv2rdf4lod-automation/wiki/CSV2RDF4LOD-not-set"}

# The identifiers used to name the dataset that will be converted.
#            (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-process-phase:-name)
surrogate="http://semanticdiet.com" # Came from $CSV2RDF4LOD_BASE_URI when cr-create-conversion-trigger.sh created this script.
sourceID="usgs-gov"               # Came from directory name ../../../ (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Directory-Conventions)
datasetID="nutrient-database"             # Came from directory name ../../ (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Directory-Conventions)
datasetVersion="release-25"        # DEPRECATED
versionID="release-25"             # Came from directory name ../ (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Directory-Conventions) renaming datasetVersion (deprecating datasetVersion)
eID="1"                             # enhancement identifier
if [[ ${1:-"."} == "-e" && $# -ge 2 ]]; then
   eID="$2" # see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Generating-enhancement-parameters
fi

if [ -d doc/logs ]; then
   dateInXSDDateTime.sh > doc/logs/conversion-trigger-last-pulled
fi

destDir="automatic"                 # convention has led to always be 'automatic'; the directory where the converted RDF is put.
#--------------------------------------------------------------


#-----------------------------------
# manual/DATA_SRC.txt.csv
sourceDir="manual"
datafile="DATA_SRC.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="data-src.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/DATSRCLN.txt.csv
sourceDir="manual"
datafile="DATSRCLN.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="datsrcln.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/DERIV_CD.txt.csv
sourceDir="manual"
datafile="DERIV_CD.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="deriv-cd.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/FD_GROUP.txt.csv
sourceDir="manual"
datafile="FD_GROUP.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="fd-group.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/FOOD_DES.txt.csv
sourceDir="manual"
datafile="FOOD_DES.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="food-des.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/FOOTNOTE.txt.csv
sourceDir="manual"
datafile="FOOTNOTE.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="footnote.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/LANGDESC.txt.csv
sourceDir="manual"
datafile="LANGDESC.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="langdesc.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/LANGUAL.txt.csv
sourceDir="manual"
datafile="LANGUAL.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="langual.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/NUTR_DEF.txt.csv
sourceDir="manual"
datafile="NUTR_DEF.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="nutr-def.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/NUT_DATA.txt.csv
sourceDir="manual"
datafile="NUT_DATA.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="nut-data.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/SRC_CD.txt.csv
sourceDir="manual"
datafile="SRC_CD.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="src-cd.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
# manual/WEIGHT.txt.csv
sourceDir="manual"
datafile="WEIGHT.txt.csv"
data="$sourceDir/$datafile"
# Bootstrap conversion parameters (see https://github.com/timrdf/csv2rdf4lod-automation/wiki/Conversion-trigger):
subjectDiscriminator="weight.txt"             # Additional part of URI for subjects created; must be URI-ready (e.g., no spaces).
commentCharacter=""                 # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
cellDelimiter=","                   # ONLY one character; complain to http://sourceforge.net/projects/javacsv/ otherwise.
header=                             # Line that header is on; only needed if not '1'. '0' means no header.
dataStart=                          # Line that data starts; only needed if not immediately after header.
repeatAboveIfEmptyCol=              # 'Fill in' value from row above for this column.
onlyIfCol=                          # Do not process if value in this column is empty
interpretAsNull=                    # NO SPACES
dataEnd=                            # Line on which data stops; only needed if non-data bottom matter (legends, footnotes, etc).
source $CSV2RDF4LOD_HOME/bin/convert.sh


#-----------------------------------
source $CSV2RDF4LOD_HOME/bin/convert-aggregate.sh
# ^^ Note, this step can also be done manually using publish/bin/publish.sh
