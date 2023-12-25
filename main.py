import time
from taslaribul import taslari_bul
from kombinasyonlar import seri_bul, farkli_renk_bul, per_bul, el_gucu, cift_tas_bul, okey_bul, gosterge_bul
class Tas:
    def __init__(self, tip, renk=None, deger=None):
        self.tip = tip
        self.renk = renk
        self.deger = deger if deger is not None else 0

    def __str__(self):
        if self.tip == "normal":
            return f"{self.renk} {self.deger}"
        else:
            return f"{self.tip}"

    def __eq__(self, other):
        if self.tip == other.tip == "normal":
            return self.renk == other.renk and self.deger == other.deger
        else:
            return self.tip == other.tip

    def __hash__(self):
        if self.tip == "normal":
            return hash((self.renk, self.deger))
        else:
            return hash((self.tip,))


def kombinasyonlari_bul_sayisal(taslar):
    seri_degerleri = seri_bul(taslar)
    per_degerleri = per_bul(taslar)
    farkli_degerleri = farkli_renk_bul(taslar)
    el_gucu_degerleri = el_gucu(taslar)
    ciftler = cift_tas_bul(taslar)
    okey = okey_bul(taslar)
    gosterge = gosterge_bul(taslar)

    seri_toplami = sum(sum(seri) for seri in seri_degerleri)
    per_toplami = sum(sum(per) for per in per_degerleri)
    farkli_toplami = sum(sum(farkli) for farkli in farkli_degerleri)
    cift_sayisi = ciftler
    okey_sayisi = okey
    gosterge_sayisi = gosterge
    elin_toplami = seri_toplami + per_toplami + farkli_toplami

    print(f"Oyuncunun El Gücü: {elin_toplami}")
    print(f"Oyuncunun gösterge sayısı: {gosterge_sayisi}")
    print(f"Oyuncunun Okey sayısı: {okey_sayisi}")
    print(f"Oyuncunun çift kombinasyonlarinin toplami: {cift_sayisi}")
    print(f"Oyuncunun seri kombinasyonlarinin toplami: {seri_toplami}")
    print(f"Oyuncunun per kombinasyonlarinin toplami: {per_toplami}")
    print(f"Oyuncunun farkli renk kombinasyonlarinin toplami: {farkli_toplami}")
    print(f"Oyuncunun el gucunun degeri : {el_gucu_degerleri}")

def taslari_isle(api_key, project_name, model_version):
    detected_classes = taslari_bul(api_key, project_name, model_version)
    print(detected_classes)
    taslar = []
    for detected_class in detected_classes:
        if detected_class == "gosterge" or detected_class == "okey":
            taslar.append(Tas(detected_class))
        else:
            renk = detected_class[:1]
            if renk in ["K", "S", "T", "M"]:
                deger = int(detected_class[1:])
                taslar.append(Tas("normal", renk, deger))

    print("Detected Taslar:", [str(tas) for tas in taslar])
    kombinasyonlari_bul_sayisal(taslar)

def main():
    api_key = "lduRM9gO46HC7HCEGxTj"
    project_name = "okeyy"
    model_version = 4

    while True:
        taslari_isle(api_key, project_name, model_version)
        time.sleep(10)

if __name__ == "__main__":
    main()


""" DOSYAYA YAZMA
    with open("kombinasyonlar.txt", "a") as dosya:
        dosya.write(f"Seri Toplamı: {seri_toplami}\n")
        dosya.write(f"Per Toplamı: {per_toplami}\n")
        dosya.write(f"Farklı Renk Toplamı: {farkli_toplami}\n")
        dosya.write(f"Çift Sayısı: {cift_sayisi}\n")
        dosya.write(f"Okey Sayısı: {okey_sayisi}\n")
        dosya.write(f"Gösterge Sayısı: {gosterge_sayisi}\n")
        dosya.write(f"El Gücü: {elin_toplami}\n")
        dosya.write("\n")
"""