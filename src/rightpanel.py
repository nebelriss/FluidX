#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
from data import *


class Rightpanel():
    '''
    classdocs
    '''


    def __init__(self, frame):
        '''
        Constructor
        '''

        
        # load data
        d = Data()
        self.values, self.meta = d.getdata()
        self.frame = frame
        
        #
        for i in range (0,len(self.meta)):
            meta_tmp = self.meta[i]
            print meta_tmp['additional_info']
        
        #Labels for Listbox
        motor_label = Label(self.frame, text = "motors")
        motor_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        self.motor_listbox = Listbox(self.frame, selectmode = SINGLE, height = 4)
        self.motor_listbox.pack(side=TOP, padx = 20)
        
        self.motor_listbox.insert(END, "series_nr 1")
        self.motor_listbox.insert(END, "series_nr 2")
        self.motor_listbox.insert(END, "series_nr 3")
        
        # read selected in motor_listbox
        self.motor_listbox.bind("<<ListboxSelect>>", self.sel_motor)
            
        
        # Listbox
        medium_label = Label(self.frame, text = "mediums")
        medium_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        self.medium_listbox = Listbox(self.frame, selectmode = SINGLE, height = 3)
        self.medium_listbox.pack(side=TOP, padx = 20)
        self.medium_listbox.insert(END, "water")
        self.medium_listbox.insert(END, "oil")
        self.medium_listbox.insert(END, "ethonol")
        
        #red selected in medium_listbox
        self.medium_listbox.bind("<<ListboxSelect>>", self.sel_medium)
        
        
        
        # Checkbox
        ex_label = Label(self.frame, text = "Experiments")
        ex_label.pack(side = TOP, anchor = W, pady = 20, padx = 20)
    
        
        # Frame for checkboxes
        check_frame = Frame(self.frame, relief = SUNKEN, bg = 'white')
        check_frame.pack(side = TOP, pady = 20, padx = 20, fill = BOTH, expand = YES)
        for i in range(0,5):
            check = "CheckMe " + str(i)
            checkbox = Checkbutton(check_frame, text = check, bg = 'white')
            checkbox.pack(side = TOP, anchor = W,expand = NO)
            
            
    def sel_motor(self, event):
        self.selected_motor = self.motor_listbox.get(self.motor_listbox.curselection()[0])
        print self.selected_motor

    def sel_medium(self, event):       
        self.selected_medium = self.medium_listbox.get(self.medium_listbox.curselection()[0])
        print self.selected_medium