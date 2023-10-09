class Hcn:
    x1= 0
    y1 = 0
    x2 = 0
    Y2 =0
    maunen = " white"
    duongvien = " black"
    def __init__(self,x1=0,y1=0,x2=0,y2=0,maunen = "White",duongvien = "black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.maunen = maunen
        self.duongvien = duongvien
    def vehinh (self,cas):
        self.hinh =cas.create_rectangle(self.x1,self.y1,self.x2,self.y2,outline = self.duongvien,fill = self.maunen)
    def xoahinh(self,cas):
        if self.hinh:
            cas.delete(self.hinh)
    def kttronghinh(self,x,y):
        if x > self.x1 and x < self.x2 and y > self.y1 and y <self.y2:
             return 1
        else:
            return 0 
    def dichlen(self):
        self.y1 = self.y1-10
        self.y2 = self.y2 - 10
    def dichxuong(self):
        self.y1 = self.y1+10
        self.y2 = self.y2 + 10
    def dichtrai(self):
        self.x1 = self.x1 - 10
        self.x2 = self.x2 - 10
    def dichphai(self):
        self.x1 = self.x1 + 10
        self.x2 = self.x2 + 10
 