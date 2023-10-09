from oc import *
from hcn import *
class Banco:
    nguoichoi = 1
    thang = 0
    dk = 0 
    arr=[]
     # vi tri tao ban co
    xdau = 30
    ydau = 30
    dai = 30 # độ dài mỗi ô 
    def __init__(self):
        for i in range(0,15): # Tạo ra 15 ô cờ
            line = []
            for j in range ( 0,15):   # chạy vòng lặp qua các cột  
                mx = self.xdau + j * self.dai   #Xn = xdau + n * độ dài
                my = self.ydau + i * self.dai   #Yn = ydau + n * độ dài
                line.append(Oc(mx,my,mx+self.dai , my + self.dai))   # Ô cờ hình vuông + dai
            self.arr.append(line) # line là biến trung gian tạo ra ma trận 2 chiều 
        self.thang = 0
        self.dk = 0
        self.nguoichoi = 1

    def vehinh(self,cas): # Vẽ bàn cờ
        for i in range (0,15):
            for j in range (0,15):
                self.arr[i][j].vehinh(cas)

    def bamoco (self,cas,x,y): # bấm vào ô cờ
        if self.dk == 0:
            return
        for i in range (0,15):
            for j in range (0,15): 
                if self.arr[i][j].giatri == 0 and self.arr[i][j].kttronghinh(x,y)== 1:
                    self.arr[i][j].giatri = self.nguoichoi
                    self.nguoichoi = self.nguoichoi 
                    self.arr[i][j].vehinh(cas) # ve hinh o co da duoc an vao 
                    if self.kiemtrathang(i,j) == 1 :
                        self.dk = 0
                        self.xuatthongbaothang(cas)
                    else :
                        self.nguoichoi = self.nguoichoi * -1 # Đổi chiều người chơi 
                        
                    
    def kiemtrathang(self,mi,mj ):
        if self.ktthang_doc(mi,mj) == 1 or self.ktthang_ngang(mi,mj) == 1 or self.ktthang_cheotrai(mi,mj) == 1 or self.ktthang_cheophai(mi,mj) == 1 :
            return 1
        else:
            return 0
        

    
    def ktthang_cheophai(self,mi,mj):
        dem = 0
        #len tren i giam và j tang
        i = mi - 1
        j = mj + 1
        while (  i >= 0 and j < 15):
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            i = i - 1
            j = j + 1 
    # Xuống dưới i tang j giam 
        i = mi + 1
        j = mj - 1
    
        while (i < 15 and j >= 0):
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            j = j + 1
            i = i - 1 
        if dem >= 4 :
            return 1
        else:
            return 0


    def ktthang_cheotrai (self,mi,mj):
        dem = 0
        #len tren i và j cung giam
        i = mi - 1
        j = mj - 1
        while (  i >= 0 and j >= 0):
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            i = i - 1
            j = j - 1 
    # Xuống dưới i và j cũng tăng 
        i = mi + 1
        j = mj + 1
        if j > 15:
            j = 15 
        while (i < 15 and j < 15):
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            j = j + 1
            i = i + 1 
        if dem >= 4 :
            return 1
        else:
            return 0
            

    def ktthang_ngang(self,mi,mj):
        #kt sang trai j giam , i không đổi
        i = mi 
        j = mj - 1
        dem = 0
        if i < 0:
            i=0
        while i >= 0:
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            j = j - 1 
        #kt sang phai j tang , i ko doi 
        i = mi
        j = mj + 1
        if j > 15:
            j = 15 
        while j < 15:
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            j = j + 1
        if dem >= 4 :
            return 1
        else:
            return 0
            



        
    def ktthang_doc(self,mi,mj):
        i = mi -1
        j = mj 
        dem = 0 
        if i < 0:
            i=0
        while i >= 0:
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            i = i - 1
        #dem xuong duoi
        i = mi + 1
        j = mj
        while i < 15:
            if self.arr[i][j].giatri == self.nguoichoi:
                dem = dem + 1
            else:
                break
            i = i + 1
        if dem >= 4 :
            return 1
        else:
            return 0


     
    def xuatthongbaothang(self,cas):
        str = " người chơi"
        if self.nguoichoi == -1:
            str = str + " x thắng "
        else:
            str = str + " o thắng "
        cas.create_text(100,10,fill = "darkblue" , font = "Times 15 italic bold  ",text = str )

    
        
        


