import datetime

# Başlangıç değerleri
birikim = 0
gecmis = []
urun_fiyatlari = {
    "Yağ": 3,
    "Plastik": 2,
    "Cam": 1,
    "Metal": 5
}

def menu():
    print("\n1- Geri Dönüşüm Ürünü Gir")
    print("2- Ürün Dönüşüm Fiyatı Değiştir")
    print("3- Toplam Birikim")
    print("4- Dönüştürme Geçmişi")
    print("5- Harcama Yap")
    print("6- Çıkış")
    secim = input("Seçiminiz: ")
    return secim

def urun_menu():
    print("\n1- Yağ")
    print("2- Plastik")
    print("3- Cam")
    print("4- Metal")
    print("5- Çıkış")
    secim = input("Seçiminiz: ")
    return secim

while True:
    secim = menu()

    if secim == "1":
        urun_secim = urun_menu()
        if urun_secim == "1":
            urun = "Yağ"
        elif urun_secim == "2":
            urun = "Plastik"
        elif urun_secim == "3":
            urun = "Cam"
        elif urun_secim == "4":
            urun = "Metal"
        elif urun_secim == "5":
            continue
        else:
            print("Geçersiz seçim!")
            continue

        try:
            miktar = float(input(f"{urun} miktarı: "))
            if miktar <= 0:
                print("Geçersiz tutar!")
                continue
        except ValueError:
            print("Geçersiz miktar!")
            continue

        eklenen_para = miktar * urun_fiyatlari[urun]
        birikim += eklenen_para
        tarih = datetime.datetime.now().strftime("%d.%m.%Y")
        gecmis.append((urun, miktar, tarih))
        print("Kayıt yapılmıştır!")

    elif secim == "2":
        print("\nÜrünlerin dönüşüm fiyatları:")
        for k, v in urun_fiyatlari.items():
            print(f"{k}: {v} TL")
        urun_adi = input("Fiyatını değiştirmek istediğiniz ürün adı: ")
        if urun_adi in urun_fiyatlari:
            try:
                yeni_fiyat = float(input("Yeni fiyatı girin: "))
                if yeni_fiyat <= 0:
                    print("Geçersiz tutar!")
                    continue
                urun_fiyatlari[urun_adi] = yeni_fiyat
                print(f"{urun_adi} fiyatı güncellendi!")
            except ValueError:
                print("Geçersiz fiyat!")
        else:
            print("Ürün bulunamadı!")

    elif secim == "3":
        print(f"\nToplam Birikim: {birikim} TL")

    elif secim == "4":
        print("\nDönüştürme Geçmişi:")
        for urun, miktar, tarih in gecmis:
            print(f"{urun}: {miktar} birim - Tarih: {tarih}")

    elif secim == "5":
        try:
            harcama = float(input("Harcama miktarı: "))
            if harcama <= 0:
                print("Geçersiz tutar!")
                continue
            if harcama <= birikim:
                birikim -= harcama
                print(f"{harcama} TL harcandı. Kalan Birikim: {birikim} TL")
            else:
                print("Yetersiz birikim!")
        except ValueError:
            print("Geçersiz harcama miktarı!")

    elif secim == "6":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim!")
