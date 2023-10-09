from hcn import *
class Oc(Hcn):
    giatri = 0 # giatri la -1 quan co x, giatri la 1 quan co O
    def __init__(self,mx1,my1,mx2,my2):
        super().__init__(mx1,my1,mx2,my2) # Phuong thuc khoi tao của Hcn
        self.giatri = 0
    def vehinh(self,cas):
        #ve hcn
        super().vehinh(cas)
        dx = (self.x2 - self.x1)/4 # độ dài cạnh chia 4
        dy = (self.y2 - self.y1)/4 
        if self.giatri == 1:
            #ve hinh tron
            cas.create_oval(self.x1 +dx ,self.y1 +dy,self.x2 - dx,self.y2 - dy ) 
        if self.giatri == -1:
            #ve duong cheo
            cas.create_line(self.x1 + dx,self.y1 + dy ,self.x2 - dx,self.y2 - dy )
            cas.create_line(self.x2 - dx,self.y1 + dy ,self.x1 + dx,self.y2 - dy)