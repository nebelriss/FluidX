#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
from data import *


class Rightpanel(object):
    '''
    classdocs
    '''


    def __init__(self, frame):
        '''
        Constructor
        '''
        # load data
        d = Data()
        values, meta = d.getdata()
        
        #Labels for Listbox
        motor_label = Label(frame, text = "motors")
        motor_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        motor_listbox = Listbox(frame, selectmode = SINGLE, height = 4)
        motor_listbox.pack(side=TOP, padx = 20)
        motor_listbox.insert(END, "series_nr 1")
        motor_listbox.insert(END, "series_nr 2")
        motor_listbox.insert(END, "series_nr 3")
        
        # Listbox
        medium_label = Label(frame, text = "mediums")
        medium_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        medium_listbox = Listbox(frame, selectmode = SINGLE, height = 3)
        medium_listbox.pack(side=TOP, padx = 20)
        medium_listbox.insert(END, "water")
        medium_listbox.insert(END, "oil")
        medium_listbox.insert(END, "ethonol")
        
        # Checkbox
        ex_label = Label(frame, text = "Experiments")
        ex_label.pack(side = TOP, pady = 20, padx = 20, anchor = W) 
        for i in range(0,5):
            check = "CheckMe " + str(i)
            checkbox = Checkbutton(frame, text = check)
            checkbox.pack(side = TOP, anchor = W, padx = 20)