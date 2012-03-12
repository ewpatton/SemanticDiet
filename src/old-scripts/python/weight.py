from rdf import RDFSerializable
from uri import NamespaceResolver

def escape(str):
    return str.replace(" ","_").replace("/","|").replace("\"", "in.")

class Weight(RDFSerializable):
    def __init__(self):
        RDFSerializable.__init__(self)
        self.label = ""
        self.food = None
        self.amount = ""
        self.grams = ""
        self.order = ""
        self.addType(NamespaceResolver.getURI("units")+"UnitDerivedByScaling")

    def getID(self):
        return NamespaceResolver.defaultNamespace+"common-measures/"+self.food.id+"-"+self.order
    
    def begin(self,file):
        file.write("<nndsr:CommonMeasure rdf:about=\""+self.getID()+"\">")
    
    def serialize(self,file):
        RDFSerializable.serialize(self,file)
        file.write("<units:derivedFromUnit rdf:resource=\""+NamespaceResolver.getURI("units")+"gram\"/>")
        file.write("<units:hasPrefix rdf:parseType=\"Resource\">")
        file.indent()
        file.write("<units:hasValue rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.grams+"</units:hasValue>")
        file.write("<rdf:type rdf:resource=\""+NamespaceResolver.getURI("units")+"Prefix\"/>")
        file.unindent()
        file.write("</units:hasPrefix>")
        file.write("<nndsr:measureOf rdf:resource=\""+self.food.getID()+"\"/>")
        file.write("<nndsr:multiplier rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.amount+"</nndsr:multiplier>")
    
    def end(self,file):
        file.write("</nndsr:CommonMeasure>")
        
class WeightParser:
    def __init__(self):
        self.results = {}
    
    def parseFile(self, file, foods):
        self.results = {}
        file = open(file, "r")
#        try:
        for entry in file:
            entry = entry.strip()
            cols = entry.split("^")
            obj = Weight()
            obj.food = foods[cols[0].strip("~")]
            obj.order = cols[1].strip("~")
            obj.amount = cols[2].strip("~")
            obj.label = cols[3].strip("~")
            obj.grams = cols[4].strip("~")
            self.results[obj.getID()] = obj
#        except:
#            return None
        return self.results