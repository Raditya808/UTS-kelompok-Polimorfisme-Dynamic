# ide masing masing perkelompok 
# alva zidan ,ripal , radit 
# V 1 
class pegawai:
    def __init__(self,nama,bagian):
        self.nama = nama
        self.bagian = bagian


    def gaji(self):
        return 0

class manajer(pegawai):
    def __init__(self,nama,bagian,bonus):
        super().__init__(nama,bagian)
        self.bonus = bonus

    def gaji(self):
        gaji_pokok = 300
        return gaji_pokok + self.bonus

class programer(pegawai):
    def __init__(self,nama,bagian,gaji,bonus):
        super().__init__(nama,bagian)
        self.Gaji = gaji
        self.bonus = bonus

    def gaji(self):
        bonus1_projek = 200
        return bonus1_projek * self.bonus

Pegawai_list = [

    manajer("dimas","manajer",300),
    programer("ripal","pr",300,2),
]

for pegawai in Pegawai_list:
    print("="*50)
    print(f"NAMA :{pegawai.nama}")
    print(f"bagian: {pegawai.bagian}")
    print(f"GAJI :{pegawai.gaji()}")
    print(f"bonus / projek :{pegawai.bonus}")
    print("-"*50)