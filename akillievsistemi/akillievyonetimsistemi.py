from abc import ABC, abstractmethod

# Kontrol Edilebilir Arayüzü
class KontrolEdilebilir(ABC):
    @abstractmethod
    def ac(self):
        pass

    @abstractmethod
    def kapat(self):
        pass

    @abstractmethod
    def durum(self):
        pass

# Temel Cihaz Sınıfı
class Cihaz(KontrolEdilebilir):
    def __init__(self, isim):
        self.isim = isim
        self._acik = False

    def ac(self):
        self._acik = True
        print(f"{self.isim} açıldı.")

    def kapat(self):
        self._acik = False
        print(f"{self.isim} kapatıldı.")

    def durum(self):
        return self._acik

# Cihaz Sınıfları
class Lamba(Cihaz):
    def __init__(self, isim):
        super().__init__(isim)

    def parlaklik_ayarla(self, seviye):
        if self.durum():
            print(f"{self.isim} parlaklık seviyesi {seviye}% olarak ayarlandı.")
        else:
            print(f"{self.isim} kapalı. Parlaklık ayarlamak için önce açın.")

class Termostat(Cihaz):
    def __init__(self, isim):
        super().__init__(isim)
        self.sicaklik = 22

    def sicaklik_ayarla(self, derece):
        if self.durum():
            self.sicaklik = derece
            print(f"{self.isim} sıcaklığı {derece}°C olarak ayarlandı.")
        else:
            print(f"{self.isim} kapalı. Sıcaklık ayarlamak için önce açın.")

class GuvenlikSistemi(Cihaz):
    def __init__(self, isim):
        super().__init__(isim)

    def alarm_aktif_et(self):
        if self.durum():
            print(f"{self.isim} alarmı aktif edildi!")
        else:
            print(f"{self.isim} kapalı. Alarmı aktif etmek için önce açın.")

# Konsol Uygulaması
def ana_program():
    oturma_odasi_lambasi = Lamba("Oturma Odası Lambası")
    ev_termostati = Termostat("Ev Termostatı")
    guvenlik_sistemi = GuvenlikSistemi("Güvenlik Sistemi")

    cihazlar = [oturma_odasi_lambasi, ev_termostati, guvenlik_sistemi]

    while True:
        print("\nMevcut Cihazlar:")
        for i, cihaz in enumerate(cihazlar, 1):
            durum = "Açık" if cihaz.durum() else "Kapalı"
            print(f"{i}. {cihaz.isim} - {durum}")

        print("\nKomutlar:")
        print("1. Cihazı Aç")
        print("2. Cihazı Kapat")
        print("3. Cihaza Özel İşlem Yap")
        print("4. Çıkış")

        secim = input("\nSeçiminizi yapın: ")

        if secim == "1":
            cihaz_no = int(input("Açmak istediğiniz cihaz numarasını girin: ")) - 1
            cihazlar[cihaz_no].ac()
        elif secim == "2":
            cihaz_no = int(input("Kapatmak istediğiniz cihaz numarasını girin: ")) - 1
            cihazlar[cihaz_no].kapat()
        elif secim == "3":
            cihaz_no = int(input("İşlem yapmak istediğiniz cihaz numarasını girin: ")) - 1
            cihaz = cihazlar[cihaz_no]

            if isinstance(cihaz, Lamba):
                seviye = int(input("Parlaklık seviyesi (0-100): "))
                cihaz.parlaklik_ayarla(seviye)
            elif isinstance(cihaz, Termostat):
                derece = int(input("Sıcaklık değeri: "))
                cihaz.sicaklik_ayarla(derece)
            elif isinstance(cihaz, GuvenlikSistemi):
                cihaz.alarm_aktif_et()
        elif secim == "4":
            print("Programdan çıkılıyor... Hoşçakalın!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    ana_program()
