from units import Units
from rdf import RDFSerializable
from uri import NamespaceResolver

def capwords(str):
    o = str.split(" ")
    res = ""
    for s in o:
        res = res + s.capitalize()
    return res

def compressString(str):
    str = capwords(str)
    idx = str.find("(")
    if idx>=0:
        str = str[:idx]
    str = str.replace(",", "-")
    str = str.replace(":", "_")
    str = str.replace(" ", "")
    return str

class NutrientProperty:
    def __init__(self, nutrient=None):
#        RDFSerializable.__init__(self)
        self.nutrient = nutrient

    def getID(self):
        return NamespaceResolver.getURI("nndsr")+"has"+compressString(self.nutrient.label)

    def begin(self,file):
        file.write("<owl:ObjectProperty rdf:about=\""+self.getID()+"\">\n")

    def serialize(self, file):
        RDFSerializable.serialize(self,file)
        file.write("<rdfs:label xml:lang=\"en\">has "+self.nutrient.getLabel().lower()+"</rdfs:label>\n")
        file.write("<rdfs:subPropertyOf rdf:resource=\""+NamespaceResolver.getURI("sd")+"hasMeasurement\"/>\n")
        file.write("<rdfs:range>\n")
        file.indent()
        file.write("<owl:Class>\n")
        file.indent()
        file.write("<rdfs:subClassOf rdf:resource=\""+NamespaceResolver.getURI("nndsr")+"Measurement\"/>\n")
        file.write("<rdfs:subClassOf>\n")
        file.indent()
        file.write("<owl:Restriction>\n")
        file.indent()
        file.write("<owl:onProperty rdf:resource=\""+NamespaceResolver.getURI("nndsr")+"hasUnit\"/>\n")
        file.write("<owl:hasValue rdf:resource=\""+self.nutrient.getUnit().per100g()+"\"/>\n")
        file.unindent()
        file.write("</owl:Restriction>\n")
        file.unindent()
        file.write("</rdfs:subClassOf>\n")
        file.write("<rdfs:subClassOf>\n")
        file.indent()
        file.write("<owl:Restriction>\n")
        file.indent()
        file.write("<owl:onProperty rdf:resource=\""+NamespaceResolver.getURI("nndsr")+"measureOf\"/>\n")
        file.write("<owl:hasValue rdf:resource=\""+self.nutrient.getID()+"\"/>\n")
        file.unindent()
        file.write("</owl:Restriction>\n")
        file.unindent()
        file.write("</rdfs:subClassOf>\n")
        file.unindent()
        file.write("</owl:Class>\n")
        file.unindent()
        file.write("</rdfs:range>\n")
    
    def end(self,file):
        file.write("</owl:ObjectProperty>\n")


class Nutrient(RDFSerializable):
    def __init__(self, label="", unit=None, number=0):
        RDFSerializable.__init__(self)
        self.label = label
        self.unit = unit
        self.number = number
        if unit is not None:
            self.property = self.getProperty()
        else:
            self.property = None
    
    def begin(self,file):
        file.write("<nndsr:Nutrient rdf:about=\""+self.getID()+"\">")

    def serialize(self, file):
        RDFSerializable.serialize(self, file)
        file.write("<sd:measuredIn rdf:resource=\""+self.unit.per100g()+"\"/>")
    
    def end(self,file):
        file.write("</nndsr:Nutrient>")

    def getID(self):
        return NamespaceResolver.defaultNamespace+"nutrients/"+str(self.number)

    def getProperty(self):
        prop = NutrientProperty(self)
        return prop

    def getLabel(self):
        return self.label

    def getUnit(self):
        return self.unit

class NutrientParser:
    def __init__(self):
        self.results = {}

    def parseFile(self, file):
        self.results = {}
        file = open(file,"r")
        try:
            for entry in file:
                entry = entry.strip()
                cols = entry.split("^")
                id = cols[0].strip("~")
                unit = cols[1].strip("~")
                unit = Units.getUnitForLabel(unit)
                label = cols[3].strip("~")
                val = Nutrient(label, unit, id)
                self.results[id] = val
        except:
            return None
        return self.results
