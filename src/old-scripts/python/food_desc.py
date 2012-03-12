# Defines Food object for describing various foods, e.g., chicken, broccoli, etc.

from rdf import RDFSerializable
from uri import NamespaceResolver

class Food(RDFSerializable):
    '''
    The Food class encapsulates the description of a food from the USDA's 
    database and stores it nutritional content per 100 g
    '''
    def __init__(self):
        RDFSerializable.__init__(self)
        self.id = ""
        self.food_group = None
        self.label = ""
        self.maker = ""
        self.percentRefuse = ""
        self.nfactor = ""
        self.profactor = ""
        self.fatfactor = ""
        self.chofactor = ""
        self.nutrients = []

    def begin(self,file):
        file.write("<nndsr:FoodItem rdf:about=\""+self.getID()+"\">\n");

    def serialize(self, file):
        '''
Food.serialize(file,indent):
    Serializes this food into RDF/XML specified by file
'''
        file.write("<rdf:type rdf:resource=\""+self.food_group.getID()+"\"/>")
        RDFSerializable.serialize(self, file)
        file.write("<nndsr:hasPercentRefuse rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.percentRefuse+"</nndsr:hasPercentRefuse>")
        file.write("<nndsr:hasNitrogenFactor rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.nfactor+"</nndsr:hasNitrogenFactor>")
        file.write("<nndsr:hasProteinFactor rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.percentRefuse+"</nndsr:hasProteinFactor>")
        file.write("<nndsr:hasFatFactor rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.percentRefuse+"</nndsr:hasFatFactor>")
        file.write("<nndsr:hasCarbohydrateFactor rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.percentRefuse+"</nndsr:hasCarbohydrateFactor>")
        if self.maker != "":
            file.write("<foaf:maker rdf:resource=\""+self.maker.getID()+"\"/>")
        for measure in self.nutrients:
            file.write("<sd:hasMeasurement>")
            file.visit(measure)
            file.write("</sd:hasMeasurement>")
    
    def end(self,file):
        file.write("</nndsr:FoodItem>")
        
    def getID(self):
        '''
Food.getID():
    Returns the URI that identifies this Food resource.
'''
        return NamespaceResolver.defaultNamespace+"food/"+str(self.id)

class Maker(RDFSerializable):
    def __init__(self, label):
        RDFSerializable.__init__(self)
        self.label = label
        
    def begin(self,file):
        file.write("<foaf:Organization rdf:about=\""+self.getID()+"\">")
    
    def serialize(self,file):
        RDFSerializable.serialize(self, file)
    
    def end(self,file):
        file.write("</foaf:Organization>")
    
    def getID(self):
        return NamespaceResolver.defaultNamespace+self.label.replace(" ", "_").replace("/","-")

class FoodDescParser:
    '''
    The FoodDescParser class is responsible for parsing contents from the 
    USDA nutrient database into instances of the Food class so that they 
    can be serialized into RDF/XML.
    '''
    def __init__(self):
        self.results = {}
    
    def parseFile(self, file, foodGroups):
        '''
        Parses the database table for food descriptions
        and returns a dictionary of the rows.
        '''
        self.results = {}
        file = open(file,"r")
        try:
            for entry in file:
                entry = entry.strip()
                cols = entry.split("^")
                food = Food()
                food.id = cols[0].strip("~")
                food.food_group = foodGroups[cols[1].strip("~")]
                food.label = cols[2].strip("~")
                makerLabel = cols[6].strip("~")
                if self.results.has_key(makerLabel):
                    food.maker = self.results[makerLabel]
                else:
                    maker = Maker(makerLabel)
                    self.results[makerLabel] = maker
                    food.maker = maker
                food.percentRefuse = cols[8].strip("~")
                food.nfactor = cols[10].strip("~")
                food.profactor = cols[11].strip("~")
                food.fatfactor = cols[12].strip("~")
                food.chofactor = cols[13].strip("~")
                if food.percentRefuse == "" or food.percentRefuse is None: food.percentRefuse = "0"
                if food.nfactor == "" or food.nfactor is None: food.nfactor = "0"
                if food.profactor == "" or food.profactor is None: food.profactor = "0"
                if food.fatfactor == "" or food.fatfactor is None: food.fatfactor = "0"
                if food.chofactor == "" or food.chofactor is None: food.chofactor = "0"
                self.results[food.id] = food
        except:
            return None
        return self.results
