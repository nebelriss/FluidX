#!/usr/bin/python
# encoding: utf-8

from data_access import *
import sys
import csv


class Csvimport(object):
    '''
    This class is to import a csv file in a given or new sqlite3 database.
    For the SQL connection and the table design is the data_access.py file used.
    More informations and docs see data_access.py file.
    
    Initial version by:
        Michel Heiniger and Sandra Lang
    
    Latest source code can be found at:
        https://github.com/nebelriss/FluidX
           
    The latest documentation about the csv file-format can be found at:
        https://github.com/nebelriss/FluidX/csv-file.pdf
    '''


    def __init__(self, filepath, dbpath):
        '''
        Constructor for the class, given variable 
        '''
        # path to the csv file
        self.filepath = filepath
        # path to the db file
        self.dbpath = dbpath 
        # number of values given by groups
        self.vn = 6 
        
        
        
    def cvsread(self):
        '''
        Opens the csv file with the given path and sniff the dialect 
        to convert it correctly and write it to the self.reader.
        '''
        # opens the csv file with the given path and read only rights
        csvfile = open(self.filepath, "rb")
        
        # looking for the dialect of the csv file
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)

        # wirte the csv file into a list
        self.reader = csv.reader(csvfile, dialect)
   
   
        
    def tosql(self):
        '''
        Now the self.reader will be written to an sqlite3 database.
        
        To access the database and store values we use the data_acces class written by "Tobias Thüring" and "Patrick Pfeifer"
        this file is used by every group to get the same structure in the db file.
        More informations and docs see data_access.py file.
         
        If self.value is "0" then a new database file will be created
        if its "1" the data will be written in an existing database.
        '''
        #init of a empty dictionary for the meta datas
        meta = {}
             
        
        # open database connection with the parameters database path and number of v values which are set in the constructor
        db = Experiment(str(self.dbpath), self.vn)
        
        
        # storing values in the sqlite3 file
        #
        # reading values of each row and store it in the database
        for row in self.reader:
            
            # read the id number in the first column of each row
            id = str(row[0])
            
            # test if the first value in each row is a digit and if its a valid id
            if id.isdigit and len(id) == 1:
                meta.update({'exp_name':row[1], 'actor_name': unicode(str(row[2])), 'additional_info': row[3], 'date': row[4]})
            
            
            # if the first value is 'ID' then it is a metaline with metaunit and meta description
            elif row[0] == 'ID':
                n = 1  
                
                # now every column will be read           
                for i in range(1,len(row)):
                    
                    # building the metaunit and metadesc name
                    metaunit = 'v' + str(n) + '_unit'
                    metadesc = 'v' + str(n) + '_desc'
                    word = row[i]
                    
                    # the format of a value look like "metadescription[metaunit]"
                    # so it is looking for the "[" and "]" signs to know where the metaunit is starting and ending 
                    a = word.find('[')
                    b = word.find(']')
                    
                    # writing/updating the new metavalues to the dictionary
                    meta.update({metaunit: unicode(word[a + 1:b]), metadesc: unicode(word[:a])})
                    n = n + 1
        
            
            # if the fist digit equals 4 the this line is a valueline
            elif id.isdigit() and len(id) == 4:
                
                # store values in db-file
                row_tmp = row[2:]
                db.store_metadata(meta)
                db.store_values(int(id), [row_tmp])
            
            
            # 
            else: return False
        
        
        #returning True to import_ui if the import to the sqlite-file was successful
        return True
                
                
                
            
