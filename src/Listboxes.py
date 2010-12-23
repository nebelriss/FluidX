#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
from metabox import *



class Listboxes():
    '''
    classdocs
    '''


    def __init__(self, frame, meta, values, idx, plot):
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
        
        
        self.meta_frame = Frame(self.right_frame)
        self.meta_frame.pack(side = TOP, padx = 20, pady = 10)
        self.metabox = Metabox(self.meta_frame, self.meta_height)
        
        spacer = Frame(self.right_frame, bg = "white", height = 5)
        spacer.pack(side = TOP, expand = NO, fill = BOTH)
        
        
        self.values_frame = Frame(self.right_frame)
        self.values_frame.pack(side =TOP, padx = 20, fill = BOTH, expand = NO, pady = 10)
        
        
        # get meta
        meta_tmp = self.meta[self.idx]
        self.canvas_data = self.values[self.idx]
        date_meta = str(meta_tmp['date'])
        motor_meta = str(meta_tmp['exp_name'])
        media_meta = str(meta_tmp['additional_info'])
        self.i += 1
        
        #convert date
        date_txt = date_meta[6:8] + "." + date_meta[4:6] + "." + date_meta[:4] + " " + date_meta[8:10] + ":" + date_meta[10:]
        motor_txt = "Motor: " + motor_meta
        media_txt = "Media: " + media_meta
        # create Labels
        motor_label = Label(self.values_frame, text = motor_txt)
        motor_label.pack(side = TOP, anchor = W)
        
        media_label = Label(self.values_frame, text = media_txt)
        media_label.pack(side = TOP, anchor = W)
        
        date_label = Label(self.values_frame, text = date_txt)
        date_label.pack(side = TOP, anchor = W)
        
        # create Listbox

        self.values_listbox = Listbox(self.values_frame, selectmode = MULTIPLE, height = self.values_height, exportselection=0)
        self.values_listbox.pack(side = TOP, fill = BOTH, expand = YES)
        self.values_listbox.bind("<<ListboxSelect>>", self.sel_values)
        
        self.canvas_data = []
        values_id = 0
        values = self.values[self.idx]
        
        #inserting listboxes
        id = 1
        for i in range(1,4):
            desc = 'v' + str(i) + '_desc'
            box_desc = meta_tmp[desc]
            self.values_listbox.insert(END, str(id) + ". " + box_desc + ' - Sensor')
            id += 1            
            self.values_listbox.insert(END, str(id) + ". " + box_desc + ' - Waage')
            id += 1
            self.values_height += 2
            self.values_listbox.configure(height = self.values_height)

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
  
        self.plot.createline(self.meta, self.canvas_data, self.idx, sel_idx, metabox)
        
    def metabox(self, meta):
        '''
        
        '''
        self.meta_listbox.delete(0, END)
        self.meta_listbox.insert(END, meta)
        