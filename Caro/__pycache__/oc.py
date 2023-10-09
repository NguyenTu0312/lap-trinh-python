from hcn import *
class oc(Hcn):
    giatri = 0 # giatri la -1 quan co x, giatri la 1 quan co 0
    def __init__(self,nx1,ny1,nx2,ny2):
        super().__init__(nx1,ny1,nx2,ny2)
        self.giatri = 0
    def vehinh(self,cas):
        super().vehinh(cas)
        if self.giatri == 1:
            #ve hinh tron
            cas.create_oval(self.x1,self.y1,self.x2,self.y2)
        if self.giatri == -1:
            #ve duong cheo
            cas.create_line(self.x2,self.y1,self.x1,self.y2)
            cas.create_line(self.x2,self.y1,self.x1,self.y2)