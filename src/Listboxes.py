#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
from metabox import *
import threading
import random



class Listboxes():
    '''
    classdocs
    '''


    def __init__(self, frame, meta, values, idx, plot, color):
        '''
        Constructor
        '''
        self.right_frame = frame
        self.i = 0
        self.values_height = 1
        self.meta_height = 1
        self.meta = meta
        self.values = values
        self.idx = idx
        self.plot = plot
        self.sel_colors = color
        self.colors = {1: 'red', 2: 'blue', 3: 'yellow', 4: 'cyan', 5: 'moccasin', 6: 'black', 7: 'orange', 8: 'lightblue', 9: 'pink', 10: 'magenta', 11: 'green'}
        
       
        spacer = Frame(self.right_frame, bg = "white", height = 5)
        spacer.pack(side = TOP, expand = NO, fill = BOTH)
        
        
        self.values_frame = Frame(self.right_frame)
        self.values_frame.pack(side =TOP, padx = 20, fill = BOTH, expand = NO, pady = 10)
        
        
        # get meta
        meta_tmp = self.meta[self.idx]
        self.canvas_data = self.values[self.idx]
        motor_meta = str(meta_tmp['exp_name'])
        media_meta = str(meta_tmp['additional_info'])
        self.i += 1
        
        #convert date
        motor_txt = "Pumpe: " + motor_meta
        media_txt = "Media: " + media_meta
        # create Labels
        motor_label = Label(self.values_frame, text = motor_txt)
        motor_label.pack(side = TOP, anchor = W)
        
        media_label = Label(self.values_frame, text = media_txt)
        media_label.pack(side = TOP, anchor = W)
        
        
        # create istbox

        self.values_listbox = Listbox(self.values_frame, selectmode = MULTIPLE, height = self.values_height, exportselection=0)
        self.values_listbox.pack(side = TOP, fill = BOTH, expand = YES)
        self.values_listbox.bind("<<ListboxSelect>>", self.sel_values)
        self.values_listbox.bind("<Button-3>", self.metaview)
        
        self.canvas_data = []
        values = self.values[self.idx]
        
        #inserting listboxes
        id = 1
        self.sel_colors.append([])
        for i in range(1,4):
            desc = 'v' + str(i) + '_desc'
            box_desc = meta_tmp[desc]
            self.values_listbox.insert(END, str(id) + ". " + box_desc + ' - Sensor')
            id += 1
            
            self.values_listbox.insert(END, str(id) + ". " + box_desc + ' - Waage')
            id += 1
            self.values_height += 2
            self.values_listbox.configure(height = self.values_height)
            
        for i in range(8):
            r = random.randrange(1,len(self.colors), 1)
            color = self.colors[r]
            self.sel_colors[self.idx].append(color)


        # wirte infos to List
        data = values
        self.canvas_data.append(data)
        self.plot.createlist(self.idx) 
                
    def sel_values(self, event):
        sel_idx = []
        self.sel_values_list = []
        for i in range(len(self.values_listbox.curselection())):
            sel_values = self.values_listbox.get(self.values_listbox.curselection()[i])
            sel_idx.append(sel_values)

            

            
  
        self.plot.createline(self.meta, self.canvas_data, self.idx, sel_idx, self.sel_colors)
        
    def metaview(self, event):
        '''
        
        '''
        m = Metabox(self.meta, self.idx)
        m.run()
        