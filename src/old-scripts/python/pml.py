'''
Created on Aug 26, 2010

@author: ewpatton
'''

from rdf import RDFSerializable

class Information(RDFSerializable):
    
    def __init__(self):
        self.content = None
        self.source = None

class RDFInformation(Information):
    
    def __init__(self, subject = None, predicate = None, object = None):
        Information.__init__(self)
        self.subject = subject
        self.predicate = predicate
        self.object = object

class SourceUsage(RDFSerializable):
    
    def __init__(self):
        self.source = None
        self.accessDate = None

class Source(RDFSerializable):
    
    DATASET, DOCUMENT_FRAGMENT_OFFSET, DOCUMENT_FRAGMENT_ROWCOL, ONTOLOGY, PUBLICATION, WEBSITE, CUSTOM, UNKNOWN = range(8)
    
    def __init__(self,uri = None):
        self.type = Source.UNKNOWN
        self.customType = None
        self.identifier = uri
        
    def serialize(self,file):
        RDFSerializable.serialize(self, file)

class Document(Source):
    
    def __init__(self,uri = None):
        Source.__init__(self, uri)
        self.abstract = None
        self.version = None
        self.publisher = None
        self.citation = None
        self.content = []
        
    def setVersion(self,version):
        self.version = version
    
    def getVersion(self):
        return self.version
    
    def setAbstract(self,abstract):
        self.abstract = abstract
    
    def getAbstract(self):
        return self.abstract
    
    def setPublisher(self,publisher):
        self.publisher = publisher
    
    def getPublisher(self):
        return self.publisher
    
    def begin(self,file):
        if self.identifier is None:
            self.identifier = file.nextBlankNode()
        file.write("<pmlp:Document rdf:about=\""+self.identifier+"\">")
        
    def serialize(self,file):
        Source.serialize(self,file)
    
    def end(self,file):
        file.write("</pmlp:Document>")

class Publication(Document):
    
    def __init__(self,uri = None):
        Document.__init__(self, uri)
        self.type = Source.PUBLICATION
        self.publicationDate = None
        self.isbn = None

class Dataset(Document):
    
    def __init__(self,uri = None):
        Document.__init__(self, uri)
        self.type = Source.DATASET

class Ontology(Document):
    
    def __init__(self,uri = None):
        Document.__init__(self, uri)
        self.type = Source.ONTOLOGY

class Website(Document):
    
    def __init__(self,uri = None):
        Document.__init__(self, uri)
        self.type = Source.WEBSITE
        
class DocumentFragment(Source):
    
    def __init__(self,uri = None):
        Source.__init__(self, uri)
        self.document = None

class DocumentFragmentByOffset(DocumentFragment):
    
    def __init__(self,uri = None):
        DocumentFragment.__init__(self, uri)
        self.type = Source.DOCUMENT_FRAGMENT_OFFSET
        self.fromOffset = None
        self.toOffset = None

class DocumentFragmentByRowCol(DocumentFragment):
    
    def __init__(self,uri = None):
        DocumentFragment.__init__(self, uri)
        self.type = Source.DOCUMENT_FRAGMENT_ROWCOL
        self.fromRow = None
        self.toRow = None
        self.fromCol = None
        self.toCol = None

class PML:
    
    class SourceMode:
        DATASET, DOCUMENT_FRAGMENT_OFFSET, DOCUMENT_FRAGMENT_ROW, ONTOLOGY, PUBLICATION, WEBSITE, CUSTOM, UNKNOWN = range(8)
    
    class SourceOptions:
        def __init__(self):
            self.__mode = PML.SourceMode.UNKNOWN
            self.__customMode = None
            self.__uri = None
            self.__fragmentRange = None
            self.__accessDate = None
            self.__name = None
            self.__citation = None
            self.__related = []
            self.__version = None
        
        def setMode(self,mode,prefix = None,qname = None):
            self.__mode = mode
            if not prefix is None and not qname is None:
                self.__customMode = {"prefix": prefix, "qname": qname}
        
        def getMode(self):
            return self.__mode
        
        def getCustomMode(self):
            return self.__customMode
        
        def setURI(self,uri):
            self.__uri = uri
        
        def getURI(self):
            return self.__uri
        
        def clearRange(self):
            self.__fragmentRange = None
        
        def setRowRange(self,start,end):
            if self.__fragmentRange is None:
                self.__fragmentRange = {}
            self.__fragmentRange['fromRow'] = start
            self.__fragmentRange['toRow'] = end
        
        def setColRange(self,start,end):
            if self.__fragmentRange is None:
                self.__fragmentRange = {}
            self.__fragmentRange['fromCol'] = start
            self.__fragmentRange['toCol'] = end
        
        def getFragment(self):
            return self.__fragmentRange
        
        def setAccessDate(self,date):
            self.__accessDate = date
        
        def getAccessDate(self):
            return self.__accessDate
        
        def setName(self,name):
            self.__name = name
        
        def getName(self):
            return self.__name
        
        def setDescription(self,desc):
            self.__citation = desc
        
        def getDescription(self):
            return self.__citation
        
        def addRelatedURL(self,url):
            self.__related.append(url)
        
        def removeRelatedURL(self,url):
            self.__related.remove(url)
        
        def clearRelatedURLs(self):
            self.__related = []
        
        def setVersion(self,version):
            self.__version = version
        
        def getVersion(self):
            return self.__version

    def __init__(self,options):
        '''
        Initializes the PML helper by specifying information regarding the
        source document that is to be used as the citation for all triples
        published by this PML Helper.
        '''
        self.dataMode = options.mode
        self