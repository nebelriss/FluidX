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
        #Axis
        self.canvas.create_line(self.sw-315, self.sh-150, 50, self.sh-150, fill = "black", width = 1)
        self.canvas.create_line(70, self.sh-130, 70, 70, fill = "black", width = 1)
        
        #Text for Axis
        y = 'Temperatur'
        x = 'Zeit'
        self.canvas.create_text(70,40, text= y)
        self.canvas.create_text(self.sw-315,self.sh-130, text= x)
        
        #labeling for axis
        self.dist_x = (sh-150)/15 
        self.dist_y = 70/3.3
        for i in range(21):
            x = 70 + (i*self.dist_x)
            self.canvas.create_line(x,self.sh-150,x,self.sh-155, width = 2)
            self.canvas.create_text(x,self.sh-140, text='%d'% (20*i), anchor=N)   
        for i in range (21):
            y = self.sh-self.dist_y*16.5-224.75 + (i*self.dist_y)   
            self.canvas.create_line(70,y,75,y, width = 2)
            self.canvas.create_text(45,y, text='%d'% (-i*(5)+(5*20)), anchor=W)
            
        # y=(5*divisor)-(200 +(1,5*(5*divisor))) divisor=(3.3)
        # divisor=Variable  Rest=constant
        #(-i(2)+(2*20)) 2=Variable  20= range(21)-1
            
    def createCanvas (self,meta,values):
        '''
        
        '''