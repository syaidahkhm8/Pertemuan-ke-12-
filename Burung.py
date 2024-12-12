from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi,):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t:", self.jenis, 
        "\nBunyi \t\t:", self.bunyi)

print("====================Merpati====================")
merpati = Burung("Merpati", "Biji-bijian", "Darat", "Bertelur", "Karang", "Chirpchirp")
merpati.cetak_burung()

print("====================Elang====================")
elang = Burung("Elang", "Ikan", "Darat", "Bertelur", "Tiram", "cikkkkk")
elang.cetak_burung()

print("====================Kowak====================")
kowak = Burung("Kowak", "Serangga","Sungai","Bertelur","Burung Malam","kwakwakwak")
kowak.cetak_burung()