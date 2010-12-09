#!/usr/bin/python
# encoding: utf-8
'''
Created on 8 Dec 2010

@author: nebelriss
'''

import csv
from data_access import *
import sys

class Csvimport(object):
    '''
    This class is to import a csv file in a given sqlite3 database.
    '''


    def __init__(self, filepath, dbpath, value):
        '''
        Constructor
        '''
        # init of the given values
        self.filepath = filepath # path to the csv file
        self.dbpath = dbpath # path to the db file
        self.value = value # is 0 or 1
        self.vn = 10 # number of values given by groups
        
    def cvsread(self):
        '''
        Open the csv file with the given path and sniff the dialect to convert it correctly in the self.reader.
        '''
        # opens the csv file with the given path
        csvfile = open(self.filepath, "rb")
        
        # finding the dialect of the csv file
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        
        # wirte the csv file into reader
        self.reader = csv.reader(csvfile, dialect)
        
    def tosql(self):
        '''
        Now the self.reader will be written to an sqlite3 database.
        
        To access the database and store values we use the data_acces class written by "Tobias Thüring" and "Patrick Pfeifer"
        this file is used by every group to get the same structure in the db file
         
        If self.value is "0" then a new database file will be created
        if its "1" the datas will be written in an existing database.
        '''
        # open database connection with the parameters database path and number of v values
        db = Experiment(str(self.dbpath), self.vn)
        
        # read values of each row and store it in the database
        for row in self.reader:
            
            # read the id number in the first column of each row
            id = str(row[0])
            
            # test if the first value in each row is a digit and if its a valid id
            if id.isdigit() and len(id) == 4:
                
                # store values in db
                print row[2:]
                db.store_values(int(id), row[2:])
                
                
            