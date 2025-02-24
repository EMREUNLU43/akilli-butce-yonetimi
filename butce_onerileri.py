class ButceOnerileri:
    def __init__(self, giderler):
        self.giderler = giderler

    def oneri_olustur(self):
        toplam_gider = sum(self.giderler.values())
        oneriler = {}

        for kategori, miktar in self.giderler.items():
            if miktar > toplam_gider * 0.3:  # Harcama %30'dan fazla ise
                oneriler[kategori] = "Harcamalarınızı azaltmayı düşünün."
            else:
                oneriler[kategori] = "Harcamalarınız makul seviyede."

        return oneriler