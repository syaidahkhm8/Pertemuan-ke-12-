from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun,):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Corak \t\t:", self.corak, 
        "\nRacun \t\t:", self.racun)

print("====================Anaconda====================")
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Bulat hitam", "Tidak Berbisa")
anaconda.cetak_ular()

print("====================Kobra====================")
kobra = Ular("Kobra", "Kambing", "Amazon", "Bertelur", "Gari-Garis", "Berbisa")
kobra.cetak_ular()