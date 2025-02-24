class GelirGiderTakibi:
    def __init__(self):
        self.gelir = 0
        self.giderler = {}

    def gelir_ekle(self, miktar):
        self.gelir += miktar

    def gider_ekle(self, kategori, miktar):
        if kategori in self.giderler:
            self.giderler[kategori] += miktar
        else:
            self.giderler[kategori] = miktar

    def kalan_butce(self):
        toplam_gider = sum(self.giderler.values())
        return self.gelir - toplam_gider