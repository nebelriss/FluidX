#!/usr/bin/python
# encoding: utf-8


from Tkinter import *
import Import_ui

def importer():
    print shit

def mainWindow(root):
    '''
    
    '''
    # Frames
    top_frame = Frame(root, height = 65, bg = 'white')
    main_frame = Frame(root)
    plot_frame = Frame(main_frame, bg = 'blue')
    right_frame = Frame(main_frame, width = 250, bg = 'red')
    # Frames pack
    top_frame.pack(side = TOP, fill = BOTH, expand = NO)
    main_frame.pack(fill = BOTH, expand = YES)
    plot_frame.pack(side = LEFT, fill = BOTH, expand = YES)
    right_frame.pack(side = RIGHT, fill = BOTH, expand = NO)
    
    
    # Buttons are temporary until they get pics inside etc
    # Buttons in the top_frame
    button_open = Button(top_frame, text = 'Open', height = 3, width = 7)
    button_import = Button(top_frame, text = 'Import', height = 3, width = 7, command = importer)
    button_table = Button(top_frame, text = 'Table', height = 3, width = 7)
    button_exit = Button(top_frame, text = 'Exit', height = 3, width = 7)
    # Button packers
    button_open.pack(side = LEFT) 
    button_import.pack(side = LEFT) 
    button_table.pack(side = LEFT)
    button_exit.pack(side = RIGHT)
    
    
    


root = Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (sw, sh))
mainWindow(root)
root.mainloop()