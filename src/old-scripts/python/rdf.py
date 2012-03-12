from uri import NamespaceResolver

class RDFSerializable:
    
    def __init__(self):
        self.serialized = False
        self.label = None
        self.comment = None
        self.related = []
        self.types = set()
    
    def begin(self,file):
        file.write("<rdf:Description>")
        return None
    
    def serialize(self,file):
        self.serialized = True
        self.placeTypes(file)
        self.placeRelatedURIs(file)
        self.placeLabel(file)
        return None
    
    def end(self,file):
        file.write("</rdf:Description>")
        return None
    
    def placeLabel(self,file):
        if self.label is not None:
            file.write("<rdfs:label xml:lang=\"en\">"+self.label.replace("&","&amp;").replace("<","&lt;")+"</rdfs:label>")
        if self.comment is not None:
            file.write("<rdfs:comment xml:lang=\"en\">"+self.comment.replace("&","&amp;").replace("<","&lt;")+"</rdfs:comment>")
            
    def placeRelatedURIs(self,file):
        if self.related and len(self.related) > 0:
            for uri in self.related:
                file.write("<rdfs:seeAlso rdf:resource=\""+uri+"\"/>")
    
    def placeTypes(self,file):
        if self.types and len(self.types) > 0:
            for uri in self.types:
                file.write("<rdf:type rdf:resource=\""+uri+"\"/>")
    
    def setLabel(self,label):
        self.label = label
    
    def getLabel(self):
        return self.label
    
    def addRelatedURI(self,uri):
        self.related.append(uri)
    
    def clearRelatedURIs(self):
        self.related = []
    
    def getRelatedURIs(self):
        return self.related

    def removeRelatedURI(self,uri):
        self.related.remove(uri)
    
    def addType(self,uri):
        self.types.add(uri)
    
    def removeType(self,uri):
        self.types.remove(uri)
    
    def clearTypes(self):
        self.types = set()

class RDFSerializer(file):
    def __init__(self, *args, **kwargs):
        file.__init__(self, *args, **kwargs)
        self.__encoding = "UTF-8"
        self.__indent = 0
        self.__bnode = 0
        self.__deferred = {}

    def begin(self):
        global NamespaceResolver
        self.write("<?xml version=\"1.0\" encoding=\""+self.__encoding+"\"?>\n")
        self.write("<rdf:RDF")
        for k,v in NamespaceResolver.getNamespaces():
            self.write(" xmlns:"+k+"=\""+v+"\"")
        self.write(">\n")
        self.__indent += 2
        return self.__indent

    def end(self):
        self.unindent()
        self.write("</rdf:RDF>\n")

    def getIndent(self):
        return self.__indent
    
    def indent(self):
        self.__indent += 2
        return self.__indent
    
    def unindent(self):
        self.__indent -= 2
        if self.__indent < 0:
            self.__indent = 0
        return self.__indent
    
    def visit(self,node):
        node.begin(self)
        self.indent()
        node.serialize(self)
        self.unindent()
        node.end(self)
        
    def write(self, text):
        return file.write(self," "*self.__indent+text+"\n")
    
    def nextBlankNode(self):
        node = "A"+self.__bnode
        self.__bnode += 1
        return node
    
    def deferRendering(self,object):
        self.__deferred[object.identifier] = object
