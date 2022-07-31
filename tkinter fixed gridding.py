from tkinter import *

root = Tk()

for i in range(6):
    root.grid_rowconfigure(i,weight=1) # i is the row index
    for j in range(7):
        Button(root,text=f'{4*i+j}th B', width=10).grid(row=i,column=j,sticky='news')
        root.grid_columnconfigure(j,weight=1) # j is column index

root.mainloop()