from gelir_gider_takibi import GelirGiderTakibi
from butce_onerileri import ButceOnerileri
from veri_gorsellestirme import VeriGorsellestirme
from veri_hazirlama import veri_hazirla
from makine_ogrenmesi import model_egit

def main():
    print("--- Akıllı Bütçe Yönetim Sistemi ---")
    
    # Gelir ve gider takibi
    takip = GelirGiderTakibi()
    takip.gelir_ekle(5000)
    takip.gider_ekle("Gıda", 1000)
    takip.gider_ekle("Ulaşım", 500)
    takip.gider_ekle("Eğlence", 300)
    print("Kalan Bütçe:", takip.kalan_butce())

    # Bütçe önerileri
    butce_onerileri = ButceOnerileri(takip.giderler)
    oneriler = butce_onerileri.oneri_olustur()
    print("Bütçe Önerileri:", oneriler)

    # Veri görselleştirme
    gorsellestirme = VeriGorsellestirme()
    gorsellestirme.harcama_grafik(takip.giderler)

    # Makine öğrenmesi
    X_train, X_test, y_train, y_test = veri_hazirla()
    model = model_egit(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
    