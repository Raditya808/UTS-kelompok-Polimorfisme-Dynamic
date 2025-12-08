# versi kelompok 
# alfa , zidan ,ripal, radit
# V 2


class pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class manajer:
    def __init__(self, nama, bonus_tunjangan):
        self.nama = nama
        self.bonus = bonus_tunjangan
        self.gaji_pokok = 200


    def tampil(self):
        print("===== GAJI MANAJER =====")
        print("nama manajer    : ", self.nama)
        print("bonus tunjangan : ", self.bonus)
        print("gaji pokok      : ", self.gaji_pokok)
        print("total gaji      : ", self.gaji_pokok + self.bonus)
        return  self.gaji_pokok + self.bonus

class programer:
    def __init__(self,nama,bonus_projek):
        self.nama = nama
        self.projek = bonus_projek
        self.gaji_pokok = 20



    def tampil(self):
        print("="*50)
        print("===== GAJI PROGAMER =====")
        print("nama progamer   : ",self.nama)
        print("jumlah projek   : ",self.projek)
        print("gaji pokok      : ",self.gaji_pokok)
        print("total gaji      : ",self.gaji_pokok * self.projek)
        return self.gaji_pokok* self.projek

pegawai_list = [
    manajer("ivan",9),
    programer("ripal",2)

]

for pegawai in pegawai_list:
    pegawai.tampil()