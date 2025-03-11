class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def info_kendaraan(self):
        print(f"Jenis Kendaraan: {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")
    
    def bergerak(self):
        print("Kendaraan sedang bergerak...")

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        self.info_kendaraan()
        print(f"Merk Mobil: {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")
    
    def bunyikan_klakson(self):
        print("Beep beep! Mobil membunyikan klakson.")

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga
    
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        if value > 0:
            self.__tenaga_kuda = value
        else:
            print("Tenaga kuda harus lebih dari 0!")
    
    def get_harga(self):
        return self.__harga
    
    def set_harga(self, value):
        if value > 0:
            self.__harga = value
        else:
            print("Harga harus lebih dari 0!")
    
    def info_mobil_sport(self):
        self.info_mobil()
        print(f"Tenaga Kuda: {self.__tenaga_kuda} HP")
        print(f"Harga: Rp {self.__harga}")
    
    def mode_balap(self):
        print("Mobil Sport masuk ke mode balap!")


mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 700, 6000000000)
mobil_sport.info_mobil_sport()
mobil_sport.bunyikan_klakson()
mobil_sport.mode_balap()


print("Tenaga Kuda sebelum diubah:", mobil_sport.get_tenaga_kuda())
mobil_sport.set_tenaga_kuda(800)
print("Tenaga Kuda setelah diubah:", mobil_sport.get_tenaga_kuda())
