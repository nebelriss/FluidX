#!/usr/bin/python
# encoding: utf-8

from Tkinter import *

class Metabox(object):
    '''
    classdocs
    '''


    def __init__(self, frame):
        '''
        Constructor
        '''
        self.meta_frame = Frame(self.right_frame)
        self.meta_frame.pack(side = TOP, padx = 20, pady = 10)
        
        
        self.meta_listbox = Listbox(self.meta_frame, selectmode = SINGLE, height = self.meta_height)
        self.meta_listbox.pack(side = TOP, anchor = N)
        
        