from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna,):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna

    def cetak_ikan(self):
        super().cetak()
        print("Jenis \t\t:", self.jenis, 
        "\nWarna \t\t:", self.warna)

print("====================Ikan Mas====================")
mas = Ikan("Mas", "Serangga", "Air", "Bertelur", "Konsumsi", "Putih")
mas.cetak_ikan()

print("====================Ikan Nila====================")
nila = Ikan("Nila", "Zooplankton", "Air", "Bertelur", "Nirwana", "Kemerahan")
nila.cetak_ikan()

print("====================Ikan Gurame====================")
gurame = Ikan("Gurame", "Pelet", "Air", "Bertelur", "Batu", "Hitam")
gurame.cetak_ikan()