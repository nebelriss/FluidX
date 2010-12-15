#!/usr/bin/python
# encoding: utf-8
from data_access import *

class Data():
    
    def __init__(self):
        self.values = []
        self.meta = []
 
    def saveata(self, dbpath):
        db = Experiment(dbpath)
        values = db.load_values()
        meta = db.load_metadata()
        
        self.storedata(values, meta)
        print dbpath


    def storedata(self, v, m):
        self.values.append(v)
        self.meta.append(m)
    
    
    def getdata(self):
        values = self.values
        meta = self.meta
        
        return values, meta