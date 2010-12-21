#!/usr/bin/python
# encoding: utf-8


from Tkinter import *
from import_ui import *
from data_access import *
from plot import *
from table import *
from data import *
from Listboxes import *
import threading


class Main():
    
    def __init__(self, root):
        '''
        Constructor for the main Gui.
        '''
        self.screenSize()
        
        # init db name
        self.databasename = StringVar()
        self.data = Data()
        self.idx = 0

        
        # Frames
        top_frame = Frame(root, height = 65)
        main_frame = Frame(root)
        self.plot_frame = Frame(main_frame, relief =  SUNKEN)
        self.right_frame = Frame(main_frame, width = 250)
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
        button_open.pack(side = LEFT, anchor = W, pady = 2) 
        button_import.pack(side = LEFT, padx = 5, pady = 2 ) 
        button_table.pack(side = LEFT, pady = 2)
        button_exit.pack(side = RIGHT, pady = 2, padx = 5)
        
        self.plot()
        
        
#screen size##########################################################################################        
    def screenSize(self):
        '''
        asking for screen witdh and height
        '''
        self.sw = root.winfo_screenwidth()
        self.sh = root.winfo_screenheight()
        self.sw -= 200
        self.sh -= 150
        root.geometry("%dx%d+0+0" % (self.sw , self.sh))
###################################################################################################

        
#plot##############################################################################################      
    def plot(self):
        '''
        
        ''' 
        self.plot = Plot(root, self.plot_frame, self.sw, self.sh)
###################################################################################################

#updateplot##############################################################################################      
    def updateplot(self, meta, values):
        '''
        
        ''' 
        canvas_data = []
        canvas_data.append([])
        print canvas_data
###################################################################################################


#save data##########################################################################################           
    def table(self):
        '''
        
        '''
        t = Table(root)
###################################################################################################

        
        
#save data##########################################################################################       
    def savedata(self, databasepath):
        '''
        opening the database and get infos out of the sql
        '''
        # store datas to lists
        self.data.savedata(databasepath)
        self.getdata()
###################################################################################################        
        

#save data##########################################################################################       
    def getdata(self):
        '''

        '''
        values, meta = self.data.getdata()
        lister = Listboxes(self.right_frame, meta, values, self.idx, self.plot)
###################################################################################################



#importer##########################################################################################
    def importer(self):
        '''
        opens the importer window
        '''
        self.importer = Import_ui(root)
        self.savedata(self.importer)
##################################################################################################         
        


# open button file dialog #########################################################################        
    def fileOpen(self):
        '''
        
        '''
        self.file_open = options = {}
        options['filetypes'] = [('database file', '.tes')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Choose your existing database file'
        dbpath = askopenfilename(**self.file_open)
        self.databasename.set(dbpath)
        databasepath = self.databasename.get()
        self.savedata(databasepath)
################################################################################################## 

        
        


root = Tk()
root.title("FluidX - 0.1")
main = Main(root)
root.mainloop()