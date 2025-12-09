# fix masing masing ide 
class pegawai:
    def __init__(self,nama,bagian):
        self.nama = nama 
        self.bagian = bagian
    def output(self):
        print("Nama anda =",self.nama)
        print("Bagian    =",self.bagian)
        
class manajer(pegawai):
    def __init__(self,nama,bagian,gaji,bonus):
        super().__init__(nama,bagian)
        self.gaji = gaji 
        self.bonus = bonus 
    def output(self):
        super().output()
        print("Gaji  =",self.gaji)
        print("Bonus =",self.bonus)
        print("Total =",self.bonus + self.gaji)
class programmer(pegawai):
    def __init__(self,nama,bagian,gaji,bonus):
        super().__init__(nama,bagian)
        self.gaji = gaji
        self.bonus = bonus
    def output(self):
        super().output()
        print("Gaji    =",self.gaji)
        print("Bonus   =",self.bonus)
        print("Total   =",self.gaji + self.bonus)

# ide (radit tanpa menggunakan pemanggilan for i )
print("-"*50)
tes1 = programmer("radit","programmer",200,10)
tes1.output()
print("-"*50)
tes2 = manajer("dimas","manajer",200,10)
tes2.output()
print("-"*50)
