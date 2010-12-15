#!/usr/bin/python
# encoding: utf-8


from Tkinter import *
from import_ui import *
from data_access import *
from plot import *
from table import *
from rightpanel import *


class Main():
    
    def __init__(self, root):
        '''
    
        '''
        self.screenSize()
        
        # init db name
        self.databasename = StringVar()
        self.values = []
        self.meta = []

        
        # Frames
        top_frame = Frame(root, height = 65)
        main_frame = Frame(root)
        self.plot_frame = Frame(main_frame, relief =  SUNKEN)
        self.right_frame = Frame(main_frame, width = 250, bg = 'red')
        # Frames pack
        top_frame.pack(side = TOP, fill = BOTH, expand = NO)
        main_frame.pack(fill = BOTH, expand = YES)
        self.plot_frame.pack(side = LEFT, fill = BOTH, expand = YES)
        self.right_frame.pack(side = RIGHT, fill = BOTH, expand = NO)
        
        # Scrollbar
        scrollbar = Scrollbar(self.right_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
    
    
        # Buttons are temporary until they get pics inside etc
        # Buttons in the top_frame
        button_open = Button(top_frame, text = 'Open', height = 3, width = 7, command = self.fileOpen)
        button_import = Button(top_frame, text = 'Import', height = 3, width = 7, command = self.importer)
        button_table = Button(top_frame, text = 'Table', height = 3, width = 7, command = self.table)
        button_exit = Button(top_frame, text = 'Exit', height = 3, width = 7, command = quit)
        # Button packers
        button_open.pack(side = LEFT, anchor = W) 
        button_import.pack(side = LEFT, padx = 5 ) 
        button_table.pack(side = LEFT)
        button_exit.pack(side = RIGHT)
        
        
        self.rightpanel()
        self.plot()
        
    def screenSize(self):
        '''
        asking for screen witdh and height
        '''
        self.sw = root.winfo_screenwidth()
        self.sh = root.winfo_screenheight()
        self.sw -= 200
        self.sh -= 150
        root.geometry("%dx%d+0+0" % (self.sw , self.sh))
        
    def plot(self):
        '''
        
        ''' 
        Plot(root, self.plot_frame, self.sw, self.sh)
        
    def rightpanel(self):
        '''
        
        '''
        try:
            Rightpanel(self.right_frame)
        except AttributeError:
            raise Exception("AttributeError: Main instance has no attribute 'values'")
        
          
    def table(self):
        '''
        
        '''
        tab = Table(root)
        
    def readdata(self, databasepath):
        '''
        opening the database and get infos out of the sql
        '''
        self.values = []
        self.meta = {}
        db = Experiment(databasepath)
        values = db.load_values()
        meta = db.load_metadata()
        
        # store datas to lists
        self.values.append(values)
        self.meta.append(meta)
        

       
    
    def importer(self):
        '''
        opens the importer window
        '''
        self.i = Import_ui(root)

        
    def fileOpen(self):
        '''
        
        '''
        self.file_open = options = {}
        options['filetypes'] = [('database file', '.tes')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Choose your existing database file'
        databasename = askopenfilename(**self.file_open)
        self.databasename.set(databasename)
        databasepath = self.databasename.get()
        self.readdata(databasepath)
        
        

root = Tk()
root.title("FluidX - 0.1")

main = Main(root)
root.mainloop()