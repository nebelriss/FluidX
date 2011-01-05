#!/usr/bin/python
# encoding: utf-8

from Tkinter import *
from Canvas import *
import random
import os

class Plot(object):
    '''
    A canvas will be created where the selected values will be plotted as lines, with the best fitting scale.
    
    Initial version by:
        Michel Heiniger and Sandra Lang
    
    Latest source code can be found at:
        https://github.com/nebelriss/FluidX
    '''
    
    
    def __init__(self, master, frame, sw, sh):
        '''
        Constructor for the plot area.
        '''
        # initialization of 
        self.sw = sw
        self.sh = sh
        self.frame = frame
        
        # empty value list
        self.value_list = []
        
        # canvas area where the value lines and the coordinate system
        self.canvas = Canvas(self.frame, bg = "white")
        self.canvas.pack(expand = YES, fill = BOTH)
        
        #if the used os is a windows or a mac, they need a factor 1.5 for the y-axis
        if os.name == "nt":
            self.win_osx_factor = 1.5
        elif os.name == "mac":
            self.win_osx_factor = 1.5
            
        # if its a linux machine factor is 1           
        else:
            self.win_osx_factor = 1
        
        
        
    def createCoordSystem(self):
        '''
        This creates the coordinate system with a given max value for x,y axis.
        '''
        # Interval for the numbers 
        self.xInterval = 2
        self.yInterval = 0.2
        
        
        # delete all canvas with the tag "text"
        self.canvas.delete("text")                
        
        
        # draw axis lines
        self.canvas.create_line(self.sw-315, self.sh-150, 50, self.sh-150, fill = "black", width = 1)
        self.canvas.create_line(70, self.sh-130, 70, 70, fill = "black", width = 1)
        
        
        # text for Axis
        y = 'Y-Axis'
        x = 'X-Axis'
        # write the text at the right position
        self.canvas.create_text(70,40, text= y, tag = "text")
        self.canvas.create_text(self.sw-315,self.sh-120, text= x, tag = "text")
        
        
        # numbers for x and y axis
        maximumx = ((self.xMax) + 2) / self.xInterval
        maximumy = ((self.yMax) + 1) / self.yInterval
        
        
        # loop to write the numbers under the axis line and draw the separation lines for the x-axis
        for i in range(int(maximumx)):
            x = 70 + (i * self.dist_x * self.xInterval)
            self.canvas.create_line(x,self.sh-150,x,self.sh-155, width = 2)
            self.canvas.create_text(x,self.sh-140, text='%d'% (i * self.xInterval), anchor=N, tag = "text")   
        
        # loop to write the numbers under the axis line and draw the separation lines for the x-axis      
        for i in range (int(maximumy)):
            y = self.sh-150-(i * self.dist_y * self.yInterval) * self.win_osx_factor  
            self.canvas.create_line(70,y,75,y, width = 2)
            self.canvas.create_text(45,y, text=str((i * self.yInterval)), anchor=W, tag = "text")
        
        
            
    def createline (self, meta, values, idx, sel_idx, colors):
        '''
        Fist the given values are written in a list with the index number of the listbox and the selected items.
        '''
        # remove all lines with the tag "plot"
        self.canvas.delete("plot")
        
        
        # overwrite values with the given index with none
        try:
            self.value_list[idx][1] = None
        except IndexError:
            print "Index Error - List out of range"
  

        # write values in the list
        self.value_list[idx][1] = values
        self.value_list[idx][2] = sel_idx
        
        
        # The zero-point in the coordinate system
        xZeroTotal = 70
        yZeroTotal = self.sh-150
        
        # get the max value
        self.getMax(self.value_list)
        
           
        # draw lines with the selected values
        # read every row of the value_list
        for row in self.value_list:
            # write row to a different variable because I had to build a for loop like this (for row in row:)
            values = row[1]
            
            # get the value with the index 2 in each row
            for item in row[2]:

                for row in values:
                    endValue = row
                    
                    # setting zeroTotal to zero
                    xZero = xZeroTotal
                    yZero = yZeroTotal
                    # setting point to zero for the reason the line begins at the zero point
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
                        
                        # setting color for the line
                        color = colors[idx][int(item[0]) - 1]
                        
                        # calculating x,y points on the screen
                        xPoint = (xValue * self.dist_x) + 70
                        yPoint = self.sh - ((yValue * self.dist_y) + 150) * self.win_osx_factor
                        
                        # drawing line
                        self.canvas.create_line(xZero, yZero, xPoint, yPoint, fill=color, width = 3, tag = "plot")

                        self.canvas.create_oval(xPoint - 4, yPoint - 4, xPoint + 4, yPoint + 4, fill = color, outline = color, tag = "plot")
                        
                        # setting x,y points as new zero points
                        xZero = xPoint
                        yZero = yPoint
                        

        
    def createlist(self, idx):
        '''
        adding new index to the list with two empty fields
        '''
        self.value_list.append([idx])
        self.value_list[idx].append(None)
        self.value_list[idx].append(None)
        


        
        
        
    def getMax(self, value_list):
        '''
        This method is trying to find the max value for the scale grid.
        '''
        # setting max values to zero to find out the highest value
        self.xMax = 0
        self.yMax = 0

                        
        # get values
        for row in value_list:
            values = row[1]
            for row in values:
                endValue = row
                for row in endValue: 
                    
                    # check for max value in the x-axis                                                 
                    for i in range(1,3):
                        if self.xMax < row[i]:
                            self.xMax = row[i]
                    
                    # check for max value in the y-axis
                    for i in range(6,7):
                        if self.yMax < row[i]:
                            self.yMax = row[i]


        # calculating the distance between     
        self.dist_x = (self.sw - 400) / self.xMax
        self.dist_y = (self.sh - 500) / self.yMax       
        self.createCoordSystem()
        