'''
Created on Sep 12, 2010

@author: ewpatton
'''

class NamespaceResolver:
    '''
    Stores namespaces
    '''
    
    __namespaces = {"rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                    "rdfs":"http://www.w3.org/2000/01/rdf-schema#",
                    "owl":"http://www.w3.org/2002/07/owl#",
                    "xsd":"http://www.w3.org/2001/XMLSchema#",
                    "nndsr":"http://semanticdiet.com/schema/usda/nndsr/",
                    "nndsr22":"http://semanticdiet.com/data/usda/nndsr/22/",
                    "nndsr23":"http://semanticdiet.com/data/usda/nndsr/23/",
                    "pmlp":"http://inferenceweb.stanford.edu/2006/06/pml-provenance.owl#",
                    "pmlj":"http://inferenceweb.stanford.edu/2006/06/pml-justification.owl#",
                    "sd":"http://semanticdiet.com/schema/",
                    "units":"http://sweet.jpl.nasa.gov/2.0/sciUnits.owl#",
                    "oper2":"http://sweet.jpl.nava.gov/2.0/mathOperation.owl#",
                    "foaf":"http://xmlns.com/foaf/0.1/"
                    }
    
    __labels = {"rdf":"Resource Description Framework",
                "rdfs":"RDF Schema",
                "owl":"Web Ontology Language",
                "xsd":"XML Schema Datatypes",
                "nndsr":"USDA National Nutrient Database for Standard Reference",
                "nndsr22":"USDA National Nutrient Database for Standard Reference, release 22",
                "nndsr23":"USDA National Nutrient Database for Standard Reference, release 23",
                "pmlp":"Proof Markup Language for Provenance",
                "pmlj":"Proof Markup Language for Justification",
                "sd":"SemanticDiet Ontology",
                "units":"SWEET Ontology, Scientific Units module",
                "oper2":"SWEET Ontology, Mathematical Operations module",
                "foaf":"Friend-of-a-Friend Ontology"
                }

    @staticmethod
    def getURI(namespace):
        return NamespaceResolver.__namespaces[namespace]
    
    @staticmethod
    def getLabel(namespace):
        return NamespaceResolver.__labels[namespace]

    @staticmethod
    def addNamespace(prefix, uri, label=""):
        if not NamespaceResolver.__namespaces.has_key(prefix):
            NamespaceResolver.__namespaces[prefix] = uri
            NamespaceResolver.__labels[prefix] = label
    
    @staticmethod
    def getNamespaces():
        return NamespaceResolver.__namespaces.items()

    defaultNamespace = "http://semanticdiet.com/data/usda/nndsr/23/"