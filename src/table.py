#!/usr/bin/python
# encoding: utf-8


from Tkinter import *

class MessureTable(Frame):#table frame
    def __init__(self, master, lists):
        Frame.__init__(self, master) #Inside Frame for table
        self.lists = []
        for l,w in lists:#Frame for text and list box
            frame = Frame(self) 
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            
                
        #scroll bar
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set

    #define command
    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)
    
    #define insert
    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1
    
    
       
if __name__ == '__main__': #command for name column
    tk = Tk()
    #name table1 + name column
    mlb1 = Label(tk, text='Messreihenauswahl').pack()#name table
    mlb1 = MessureTable(tk, (('Pumpennummer',10), ('GruppenID',10), ('Gruppenname',10), ('Medium',10)))
    mlb1.pack(fill=BOTH,side=TOP)
    #insert data1
    for i in range(5):
        mlb1.insert(END,('Pumpennummer %d'%i, 'GruppenID %d'%i, 'Gruppenname %d'%i, 'Medium %d'%i))            
    for i in range (1):

        #name table2 + name column   
        mlb2 = Label(tk, text='Messwerte').pack()
        mlb2 = MessureTable(tk, (('ID', 10), ('Date',10), ('Gegendruck [kPa]',10), ('Temperatur[C]',10), ('Frequenz[Hz]',10), ('0,5mL',5), ('1mL',5), ('1,5mL',5), ('2mL',5), ('2,5mL',5), ('Fluss[ml/min]',10), ('Strom',10), ('Spannung',10), ('Leistungsaufnahme[mW]',10)))
        mlb2.pack(expand=YES,fill=BOTH,side=BOTTOM)
        #insert data2
        for i in range (100):
            mlb2.insert(END,('ID %d'%i, 'Date %d'%i, 'Gegendruck %d'%i, 'Temperatur %d'%i, 'Frequenz %d'%i, '0,5mL %d'%i, '1mL %d'%i, '1,5mL %d'%i, '2mL %d'%i, '2,5mL %d'%i, 'Fluss %d'%i, 'Strom %d'%i, 'Spannung %d'%i, 'Leistungsaufnahme %d'%i))   
tk.mainloop()
                
