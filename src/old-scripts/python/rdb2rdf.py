import sys
from food_group import FoodGroupParser
from nutrients import NutrientParser
from food_desc import FoodDescParser
from measures import MeasurementParser
from weight import WeightParser
from rdf import RDFSerializer
from pml import PML

options = PML.SourceOptions()
options.setMode(PML.SourceMode.DATASET)
options.setAccessDate("2010-06-06T23:37:00-04:00")
options.setName("USDA National Nutrient Database for Standard Reference, Release 22")
options.setDescription("""
U.S. Department of Agriculture, Agricultural Research Service. 2009. USDA National Nutrient Database for Standard Reference, Release 22. Nutrient Data Laboratory Home Page, <a href="http://www.ars.usda.gov/ba/bhnrc/ndl">http://www.ars.usda.gov/ba/bhnrc/ndl</a>
""")
options.setURI("http://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR22/dnload/sr22.ZIP")
options.addRelatedURL("http://www.ars.usda.gov/ba/bhnrc/ndl")

if len(sys.argv)!=6:
    print "Usage: python "+sys.argv[0]+" <input-dir> <schema-file> <data-file> <measures-file>"
    sys.exit(-1)

dbPath = sys.argv[1]
if not dbPath.endswith("/"):
    dbPath = dbPath + "/"

# Parse food group descriptions
print "Parsing food groups"
parser = FoodGroupParser()
tableFoodGroups = parser.parseFile(dbPath+"FD_GROUP.txt")
if tableFoodGroups is None:
    print "Unable to parse food groups table. Aborting..."
    sys.exit(-2)

# Parse nutrient descriptions
print "Parsing nutrient descriptions"
parser = NutrientParser()
tableNutrientDesc = parser.parseFile(dbPath+"NUTR_DEF.txt")
if tableNutrientDesc is None:
    print "Unable to parse nutrient definition table. Aborting..."
    sys.exit(-3)

# Parse food descriptions
print "Parsing food descriptions"
parser = FoodDescParser()
tableFoodDesc = parser.parseFile(dbPath+"FOOD_DES.txt", tableFoodGroups)
if tableFoodDesc is None:
    print "Unable to parse food definition table. Aborting..."
    sys.exit(-4)
    
# Parse measurements
print "Parsing nutrient data"
parser = MeasurementParser()
tableFoodDesc = parser.parseFile(dbPath+"NUT_DATA.txt", tableFoodDesc, tableNutrientDesc)
if tableFoodDesc is None:
    print "Unable to parse nutrient data table. Aborting..."
    sys.exit(-5)

print "Parsing food weights"
parser = WeightParser()
tableWeights = parser.parseFile(dbPath+"WEIGHT.txt", tableFoodDesc)
if tableWeights is None:
    print "Unable to parse weights table. Aborting..."
    sys.exit(-6)

print "Serializing data"
schema = RDFSerializer(sys.argv[2],"w+")
data = RDFSerializer(sys.argv[3],"w+")
nutrients = RDFSerializer(sys.argv[4],"w+")
weights = RDFSerializer (sys.argv[5],"w+")

schema.begin()
data.begin()
weights.begin()
nutrients.begin()

for k, v in tableFoodGroups.items():
    schema.visit(v)
for k, v in tableNutrientDesc.items():
    nutrients.visit(v)
for k, v in tableFoodDesc.items():
    data.visit(v)
for k, v in tableWeights.items():
    weights.visit(v)

schema.end()
data.end()
nutrients.end()
weights.end()
schema.close()
data.close()
weights.close()
nutrients.close()