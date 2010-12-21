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
        self.value_list = []
        self.frame = frame
        
        
        self.canvas = Canvas(frame, bg = "white")
        self.canvas.pack(expand = YES, fill = BOTH)
        
        #Axis
        self.canvas.create_line(self.sw-315, self.sh-150, 50, self.sh-150, fill = "black", width = 1)
        self.canvas.create_line(70, self.sh-130, 70, 70, fill = "black", width = 1)
        
        #Text for Axis
        y = 'Volume (mL)'
        x = 'Time (seconds)'
        self.canvas.create_text(70,40, text= y)
        self.canvas.create_text(self.sw-315,self.sh-120, text= x)
        
        #labeling for axis
        maximumx = 21
        maximumy = 11
        interval = 1
        divisor = 1.7
        self.dist_x = (sh-150)/15 
        self.dist_y = 70/divisor
        
        for i in range(maximumx):
            x = 70 + (i*self.dist_x)
            self.canvas.create_line(x,self.sh-150,x,self.sh-155, width = 2)
            self.canvas.create_text(x,self.sh-140, text='%d'% (20*i), anchor=N)   
        for i in range (maximumy):
            y = self.sh-self.dist_y*(5*divisor)-(200 +(1.5*(5*divisor))) + (i*self.dist_y)   
            self.canvas.create_line(70,y,75,y, width = 2)
            self.canvas.create_text(45,y, text='%d'% (-i*(interval)+(interval*(maximumy-1))), anchor=W)
            
        # y=(5*divisor)-(200 +(1,5*(5*divisor))) divisor=(3.3)
        # divisor=Variable  Rest=constant
        #(-i(2)+(2*20)) 2=Variable  20= range(21)-1
            
    def createline (self, meta, values, idx):
        '''
        
        '''
        self.canvas.delete("plot")
        try:
            self.value_list[idx][1] = None
            self.value_list[idx][2] = None
        except IndexError:
            print "Index Error"
  
        self.value_list[idx][1] = meta
        self.value_list[idx][2] = values
        
        xZeroTotal = 70
        yZeroTotal = self.sh-150

        xScale = 20
        yScale = 1

        
        
        # draw lines
        valuesList = self.value_list
        for row in valuesList:
            meta = row[1]
            values = row[2]
            for row in values:
                endValue = row
                
                xZero = xZeroTotal
                yZero = yZeroTotal
                xPoint = xZero
                yPoint = yZero
                for i in range(3,8):
                    try:
                        vname = 'v' + str(i) + '_desc'
                        yValue = float(meta[vname])
                        xValue = float(endValue[i])
                    except ValueError:
                        break
                        print "ValueError, value is empty"

                    xValue = (xValue / xScale)
                    yValue = (yValue / yScale)
                    
                    xPoint = xPoint + (xValue * self.dist_x)
                    yPoint = yPoint - (yValue * self.dist_y)


                    self.canvas.create_line(xZero, yZero, xPoint, yPoint, fill='red', width = 3, tag = "plot")

                    xZero = xPoint
                    yZero = yPoint

        
    def createlist(self, idx):
        '''
        
        '''
        self.value_list.append([idx])
        self.value_list[idx].append(None)
        self.value_list[idx].append(None)
        