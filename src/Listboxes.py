#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
import threading


class Listboxes(threading.Thread):
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
        threading.Thread.__init__(self)
        self.meta = meta
        self.values = values
        self.idx = idx
        self.plot = plot

        values_frame = Frame(self.right_frame)
        values_frame.pack(side =TOP, padx = 20, fill = BOTH, expand = NO, pady = 10)
        
        # get meta
        meta_tmp = self.meta[self.idx]
        date_meta = str(meta_tmp['date'])
        motor_meta = str(meta_tmp['exp_name'])
        media_meta = str(meta_tmp['additional_info'])
        self.i += 1
        
        #convert date
        date_txt = date_meta[6:8] + "." + date_meta[4:6] + "." + date_meta[:4] + " " + date_meta[8:10] + ":" + date_meta[10:]
        motor_txt = "Motorrrrrrrrr: " + motor_meta
        media_txt = "Media: " + media_meta
        # create Labels
        motor_label = Label(values_frame, text = motor_txt)
        motor_label.pack(side = TOP, anchor = W)
        
        media_label = Label(values_frame, text = media_txt)
        media_label.pack(side = TOP, anchor = W)
        
        date_label = Label(values_frame, text = date_txt)
        date_label.pack(side = TOP, anchor = W)
        
        # create Listbox

        self.values_listbox = Listbox(values_frame, selectmode = MULTIPLE, height = self.values_height, exportselection=0)
        self.values_listbox.pack(side = TOP, fill = BOTH, expand = YES)
        self.values_listbox.bind("<<ListboxSelect>>", self.sel_values)
        
        self.canvas_data = []
        values_id = 0
        values = self.values[self.idx]
        print self.idx
        for row in values:
            values_id += 1
            box_name = str(values_id) + ":  " + str(row[2]) + "/" + str(row[1]) + "/" + str(row[3])
            self.values_listbox.insert(END, str(box_name))
            self.values_listbox.configure(height = self.values_height)
            self.values_height += 1
            # wirte infos to List
            self.canvas_data.append([meta_tmp, row])

            
                
    def sel_values(self, event):
        self.sel_values_list = []
        for i in range(len(self.values_listbox.curselection())):
            sel_values = self.values_listbox.get(self.values_listbox.curselection()[i])
            sel_nr = sel_values[0]
            row = self.canvas_data[int(sel_nr)]
            self.meta = row[0]
            values = row[1]
            self.sel_values_list.append(values)
            
        self.plot.createline(self.sel_values_list)
            
    

                
