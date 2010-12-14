'''
Created on 14 Dec 2010

@author: nebelriss
'''

from Tkinter import *

class Checkbox(object):
    '''
    classdocs
    '''


    def __init__(self, frame):
        '''
        Constructor
        '''
        #Labels for Listbox
        motor_label = Label(frame, text = "motors")
        motor_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        motor_listbox = Listbox(frame)
        motor_listbox.pack(side=TOP, padx = 20)
        
        # Listbox
        medium_label = Label(frame, text = "mediums")
        medium_label.pack(side = TOP, pady = 20, padx = 20, anchor= W)
        medium_listbox = Listbox(frame)
        medium_listbox.pack(side=TOP, padx = 20)
        
        # Checkbox
        ex_label = Label(frame, text = "Experiments")
        ex_label.pack(side = TOP, pady = 20, padx = 20, anchor = W) 
        for i in range(0,5):
            check = "CheckMe " + str(i)
            checkbox = Checkbutton(frame, text = check)
            checkbox.pack(side = TOP, anchor = W, padx = 20)
                 