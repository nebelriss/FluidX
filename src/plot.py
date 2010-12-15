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

        
        self.canvas = Canvas(frame, bg = "white")
        self.canvas.pack(expand = YES, fill = BOTH)
        
        self.canvas.create_line(self.sw-315, self.sh-150, 50, self.sh-150, fill = "black", width = 1)
        self.canvas.create_line(70, self.sh-130, 70, 70, fill = "black", width = 1)
        
        #Kennzeichnung der Achsenlinien
        y = 'Temperatur'
        x = 'Zeit'
        self.canvas.create_text(70,40, text= y)
        self.canvas.create_text(self.sw-315,self.sh-130, text= x)
        
        #Beschriftung der Achsenlinien
        for i in range(12):
            x = 70 + (i*40)
            self.canvas.create_line(x,self.sh-150,x,self.sh-155, width = 2)
            self.canvas.create_text(x,self.sh-140, text='%d'% (20*i), anchor=N)   
        for i in range (12):
            y = 71 + (i*39)   
            self.canvas.create_line(self.sw-1010,y,self.sw-1005,y, width = 2)
            self.canvas.create_text(self.sw-1025,y, text='%d'% (-i+11), anchor=W)
                    