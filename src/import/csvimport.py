'''
Created on 8 Dec 2010

@author: nebelriss
'''

class Csvimport(object):
    '''
    classdocs
    '''


    def __init__(self, filepath, dbpath, value):
        '''
        Constructor
        '''
        self.filepath = filepath
        self.dbpath = dbpath
        self.value = value
        self.exit()
        
        
    def exit(self):
        return True