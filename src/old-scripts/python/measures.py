'''
Created on Nov 30, 2010

@author: ewpatton
'''

from rdf import RDFSerializable
from uri import NamespaceResolver

class Measure(RDFSerializable):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        RDFSerializable.__init__(self)
        self.nutrient = None
        self.amount = 0
        
    def begin(self,file):
        file.write("<nndsr:Measurement>")
    
    def serialize(self, file):
        RDFSerializable.serialize(self, file)
        file.write("<nndsr:hasUnit rdf:resource=\""+self.nutrient.unit.per100g()+"\"/>")
        file.write("<nndsr:measureOf rdf:resource=\""+self.nutrient.getID()+"\"/>")
        file.write("<nndsr:measuredValue rdf:datatype=\""+NamespaceResolver.getURI("xsd")+"double\">"+self.amount+"</nndsr:measuredValue>")
    
    def end(self,file):
        file.write("</nndsr:Measurement>")
        
class MeasurementParser():
    def __init__(self):
        self.results = {}
    
    def parseFile(self,file,foods,nutrients):
        self.results = {}
        file = open(file,"r")
        
        for entry in file:
            entry = entry.strip()
            cols = entry.split("^")
            measure = Measure()
            foods[cols[0].strip("~")].nutrients.append(measure)
            measure.nutrient = nutrients[cols[1].strip("~")]
            measure.amount = cols[2].strip("~")
        return foods
