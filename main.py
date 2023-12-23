import time
from taslaribul import taslari_bul
class Tas:
    def __init__(self, tip, renk=None, deger=None):
        self.tip = tip
        self.renk = renk
        self.deger = deger

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


api_key = "lduRM9gO46HC7HCEGxTj"
project_name = "okeyy"
model_version = 4

while True:
    detected_classes = taslari_bul(api_key, project_name, model_version)
    print(detected_classes)
    taslar = []
    for detected_class in detected_classes:
        if detected_class == "gosterge" or detected_class == "okey":
            taslar.append(Tas(detected_class))
        else:
            renk = detected_class[:1]
            print(f"renk : {renk}")
            if renk in ["K", "S", "T", "M"]:
                deger = int(detected_class[1:])
                print(f"deger : {deger}")
                taslar.append(Tas("normal", renk, deger))

    print("Detected Taslar:", [str(tas) for tas in taslar])

    # Diğer işlemlerinizi yapabilirsiniz.

    time.sleep(10)

def taslar(taslar):
    o_taslari = []
    for i in range(len(taslar)):
        o_taslari.append(str(taslar[i]))
    return o_taslari
def seri_bul(taşlar):
    seri_listesi = []
    for i in range(len(taşlar)):
        for j in range(i + 1, len(taşlar)):
            for k in range(j + 1, len(taşlar)):
                if (
                    taşlar[i].renk == taşlar[j].renk
                    and taşlar[i].renk == taşlar[k].renk
                    and taşlar[i].deger + 1 == taşlar[j].deger
                    and taşlar[j].deger + 1 == taşlar[k].deger
                ):
                    seri_listesi.append([taşlar[i].deger, taşlar[j].deger, taşlar[k].deger])
                    # seri_listesi.append([str(taşlar[i]), str(taşlar[j]), str(taşlar[k])])
    return seri_listesi
def per_bul(taşlar):
    per_listesi = []
    for i in range(len(taşlar)):
        for j in range(i + 1, len(taşlar)):
            for k in range(j + 1, len(taşlar)):
                for l in range(k + 1, len(taşlar)):
                    if (
                        taşlar[i].renk == taşlar[j].renk
                        and taşlar[i].renk == taşlar[k].renk
                        and taşlar[i].renk == taşlar[l].renk
                        and taşlar[i].deger + 1 == taşlar[j].deger
                        and taşlar[j].deger + 1 == taşlar[k].deger
                        and taşlar[k].deger + 1 == taşlar[l].deger
                    ):
                        per_listesi.append([taşlar[i].deger, taşlar[j].deger, taşlar[k].deger, taşlar[l].deger])
                        # per_listesi.append([str(taşlar[i]), str(taşlar[j]), str(taşlar[k]), str(taşlar[l])])

    return per_listesi
def farkli_renk_bul(taşlar):
    farkli_renk_listesi = []
    for i in range(len(taşlar)):
        for j in range(i + 1, len(taşlar)):
            for k in range(j + 1, len(taşlar)):
                if taşlar[i].deger == taşlar[j].deger == taşlar[k].deger and taşlar[i].renk != taşlar[j].renk and taşlar[i].renk != taşlar[k].renk and taşlar[j].renk != taşlar[k].renk:
                    farkli_renk_listesi.append([taşlar[i].deger, taşlar[j].deger, taşlar[k].deger])
                    # farkli_renk_listesi.append([str(taşlar[i]), str(taşlar[j]), str(taşlar[k])]) liste döndürecek gerek olursa

    return farkli_renk_listesi
def el_gücü(taslar):
    güç = 0
    for tas in taslar:
        güç += tas.deger
    return güç
def kombinasyonlari_bul_sayisal(oyuncular):
    for oyuncu_index, oyuncu in enumerate(oyuncular):
        seri_degerleri = seri_bul(oyuncu)
        per_degerleri = per_bul(oyuncu)
        farkli_degerleri = farkli_renk_bul(oyuncu)
        el_gücü_degerleri = el_gücü(oyuncu)
        oo_taslar = taslar(oyuncu)
        seri_toplami = sum(sum(seri) for seri in seri_degerleri)
        per_toplami = sum(sum(per) for per in per_degerleri)
        farkli_toplami = sum(sum(farkli) for farkli in farkli_degerleri)

        print(f"Oyuncu {oyuncular.index(oyuncu)}'nun  taşları: {oo_taslar}")
        print(f"Oyuncu {oyuncu_index}'nun seri kombinasyonlarının toplamı: {seri_toplami}")
        print(f"Oyuncu {oyuncu_index}'nun per kombinasyonlarının toplamı: {per_toplami}")
        print(f"Oyuncu {oyuncu_index}'nun farklı renk kombinasyonlarının toplamı: {farkli_toplami}")
        print(f"Oyuncu {oyuncu_index}'nun el gücünün değeri : {el_gücü_degerleri}")
