#!/usr/bin/python
# encoding: utf-8


from Tkinter import *
from import_ui import *
from data_access import *
from plot import *
from table import *
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
        self.data = Data()
        self.values_height = 3
        self.values_id = 0
        self.motor_control = []
        self.media_control = []

        
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
        
        #right panel#
        #Labels for Listbox
        motor_label = Label(self.right_frame, text = "motors")
        motor_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        self.motor_listbox = Listbox(self.right_frame, selectmode = SINGLE, height = 4)
        self.motor_listbox.pack(side=TOP, padx = 20)      
       
        # read selected in motor_listbox
        self.motor_listbox.bind("<<ListboxSelect>>", self.sel_motor)
            
        
        # Listbox
        medium_label = Label(self.right_frame, text = "mediums")
        medium_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        self.medium_listbox = Listbox(self.right_frame, selectmode = SINGLE, height = 3)
        self.medium_listbox.pack(side=TOP, padx = 20)
        
        #read selected in medium_listbox
        self.medium_listbox.bind("<<ListboxSelect>>", self.sel_medium)
        
        
        
        
        # Values label
        ex_label = Label(self.right_frame, text = "Experiments")
        ex_label.pack(side = TOP, anchor = W, pady = 20, padx = 20)
    
        
        # Frame for checkboxes
        self.values_frame = Frame(self.right_frame)
        self.values_frame.pack(side =TOP, padx = 20, fill = BOTH, expand = NO)
        self.values_listbox = Listbox(self.values_frame, selectmode = MULTIPLE, height = 4)
        self.values_listbox.pack(side = TOP, fill = BOTH, expand = YES)
        self.values_listbox.bind("<<ListboxSelect>>", self.sel_values)
        
        
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
        plot = Plot(root, self.plot_frame, self.sw, self.sh)
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
        # store datas to lists
        self.values, self.meta = self.data.getdata()
        self.canvas_data = []
        # refresh entries in the listboxes
        for i in range(0, len(self.meta)):
            meta_tmp = self.meta[i]
            motor_meta = meta_tmp['exp_name']
            # control if entry already exists
            if len(self.motor_control) == 0:
                self.motor_control.append(motor_meta)
                # insert into the_listboxes
                self.motor_listbox.insert(END, "M: " + str(motor_meta))
            else:
                for m in range(0,len(self.motor_control)):
                    if motor_meta != self.motor_control[m]:
                        self.motor_control.append(motor_meta)
                        # insert into the_listboxes
                        self.motor_listbox.insert(END, "M: " + str(motor_meta))
                    else:
                        pass
                    

        for i in range(0, len(self.meta)):
            meta_tmp = self.meta[i]
            media_meta = meta_tmp['additional_info']
            # control if entry already exists
            if len(self.media_control) == 0:
                self.media_control.append(media_meta)
                # insert into the_listboxes
                self.medium_listbox.insert(END, str(media_meta))
            else:
                for m in range(0,len(self.media_control)):
                    print "shit"
                    if media_meta != self.media_control[m]:
                        print "shit2"
                        self.media_control.append(media_meta)
                        # insert into the_listboxes
                        self.medium_listbox.insert(END, str(media_meta))
                    else:
                        print "shit3"
                        pass
            
            # create checkboxes

            self.canvas_data.append([])
            for j in range(0, len(self.values)):
                values = self.values[j]
                for row in values:
                    self.values_id += 1
                    box_name = str(self.values_id) + ":  " + str(row[2]) + "/" + str(row[1]) + "/" + str(row[3])
                    self.values_listbox.insert(END, str(box_name))
                    self.values_listbox.configure(height = self.values_height)
                    self.values_height += 1
                    # wirte infos to List
                    self.canvas_data[j].append([meta_tmp, row])

###################################################################################################



# events for values_listbox #############################################################################       
    def sel_values(self, event):
        '''
        
        '''

        for i in range(len(self.values_listbox.curselection())):
            self.selected_values = self.values_listbox.get(self.values_listbox.curselection()[i])
            sel_nr = self.selected_values[0]
            for row in self.canvas_data:
                meta = row[int(sel_nr)][0]
                values = row[int(sel_nr)][1]
                
                plot.createCanvas(meta, row)

        print
################################################################################################## 


       
#importer##########################################################################################
    def importer(self):
        '''
        opens the importer window
        '''
        self.i = Import_ui(root)
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
        


        
# events for motor and medium listbox #############################################################################       
    def sel_motor(self, event):
        '''
        
        '''
        for i in range(len(self.motor_listbox.curselection())):
            self.selected_motor = self.motor_listbox.get(self.motor_listbox.curselection()[i])
            print self.selected_motor

    def sel_medium(self, event): 
        '''
         
        '''
        self.selected_medium = self.medium_listbox.get(self.medium_listbox.curselection()[0])
        print self.selected_medium
##################################################################################################        
        


root = Tk()
root.title("FluidX - 0.1")

main = Main(root)
root.mainloop()