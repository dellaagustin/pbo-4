class abcd:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def printname(self):
        print(self.panjang)
        print(self.lebar)
        print(self.tinggi)
class volbalok(abcd):
    def __init__(self, panjang, lebar, tinggi):
        abcd.__init__(self, panjang, lebar, tinggi)
        self.vbalok = panjang * lebar * tinggi
    def volume(self):
        print("Panjang              : ", self.panjang)
        print("Lebar                : ", self.lebar)
        print("Tinggi               : ", self.tinggi)
        print("Volume balok         : ", self.vbalok)

class lpbalok(abcd):
    def __init__(self, panjang, lebar, tinggi):
        abcd.__init__(self, panjang, lebar, tinggi)
        self.luaspermukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (tinggi * lebar))
    def lp(self):
        print("Panjang              : ", self.panjang)
        print("Lebar                : ", self.lebar)
        print("Tinggi               : ", self.tinggi)
        print("Luas permukaan balok : ", self.luaspermukaan)
           
x = volbalok (4, 2, 3)
y = lpbalok (4, 2, 5)

print("==========================")
x.volume()
print("==========================")
y.lp()
print("==========================")