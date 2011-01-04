#!/usr/bin/python
# encoding: utf-8

from data_access import *



class Data():
    '''
    Initial version by:
        Michel Heiniger and Sandra Lang
    
    Latest source code can be found at:
        https://github.com/nebelriss/FluidX
    '''
    
    def __init__(self):
        '''
        constructor for empty lists
        '''
        # initialize empty list for values and meta
        self.values = []
        self.meta = []
 
    def savedata(self, dbpath):
        '''
        
        '''
        # open sqlite3 connection
        db = Experiment(dbpath)
        
        # write values and meta to sqlite3 file
        values = db.load_values()
        meta = db.load_metadata()
        
        # send values and meta to store them in a list
        self.storedata(values, meta)


    def storedata(self, v, m):
        '''
        storing meta and values in a list
        '''
        self.values.append(v)
        self.meta.append(m)

    
    def getdata(self):
        '''
        returns values and meta
        '''       
        return self.values, self.meta