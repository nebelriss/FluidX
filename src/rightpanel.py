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
        motor_listbox = Listbox(self.frame, selectmode = SINGLE, height = 4)
        motor_listbox.pack(side=TOP, padx = 20)
        
        motor_listbox.insert(END, "series_nr 1")
        motor_listbox.insert(END, "series_nr 2")
        motor_listbox.insert(END, "series_nr 3")
        
        # Listbox
        medium_label = Label(self.frame, text = "mediums")
        medium_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        medium_listbox = Listbox(self.frame, selectmode = SINGLE, height = 3)
        medium_listbox.pack(side=TOP, padx = 20)
        medium_listbox.insert(END, "water")
        medium_listbox.insert(END, "oil")
        medium_listbox.insert(END, "ethonol")
        
        
        
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