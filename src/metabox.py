#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
import threading 

class Metabox(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self, meta, idx, color):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        root = Tk()
        root.title("Meta Data")
        frame = Frame(root, height = 500)
        frame.pack(side = TOP, expand = YES, fill = BOTH)
        
        
        # groupe members
        name = Label(frame, text = 'Gruppenmitglieder:')
        name.pack(side = TOP, anchor = W)
        name = Label(frame, text = meta[idx]['actor_name'] + "\n")
        name.pack(side = TOP, anchor = W)
        
        # pump description
        name = Label(frame, text = 'Pumpennummer:')
        name.pack(side = TOP, anchor = W)
        name = Label(frame, text = meta[idx]['exp_name'] + "\n")
        name.pack(side = TOP, anchor = W)
        
        # medium description
        name = Label(frame, text = 'Medium:')
        name.pack(side = TOP, anchor = W)
        name = Label(frame, text = meta[idx]['additional_info'] + "\n")
        name.pack(side = TOP, anchor = W)       
        
        # time
        name = Label(frame, text = 'Zeit:')
        name.pack(side = TOP, anchor = W)
        
        # getting time form meta dictionary
        # time will look like this: "201007301022"
        date_meta = meta[idx]['date']
        
        # bringing date and time in a regular format (30.07.2010 10:22)
        date_txt = date_meta[6:8] + "." + date_meta[4:6] + "." + date_meta[:4] + " " + date_meta[8:10] + ":" + date_meta[10:]
        name = Label(frame, text = date_txt + "\n")
        name.pack(side = TOP, anchor = W)  

    
    def run(self):
        mainloop()
        
                
