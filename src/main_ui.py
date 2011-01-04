#!/usr/bin/python
# encoding: utf-8


from Tkinter import *
from import_ui import *
from data_access import *
from plot import *
from table import *
from data import *
from Listboxes import *



class Main():
    '''
    The Main class is where everything starts.
    
    Initial version by:
        Michel Heiniger and Sandra Lang
    
    Latest source code can be found at:
        https://github.com/nebelriss/FluidX
    '''
    
    def __init__(self, root):
        '''
        Constructor for the main window.
        
        '''
        # get the screen resolution
        # to prevent from the bug with the fullscreen 
        #the resolution is set "-200" in the width and "150" in the height
        self.sw = root.winfo_screenwidth()
        self.sh = root.winfo_screenheight()
        self.sw -= 200
        self.sh -= 150
        root.geometry("%dx%d+0+0" % (self.sw , self.sh))
        
        
        # initialisations
        self.databasename = StringVar()
        self.data = Data()
        self.idx = 0
        self.color = []

        
        # top_frame for the buttons
        # main_frame for the plot- and right frame
        # plot_frame for the plot area with canvas elements
        # right_frame for the sidebar where you can chose the experiment which will be plotted
        top_frame = Frame(root, height = 65)
        top_frame.pack(side = TOP, fill = BOTH, expand = NO)
                
        main_frame = Frame(root)
        main_frame.pack(fill = BOTH, expand = YES) 
                    
        self.plot_frame = Frame(main_frame, relief =  SUNKEN)
        self.plot_frame.pack(side = LEFT, fill = BOTH, expand = YES)
                     
        self.right_frame = Frame(main_frame, width = 250)
        self.right_frame.pack(side = RIGHT, fill = BOTH, expand = NO)


        # there are four buttons in the top_frame:
        # button_open is to open a file dialog and the user can chose a file
        # button_import is to open the import dialog
        # button_table is to open a table with the values in table format, but its disabled at this time
        # button_exit closes all open and related windows of the program    
        button_open = Button(top_frame, text = 'Open', height = 3, width = 7, command = self.fileOpen)
        button_open.pack(side = LEFT, anchor = W, pady = 2)
               
        button_import = Button(top_frame, text = 'Import', height = 3, width = 7, command = self.importer)
        button_import.pack(side = LEFT, padx = 5, pady = 2 )
              
        button_table = Button(top_frame, text = 'Table', height = 3, width = 7, command = self.table, state = DISABLED)
        button_table.pack(side = LEFT, pady = 2)
             
        button_exit = Button(top_frame, text = 'Exit', height = 3, width = 7, command = quit)
        button_exit.pack(side = RIGHT, pady = 2, padx = 5)        
        
        
        # Label in the right_frame. It's in the main file because it should be displayed only once.
        title = Label(self.right_frame, text = "left click to print to plot\n right click to open metadata")
        title.pack(side = TOP, anchor = W)
        
        
        # inserts a plot object from the Plot class
        self.plot = Plot(root, self.plot_frame, self.sw, self.sh)


       
    def table(self):
        '''
        Opens a new window with the values in table format.
        '''
        # the table viewer isn't working at the time


    
    def savedata(self, databasepath):
        '''
        Opens the database file and get the meta and values from it.
        '''
        # store data to lists
        self.data.savedata(databasepath)
        
        # get the values and the meta in a list
        values, meta = self.data.getdata()
        
        # creates a listbox with the meta and values
        Listboxes(self.right_frame, meta, values, self.idx, self.plot, self.color)
        #setting the counter for the listindex +1
        self.idx += 1



    def importer(self):
        '''
        Opens the importer dialog from the Import class and it returns the databasepath from the new sqlite3 file.
        '''
        
        self.importer = Import(root)
        self.savedata(self.importer)
      
        

       
    def fileOpen(self):
        '''
        It's the file-open dialog where you can chose a sqlite3 file and it returns the databasepath.
        '''
        # options for the file dialog.
        # the user will be only allowed files to open with the ending *.sqlite3
        self.file_open = options = {}
        options['filetypes'] = [('database file', '.sqlite3')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Choose your existing database file'
        
        
        # opens the file dialog and it will return the databasepath
        dbpath = askopenfilename(**self.file_open)
        self.databasename.set(dbpath)
        databasepath = self.databasename.get()
        self.savedata(str(databasepath))
        print databasepath


        
        


root = Tk()
root.title("FluidX - 0.2")
main = Main(root)
root.mainloop()
