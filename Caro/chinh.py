from tkinter import *
from hcn import *
from banco import *
from oc import *
tk=Tk()
tk.title('CỜ CARO')
cas =Canvas(tk,height = 600,width = 800)
cas.pack()
banco = Banco()
banco.vehinh(cas)
banco.dk = 1 
'''co = Oc(40,40,80,80)
co.giatri  = -1 
co.vehinh(cas)'''
#cas.create_rectangle(10,10,200,100,outline ="black", fill= "green")
#h1= Hcn(50,50,250,150)
def bamoco(event):
    banco.bamoco(cas,event.x, event.y)
#h1.vehinh(cas)
cas.bind_all ('<Button-1>',bamoco ) # hiển thị chỗ ấn vào 
tk.mainloop()

'''def dichchuyen(envent):
    h1.xoahinh (cas)
    if event.keysyn ==  "Up":
        h1.dichlen()
    elif event.keysyn == " Down":
        h1.dichxuong()
    elif event.keysyn == " Left ":
        h1.dichtrai()
    elif event.keysyn == "Right":
        h1.dichphai()
    h1.vehinh(cas)

cas.bind_all('<KeyPress Up',dichchuyen)
cas.bind_all('<KeyPress Doawn',dichchuyen)
cas.bind_all('<KeyPress left',dichchuyen)
cas.bind_all('<KeyPress Right',dichchuyen)'''
