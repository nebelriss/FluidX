#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
from tkFont import *
from tkFileDialog import *
from csvimport import *
from tkMessageBox import *
from data import *




class Import(object):
    '''
    This Class is for importing CSV files with a specific format that is given out to the creators.
    First the file will be read with csvreader and stored in a sqlite3 database.
    
    The latest documentation about the csv file-format can be found at:
        https://github.com/nebelriss/FluidX/csv-file.pdf
    '''

    def __init__(self, root):
        '''
        Constructor for a import window where the user can open his csv file and import it to a new or
        an existing database.
        '''
        
        # child window parameters
        self.child = Toplevel(root)
        self.child.title("Import - FluidX")
        self.child.resizable(width=FALSE, height=FALSE)
        
        # inits
        self.value = IntVar()
        self.filepath = StringVar()
        self.databasename = StringVar()
        
        # Label values
        csv_title = "CSV - Import"
        dir_txt = "Folder: "
        given_path = "~/file.csv"
        newdb_txt = "Create new Database"
        exdb_txt = "Create new Database"
        browse_txt = "Browse"
        ok_txt = "OK"
        cancel_txt  = "Cancel"
        
        
        # main Frame
        self.frame = Frame(self.child)
        self.frame.grid()         
        

        # Title showed inside the window
        csvLabel = Label(self.frame, text = csv_title)
        self.csvLabel.grid(row = 0, column = 0, columnspan = 2, sticky = (N, W), pady = 10, padx = 5)
        
        # changing font and raising size of the title       
        myfont = Font(family = 'Arial', size = 14, weight = BOLD)
        csvLabel.config(font = myfont)

        
        # Directory and emtpylabel for a space
        self.dirLabel = Label(self.frame, text = dir_txt)
        self.dirLabel.grid(row = 1, column = 0, padx = 5)
             
        self.emptylabel = Label(self.frame, height = 1)
        self.emptylabel.grid(row = 2, column = 0)
       
        
        #Entry
        self.entryPath = Entry(self.frame, width = 40, textvariable = self.filepath, bg = "grey")
        self.entryPath.insert(END, given_path)
        # Radiobuttons, new Database or existing database
        self.newDB = Radiobutton(self.frame, text = newdb_txt, variable = self.value, value = 0)
        self.existDB = Radiobutton(self.frame, text = exdb_txt, variable = self.value, value = 1)
        # Buttons to start import and quit the import window
        self.buttonBrowse = Button(self.frame, text = browse_txt, command = self.csvopenfilename)
        self.buttonOK = Button(self.frame, text = ok_txt, width = 5, command = self.cvstosql)
        self.buttonCancel = Button(self.frame, text = cancel_txt, command = self.child.destroy)
        
        # grit for widget, position etc.


        self.entryPath.grid(row = 1, column = 1, columnspan = 1, sticky = (N, W), padx = 5, pady = 2.5)
        self.buttonBrowse.grid(row = 1, column = 2, sticky = W, padx = 5)
        self.newDB.grid(row = 3, column = 1, sticky = W, columnspan = 2)
        self.existDB.grid(row = 4, column = 1, sticky = W, columnspan = 2)
        self.buttonOK.grid(row = 6, column = 2, sticky = (S, E), padx = 5, pady = 5)
        self.buttonCancel.grid(row = 6, column = 1, sticky = (S, E), pady = 5)
        
    def csvopenfilename(self):
        '''
        Opens a file dialog to choose a csv-file and then the path and filename is send to the filepath variable
        to update entryPath, so the path will be showed in the entry.
        '''
        self.file_opt = options = {}
        options['filetypes'] = [('csv files', '.csv')]
        options['initialdir'] = 'C:\\'
        options['parent'] = self.child
        options['title'] = 'choose csv file'
        filepath = askopenfilename(**self.file_opt)
        self.filepath.set(filepath)
        
    def sqlnewfilename(self):
        '''
        Opens a dialog where the user can chose the location of his file to save it. But the file will not be saved directly it 
        only writes the path to self.databasename
        '''
        self.file_save = options = {}
        options['filetypes'] = [('sqlite3 files', '.sqlite3')]
        options['initialdir'] = 'C:\\'
        options['parent'] = self.child
        options['title'] = 'Save your Database file'
        databasename = asksaveasfilename(**self.file_save)
        self.databasename.set(databasename)
        
    def sqlopenfilename(self):
        '''
        opens a dialoge where the user can chose the location of an existing database, the path is saved then in databasename.
        '''
        self.file_open = options = {}
        options['filetypes'] = [('sqlite3 files', '.sqlite3')]
        options['initialdir'] = 'C:\\'
        options['parent'] = self.child
        options['title'] = 'Choose your existing database file'
        databasename = askopenfilename(**self.file_open)
        self.databasename.set(databasename)
        
        
    def cvstosql(self):
        '''
        sends information about filepath, filename, and Database name
        '''
        # opens a filedialog 
        if self.value.get() == 0:
            self.sqlnewfilename()
        else:
            self.sqlopenfilename()
        
        
        # check if databasename is empty
        if self.databasename.get() == "":
            pass
        #if not send values to Csvimport class
        else:
            showinfo("Reading Database", "Reading Database")
            
            #  converting values to string
            filepath = self.filepath.get()
            databasename = self.databasename.get()
            value = self.value.get()
            
            # sending string values to read csv and write to sql
            check = Csvimport(filepath, databasename)
            check.cvsread()
            ok = check.tosql()
            
            

        #if Csvimport return True it mean that the import of the csv file to the sql was successful
        if ok == True:
            self.child.destroy()
            return databasename
        #if the import was iterrupted an error message will be showed
        else:
            showwarning("Import Error", "Import the Database\n wasn't successful!")

                