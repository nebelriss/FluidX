'''
Created on 14 Dec 2010

@author: nebelriss
'''
from Tkinter import *
from Canvas import *
import random

class Plot(object):
    
    def __init__(self, master, frame, sw, sh):
        '''
        
        '''
        self.sw = sw
        self.sh = sh
        self.value_list = []
        self.frame = frame
        self.meta_frame = Frame(self.frame)
        self.meta_frame.pack(sid = TOP)        
        self.canvas = Canvas(self.frame, bg = "white")
        self.canvas.pack(expand = YES, fill = BOTH)
        
        


        #self.createGrid(0,0)
        
    def createGrid(self):
        '''
        
        '''
        # delete all text
        self.canvas.delete("text")                
        
        #Axis
        self.canvas.create_line(self.sw-315, self.sh-150, 50, self.sh-150, fill = "black", width = 1)
        self.canvas.create_line(70, self.sh-130, 70, 70, fill = "black", width = 1)
        
        #Text for Axis
        y = 'Y-Axis'
        x = 'X-Axis'
        self.canvas.create_text(70,40, text= y, tag = "text")
        self.canvas.create_text(self.sw-315,self.sh-120, text= x, tag = "text")
        
        #labels for axis
      
        maximumx = ((self.xMax) + 2) / self.xInterval
        maximumy = ((self.yMax) + 1) / self.yInterval
        
        for i in range(int(maximumx)):
            x = 70 + (i * self.dist_x * self.xInterval)
            self.canvas.create_line(x,self.sh-150,x,self.sh-155, width = 2)
            self.canvas.create_text(x,self.sh-140, text='%d'% (i * self.xInterval), anchor=N, tag = "text")   
        for i in range (int(maximumy)):
            y = self.sh-150-(i * self.dist_y * self.yInterval)   
            self.canvas.create_line(70,y,75,y, width = 2)
            self.canvas.create_text(45,y, text=str((i * self.yInterval)), anchor=W, tag = "text")
        
        # Two weeks work for nothing
          
        # y=(5*divisor)-(200 +(1,5*(5*divisor))) divisor=(3.3)
        # divisor=Variable  Rest=constant
        #(-i(2)+(2*20)) 2=Variable  20= range(21)-1
            
    def createline (self, meta, values, idx, sel_idx, colors):
        '''
        Fist the given values are written in a list with the index number of the listbox and the selected items.
        '''
        self.xInterval = 2
        self.yInterval = 0.2

        
        self.canvas.delete("plot")
        try:
            self.value_list[idx][1] = None
            print self.value_list
        except IndexError:
            print "Index Error"
  

        self.value_list[idx][1] = values
        self.value_list[idx][2] = sel_idx
        print self.value_list
        xZeroTotal = 70
        yZeroTotal = self.sh-150

        self.getMax(self.value_list)

        
        
        # draw lines  
        for row in self.value_list:
            values = row[1]
            for item in row[2]:

                for row in values:
                    endValue = row

                    xZero = xZeroTotal
                    yZero = yZeroTotal
                    xPoint = xZero
                    yPoint = yZero                    

                    
                    # write xValue an yValue for the right selection
                    for row in endValue:
                        if item[0] == '1':
                            xValue = row[0]
                            yValue = row[6] 
                        elif item[0] == '2':
                            xValue = row[0]
                            yValue = row[7]
                        elif item[0] == '3':
                            xValue = row[1]
                            yValue = row[6]
                        elif item[0] == '4':
                            xValue = row[1]
                            yValue = row[7] 
                        elif item[0] == '5':
                            xValue = row[2]
                            yValue = row[6]
                        elif item[0] == '6':
                            xValue = row[2]
                            yValue = row[7]                                                                                                                                        
                        else:
                            pass
                        
                        #send item to metabox
                        print colors
                        color = colors[idx][int(item[0]) - 1]
                        xPoint = (xValue * self.dist_x) + 70
                        yPoint = self.sh - ((yValue * self.dist_y) + 150)
                        

                        self.canvas.create_line(xZero, yZero, xPoint, yPoint, fill=color, width = 3, tag = "plot")
                        self.canvas.create_oval(xPoint - 4, yPoint - 4, xPoint + 4, yPoint + 4, fill = color, outline = color, tag = "plot")

                        xZero = xPoint
                        yZero = yPoint
                    
                    
        


        
    def createlist(self, idx):
        '''
        
        '''
        self.value_list.append([idx])
        self.value_list[idx].append(None)
        self.value_list[idx].append(None)
        


        
        
        
    def getMax(self, value_list):
        '''
        This method is trying to find the max value for the scale grid.
        '''
        self.xMax = 0
        self.yMax = 0

                        
        # get values
        for row in value_list:
            values = row[1]
            for row in values:
                endValue = row
                for row in endValue:                                                  
                    for i in range(1,3):
        
                        # check for max value                
                        if self.xMax < row[i]:
                            self.xMax = row[i]

                    for i in range(6,7):
                        if self.yMax < row[i]:
                            self.yMax = row[i]


            
        self.dist_x = (self.sw - 400) / self.xMax
        self.dist_y = (self.sh - 500) / self.yMax       
        self.createGrid()     
