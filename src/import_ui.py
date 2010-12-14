#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
from tkFont import *
from tkFileDialog import *
from csvimport import *
from tkMessageBox import *



class Import_ui(object):
    '''
    This Class is for importing CSV files with a specific format that is given out to the creators.
    First the file will be read with csvreader and stored in a sqlite3 database. 
    '''

    def __init__(self, root):
        '''
        Constructor for a import window where the user can open his csv file and import it to a new or
        an existing database.
        '''

        # init
        self.value = IntVar()
        self.filepath = StringVar()
        self.databasename = StringVar()
        
        
        # main Frame
        self.frame = Frame(root)
        # grid frame
        self.frame.grid() 
        # Title showed inside the window  
        self.csvLabel = Label(self.frame, text = "CSV - Import")
        myfont = Font(family = 'Arial', size = 14, weight = BOLD)
        self.csvLabel.config(font = myfont)
        self.dirLabel = Label(self.frame, text = "Folder: ")
        self.emptylabel = Label(self.frame, height = 1)
        #Entry
        self.entryPath = Entry(self.frame, width = 40, textvariable = self.filepath, bg = "grey")
        self.entryPath.insert(END, "~/file.csv")
        # Radiobuttons, new Database or existing database
        self.newDB = Radiobutton(self.frame, text = "Create new Database", variable = self.value, value = 0)
        self.existDB = Radiobutton(self.frame, text = "Use existing Database", variable = self.value, value = 1)
        # Buttons to start import and quit the import window
        self.buttonBrowse = Button(self.frame, text = "Browse", command = self.csvopenfilename)
        self.buttonOK = Button(self.frame, text = "OK", width = 5, command = self.cvstosql)
        self.buttonCancel = Button(self.frame, text = "Cancel", command = quit)
        
        # grit for widget, position etc.
        self.csvLabel.grid(row = 0, column = 0, columnspan = 2, sticky = (N, W), pady = 10, padx = 5)
        self.dirLabel.grid(row = 1, column = 0, padx = 5)
        self.emptylabel.grid(row = 2, column = 0)
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
        options['parent'] = root
        options['title'] = 'choose csv file'
        filepath = askopenfilename(**self.file_opt)
        self.filepath.set(filepath)
        
    def sqlnewfilename(self):
        '''
        Opens a dialog where the user can chose the location of his file to save it. But the file will not be saved directly it 
        only writes the path to self.databasename
        '''
        self.file_save = options = {}
        options['filetypes'] = [('tes files', '.tes')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Save your Database file'
        databasename = asksaveasfilename(**self.file_save)
        self.databasename.set(databasename)
        
    def sqlopenfilename(self):
        '''
        opens a dialoge where the user can chose the location of an existing database, the path is saved then in databasename.
        '''
        self.file_open = options = {}
        options['filetypes'] = [('tes files', '.tes')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
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
            quit()
        #if the import was iterrupted an error message will be showed
        else:
            showwarning("Import Error", "Import the Database\n wasn't successful!")
            

        
        

root = Tk()
win2 = Toplevel(root)
importer = Import_ui(win2)
root.title("Import - FluidX") # window title

# max and min size for the window, so the window has a fix size
root.resizable(width=FALSE, height=FALSE)
root.mainloop()