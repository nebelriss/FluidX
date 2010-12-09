'''
Created on 8 Dec 2010

@author: nebelriss
'''

import csv
import data_access

class Csvimport(object):
    '''
    This class is to import a csv file in a given sqlite3 database.
    '''


    def __init__(self, filepath, dbpath, value):
        '''
        Constructor
        '''
        # init of the given values
        self.filepath = filepath
        self.dbpath = dbpath
        self.value = value
        
    def cvsread(self):
        '''
        Open the csv file with the given path and sniff the dialect to convert it corectly in the self.reader.
        '''
        # opens the csv file with the given path
        csvfile = open(self.filepath, "rb")
        
        # finding the dialect of the csv file
        dialect = csv.reader().sniff(csvfile.read(1024))
        csvfile.seek(0)
        
        # wirte the csv file into reader
        self.reader = csv.reader(csvfile, dialect)
        
    def tosql(self):
        '''
        Now the self.reader will be written to an sqlite3 database.
         
        If self.value is "0" then a new database file will be created
        if its "1" the datas will be written in an existing database.
        '''
        
        # if value is 0, a new database file will be created at the path were the user has chosen
        if self.value == "0":
            