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
    First the file will be read with csvreader and stored in a sqlite database. 
    '''

    def __init__(self, root):
        '''
        Creates a import window, where the user can choose the location of the csv file and in witch database he wants to write it
        '''

        # init
        self.value = IntVar()
        self.filepath = StringVar()
        self.databasename = StringVar()

        self.frame = Frame(root)
        # grid frame
        self.frame.grid(row = 1, column = 0) 
        # Title showed inside the window  
        self.csvLabel = Label(self.frame, text = "CSV - Import")
        myfont = Font(family = 'Arial', size = 14, weight = BOLD)
        self.csvLabel.config(font = myfont)
        self.dirLabel = Label(self.frame, text = "Folder: ")
        self.emptylabel = Label(self.frame, height = 1)
        #Entry
        self.entryPath = Entry(self.frame, width = 40, textvariable = self.filepath)
        self.entryPath.insert(END, "~/file.csv")
        #Radiobutton
        self.newDB = Radiobutton(self.frame, text = "Create new Database", variable = self.value, value = 0)
        self.existDB = Radiobutton(self.frame, text = "Use existing Database", variable = self.value, value = 1)
        # Buttons to start import and quit the import window
        self.buttonBrowse = Button(self.frame, text = "Browse", command = self.csvopenfilename)
        self.buttonOK = Button(self.frame, text = "OK", width = 5, command = self.cvstosql)
        self.buttonCancel = Button(self.frame, text = "Cancel", command = quit)
        
        # grit for widget, position etc.
        self.csvLabel.grid(row = 0, column = 0, columnspan = 2, sticky = (N, W), pady = 10, padx = 5)
        self.dirLabel.grid(row = 1, column = 0)
        self.emptylabel.grid(row = 2, column = 0)
        self.entryPath.grid(row = 1, column = 1, columnspan = 1, sticky = (N, W), padx = 5, pady = 2.5)
        self.buttonBrowse.grid(row = 1, column = 2, sticky = W, padx = 5)
        self.newDB.grid(row = 3, column = 0, sticky = W, columnspan = 2)
        self.existDB.grid(row = 4, column = 0, sticky = W, columnspan = 2)
        self.buttonOK.grid(row = 6, column = 2, sticky = (S, E), padx = 5, pady = 5)
        self.buttonCancel.grid(row = 6, column = 1, sticky = (S, E), pady = 5)
        
    def csvopenfilename(self):
        '''
        Opens a file dialog to choose a csv file and then the path and filename is send to the filepath variable to update entryPath, so the path will be showed in the entry.
        '''
        self.file_opt = options = {}
        options['filetypes'] = [('csv files', '.csv')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'choose csv file'
        filepath = askopenfilename(**self.file_opt)
        self.filepath.set(filepath)
        
    def sqlnewfilename(self):
        self.file_save = options = {}
        options['filetypes'] = [('tes files', '.tes')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'save your Database file'
        databasename = asksaveasfilename(**self.file_save)
        self.databasename.set(databasename)
        
    def sqlopenfilename(self):
        self.file_open = options = {}
        options['filetypes'] = [('tes files', '.tes')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'choose your existing database file'
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
        if self.databasename.get() == " ":
            print
        #if not send values to Csvimport class
        else:
            showinfo("Reading Database", "Reading Database")
            check = Csvimport(self.filepath, self.databasename, self.value)

        
        if check.exit() == True:
            quit()
        else:
            showwarning("Import Error", "Import the Database\n wasn't successful!")
            

        
        

root = Tk()
importer = Import_ui(root)
root.title("Import - FluidX") # window title

# max and min size for the window, so the window has a fix size
root.resizable(width=FALSE, height=FALSE)
root.mainloop()