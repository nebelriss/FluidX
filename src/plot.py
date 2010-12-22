'''
Created on 14 Dec 2010

@author: nebelriss
'''
from Tkinter import *
from Canvas import *
from math import *

class Plot(object):
    
    def __init__(self, master, frame, sw, sh):
        '''
        
        '''
        self.sw = sw
        self.sh = sh
        self.value_list = []
        self.frame = frame
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
        y = 'Volume (mL)'
        x = 'Time (seconds)'
        self.canvas.create_text(70,40, text= y, tag = "text")
        self.canvas.create_text(self.sw-315,self.sh-120, text= x, tag = "text")
        
        #labeling for axis
      
        maximumx = ((self.xMax) + 1) / self.xInterval
        maximumy = ((self.yMax) + 1) / self.yInterval

        
        print "dist................................"
        print self.dist_x
        print self.dist_y
        
        for i in range(int(maximumx)):
            x = 70 + (i * self.dist_x * self.xInterval)
            self.canvas.create_line(x,self.sh-150,x,self.sh-155, width = 2)
            self.canvas.create_text(x,self.sh-140, text='%d'% (i * self.xInterval), anchor=N, tag = "text")   
        for i in range (int(maximumy)):
            y = self.sh-150-(i * self.dist_y * self.yInterval)   
            self.canvas.create_line(70,y,75,y, width = 2)
            self.canvas.create_text(45,y, text=str((i * self.yInterval)), anchor=W, tag = "text")
            
        # y=(5*divisor)-(200 +(1,5*(5*divisor))) divisor=(3.3)
        # divisor=Variable  Rest=constant
        #(-i(2)+(2*20)) 2=Variable  20= range(21)-1
            
    def createline (self, meta, values, idx, sel_idx):
        '''
        
        '''
        self.xInterval = 2
        self.yInterval = 0.2 
        
        print sel_idx
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
                    print "this is index"
                    for row in endValue:
                        if item == '1':
                            xValue = row[1]
                            yValue = row[6]                            
                        elif item == '2':
                            xValue = row[1]
                            yValue = row[7]
                        elif item == '3':
                            xValue = row[2]
                            yValue = row[6]
                        elif item == '4':
                            xValue = row[2]
                            yValue = row[7] 
                        elif item == '5':
                            xValue = row[3]
                            yValue = row[6]
                        elif item == '6':
                            xValue = row[3]
                            yValue = row[7]                                                                                                                                        
                        else:
                            print "none haha"

                        #xValue = xValue / self.xInterval/ 2
                        #yValue = yValue / self.yInterval / 20
                        xPoint = (xPoint + (xValue * self.dist_x) / self.xInterval) + 70
                        yPoint = (yPoint + (yValue * self.dist_y) / self.yInterval) - 150


                        self.canvas.create_line(xZero, yZero, xPoint, yPoint, fill='red', width = 3, tag = "plot")

                        xZero = xPoint
                        yZero = yPoint



        
    def createlist(self, idx):
        '''
        
        '''
        print "this is " 
        print idx
        self.value_list.append([idx])
        self.value_list[idx].append(None)
        self.value_list[idx].append(None)
        
    def getMax(self, value_list):
        '''
        
        '''
        self.xMax = 0
        self.yMax = 0
        changed = False
                        
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
                            changed = True
                    for i in range(6,7):
                        if self.yMax < row[i]:
                            self.yMax = row[i]
                            changed = True
                        if changed:
                            print self.xMax
                            print self.yMax
            
        self.dist_x = (self.sw - 400) / self.xMax
        print self.dist_x
        self.dist_y = (self.sh - 500) / self.yMax 
        print self.dist_y        
        self.createGrid()
        
