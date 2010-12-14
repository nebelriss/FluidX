'''
Created on 14 Dec 2010

@author: nebelriss
'''
from Tkinter import *
from Canvas import *

class Plot(object):
    
    def __init__(self, master, frame, sw, sh):
        '''
        
        '''
        self.sw = sw
        self.sh = sh
        print sw
        print sh
        
        self.canvas = Canvas(frame, bg = "white")
        self.canvas.pack(expand = YES, fill = BOTH)
        
        self.canvas.create_line(self.sw-315, self.sh-150, 50, self.sh-150, fill = "black", width = 3)
        self.canvas.create_line(70, self.sh-130, 70, 70, fill = "black", width = 3)
        