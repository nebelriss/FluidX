#!/usr/bin/python
# encoding: utf-8
class Data():
 
    def saveata(self, dbpath):
        print dbpath


    def storedata(self, v, m):
        self.values.append(v)
        self.meta.append(m)
    
    
    def getdata(self):
        return self.values, self.meta