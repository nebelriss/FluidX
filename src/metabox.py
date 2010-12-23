#!/usr/bin/python
# encoding: utf-8

from Tkinter import *

class Metabox(object):
    '''
    classdocs
    '''


    def __init__(self, frame, meta_height):
        '''
        Constructor
        '''
        
        # new frame for the metabox

        
        title = Label(frame, text = "Your Selection")
        title.pack(side = TOP, anchor = W)
        
        desc = Label(frame, text = "click to sel color")
        desc.pack(side = TOP, anchor = W)
        
        self.meta_listbox = Listbox(frame, selectmode = SINGLE, height = meta_height)
        self.meta_listbox.pack(side = TOP, anchor = NW)
        
    def insert(self, meta_data):
        '''
        
        '''
        # delete all entrys
        self.meta_listbox.delete(0, END)
        
        # write new entrys to the list
        for item in meta_data:
            print item
            self.meta_listbox.insert(item)
        
        
    def getcolor(self):
        '''
        
        '''
        