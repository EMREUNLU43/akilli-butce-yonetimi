import matplotlib.pyplot as plt

class VeriGorsellestirme:
    def harcama_grafik(self, giderler):
        kategoriler = list(giderler.keys())
        miktarlar = list(giderler.values())

        plt.figure(figsize=(10, 6))
        plt.bar(kategoriler, miktarlar, color='skyblue')
        plt.title("Aylık Harcamalar")
        plt.xlabel("Kategoriler")
        plt.ylabel("Miktar (TL)")
        plt.show()