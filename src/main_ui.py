#!/usr/bin/python
# encoding: utf-8


from Tkinter import *
from import_ui import *
from data_access import *
from plot import *
from table import *
from rightpanel import *
from data import *


class Main():
    
    def __init__(self, root):
        '''
        Constructor for the main Gui.
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
        
        #right panel#########################################################################
        #Labels for Listbox
        motor_label = Label(self.right_frame, text = "motors")
        motor_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        

        self.motor_listbox = Listbox(self.right_frame, selectmode = SINGLE, height = 4)
        self.motor_listbox.pack(side=TOP, padx = 20)
        
        self.motor_listbox.insert(END, "series_nr 1")
        
        # read selected in motor_listbox
        self.motor_listbox.bind("<<ListboxSelect>>", self.sel_motor)
            
        
        # Listbox
        medium_label = Label(self.right_frame, text = "mediums")
        medium_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        self.medium_listbox = Listbox(self.right_frame, selectmode = SINGLE, height = 3)
        self.medium_listbox.pack(side=TOP, padx = 20)
        self.medium_listbox.insert(END, "water")
        self.medium_listbox.insert(END, "oil")
        self.medium_listbox.insert(END, "ethonol")
        
        #read selected in medium_listbox
        self.medium_listbox.bind("<<ListboxSelect>>", self.sel_medium)
        
        # Checkbox
        ex_label = Label(self.right_frame, text = "Experiments")
        ex_label.pack(side = TOP, anchor = W, pady = 20, padx = 20)
    
        
        # Frame for checkboxes
        check_frame = Frame(self.right_frame, relief = SUNKEN, bg = 'white')
        check_frame.pack(side = TOP, pady = 20, padx = 20, fill = BOTH, expand = YES)
        for i in range(0,5):
            check = "CheckMe " + str(i)
            checkbox = Checkbutton(check_frame, text = check, bg = 'white')
            checkbox.pack(side = TOP, anchor = W,expand = NO)
        
        
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
        Rightpanel(self.right_frame)

        
          
    def table(self):
        '''
        
        '''
        t = Table(root)
        
    def savedata(self, databasepath):
        '''
        opening the database and get infos out of the sql
        '''
        # store datas to lists
        d = Data()
        d.savedata(databasepath)
       
    
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
        self.savedata(databasepath)
        
    def sel_motor(self, event):
        '''
        
        '''
        self.selected_motor = self.motor_listbox.get(self.motor_listbox.curselection()[0])
        print self.selected_motor

    def sel_medium(self, event): 
        '''
         
        '''
        self.selected_medium = self.medium_listbox.get(self.medium_listbox.curselection()[0])
        print self.selected_medium1 
        
        

root = Tk()
root.title("FluidX - 0.1")

main = Main(root)
root.mainloop()