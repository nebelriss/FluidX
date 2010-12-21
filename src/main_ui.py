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
    
    def __init__(self, root):
        '''
        Constructor for the main Gui.
        '''
        self.screenSize()
        
        # init db name
        self.databasename = StringVar()
        self.values = []
        self.meta = []
        self.data = Data()
        self.values_height = 3
        self.values_id = 0
        self.idx = 0
        self.i = 0

        
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
        self.create_Listbox(meta, values, self.idx)
        self.idx += 1
###################################################################################################



#importer##########################################################################################
    def importer(self):
        '''
        opens the importer window
        '''
        self.importer = Import_ui(root)
        print str(self.importer)
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

    def create_Listbox(self, meta, values, idx):
        '''
        
        '''
        values_height = 1
        values_frame = Frame(self.right_frame)
        values_frame.pack(side =TOP, padx = 20, fill = BOTH, expand = NO, pady = 10)
        
        # get meta
        meta_tmp = meta[idx]
        date_meta = str(meta_tmp['date'])
        motor_meta = str(meta_tmp['exp_name'])
        media_meta = str(meta_tmp['additional_info'])
        self.i += 1
        
        #convert date
        date_txt = date_meta[6:8] + "." + date_meta[4:6] + "." + date_meta[:4] + " " + date_meta[8:10] + ":" + date_meta[10:]
        motor_txt = "Motor: " + motor_meta
        media_txt = "Media: " + media_meta
        # create Labels
        motor_label = Label(values_frame, text = motor_txt)
        motor_label.pack(side = TOP, anchor = W)
        
        media_label = Label(values_frame, text = media_txt)
        media_label.pack(side = TOP, anchor = W)
        
        date_label = Label(values_frame, text = date_txt)
        date_label.pack(side = TOP, anchor = W)
        
        # create Listbox

        self.values_listbox = Listbox(values_frame, selectmode = MULTIPLE, height = values_height, exportselection=0)
        self.values_listbox.pack(side = TOP, fill = BOTH, expand = YES)
        self.values_listbox.bind("<<ListboxSelect>>", self.sel_values)
        
        self.canvas_data = []
        values_id = 0
        values = values[idx]
        print self.idx
        for row in values:
            values_id += 1
            box_name = str(values_id) + ":  " + str(row[2]) + "/" + str(row[1]) + "/" + str(row[3])
            self.values_listbox.insert(END, str(box_name))
            self.values_listbox.configure(height = values_height)
            values_height += 1
            # wirte infos to List
            self.canvas_data.append([meta_tmp, row])

            
                
    def sel_values(self, event):
        sel_values_list = []
        for i in range(len(self.values_listbox.curselection())):
            sel_values = self.values_listbox.get(self.values_listbox.curselection()[i])
            sel_nr = sel_values[0]
            row = self.canvas_data[int(sel_nr)]
            meta_plot = row[0]
            values = row[1]
            print values
            sel_values_list.append(values)
            
        # update plot with the new datas    
        self.updateplot(meta_plot, sel_values_list)
        
        


root = Tk()
root.title("FluidX - 0.1")
main = Main(root)
root.mainloop()