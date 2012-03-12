#!/usr/bin/python
# -*- coding: utf-8; -*-

from uri import NamespaceResolver

class Gram:
    label=["g"]

    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"gram"

    @classmethod
    def per100g(self):
        return NamespaceResolver.getURI("sd")+"gram_per100g"

    @classmethod
    def create(self):
        return Gram()

class CentaGram:
    label=["100 g"]

    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"100grams"

    @classmethod
    def per100g(self):
        return False

class PerCentaGram:
    label=["/100 g"]

    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"per100g"

    @classmethod
    def per100g(self):
        return False

class MilliGram:
    label=["mg"]
    
    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"milligram"

    @classmethod
    def per100g(self):
        return NamespaceResolver.getURI("sd")+"milligram_per100g"

    def create(self):
        return MilliGram()

class MicroGram:
    label=["μg", "mcg", "mcg_RAE", "mcg_DFE"]

    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"microgram"

    @classmethod
    def per100g(self):
        return NamespaceResolver.getURI("sd")+"microgram_per100g"
    
    @classmethod
    def create(self):
        return MicroGram()

class InternationalUnit:
    label=["IU"]

    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"InternationalUnit"

    @classmethod
    def per100g(self):
        return NamespaceResolver.getURI("sd")+"IU_per100g"
    
    @classmethod
    def create(self):
        return InternationalUnit()

class KiloCalorie:
    label=["kcal"]

    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"kilocalorie"

    @classmethod
    def per100g(self):
        return NamespaceResolver.getURI("sd")+"kcal_per100g"

    @classmethod
    def create(self):
        return KiloCalorie()

class KiloJoule:
    label=["kJ"]

    @classmethod
    def getURI(self):
        return NamespaceResolver.getURI("sd")+"kilojoule"

    @classmethod
    def per100g(self):
        return NamespaceResolver.getURI("sd")+"kj_per100g"

    @classmethod
    def create(self):
        return KiloJoule()

class Units:
    units = [Gram, MilliGram, MicroGram, InternationalUnit, KiloCalorie, KiloJoule]

    @classmethod
    def getUnitForLabel(self,label):
        for unit in self.units:
            if unit.label.count(label)==1:
                return unit
        return False
