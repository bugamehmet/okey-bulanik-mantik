import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from skfuzzy import control as ctrl

def bulanik_hesap(seri_sayisi, per_sayisi, farkli_renk_sayisi, cift_sayisi, gosterge_sayisi, okey_sayisi, el_ham_gucu_sayisi, el_gucu_sayisi):

    seri = ctrl.Antecedent(np.arange(0, 216, 1), "S")
    per = ctrl.Antecedent(np.arange(0, 230, 1), "P")
    farkli_renk = ctrl.Antecedent(np.arange(0, 186, 1), "FR")
    cift_tas = ctrl.Antecedent(np.arange(0, 10, 0.2), "ÇT")
    gosterge = ctrl.Antecedent(np.arange(0, 2, 0.01), "G")
    okey = ctrl.Antecedent(np.arange(0, 2, 0.01), "O")
    el_ham_guc = ctrl.Antecedent(np.arange(0, 234, 1), "EHG")
    el_gucu = ctrl.Antecedent(np.arange(0, 211, 1), "EG")

    kazanma_orani = ctrl.Consequent(np.arange(0, 101, 10), "KO")


    # Seri Taşların Üyelik Fonksiyonları
    seri["A"] = fuzz.trimf(seri.universe, [0, 0, 36])
    seri["O"] = fuzz.trimf(seri.universe, [18, 105.75, 193.5])
    seri["Ç"] = fuzz.trimf(seri.universe, [171, 216, 216])

    # Per Taşların Üyelik fonksiyonları
    per["A"] = fuzz.trimf(per.universe, [0, 0, 50])
    per["O"] = fuzz.trimf(per.universe, [25, 107.5, 190])
    per["Ç"] = fuzz.trimf(per.universe, [150, 230, 230])

    # Farklı Renk Üyelik fonksiyonları
    farkli_renk["A"] = fuzz.trimf(farkli_renk.universe, [0, 0, 49])
    farkli_renk["O"] = fuzz.trimf(farkli_renk.universe, [24, 97, 170])
    farkli_renk["Ç"] = fuzz.trimf(farkli_renk.universe, [153, 187, 187])

    # Çift taş Üyelik Fonksiyonları
    cift_tas["ÇA"] = fuzz.trimf(cift_tas.universe, [0, 0, 2])
    cift_tas["A"] = fuzz.trimf(cift_tas.universe, [2, 4, 6])
    cift_tas["O"] = fuzz.trimf(cift_tas.universe, [4, 6, 8])
    cift_tas["Ç"] = fuzz.trimf(cift_tas.universe, [8, 10, 10])

    # Gösterge üyelik fonksiyonu
    gosterge["0"] = fuzz.trimf(gosterge.universe, [0, 0, 0])
    gosterge["1"] = fuzz.trimf(gosterge.universe, [0, 0.5, 1])
    gosterge["2"] = fuzz.trimf(gosterge.universe, [1, 1.5, 2])

    # Okey üyelik Fonksiyonu
    okey["0"] = fuzz.trimf(okey.universe, [0, 0, 0])
    okey["1"] = fuzz.trimf(okey.universe, [0, 0.5, 1])
    okey["2"] = fuzz.trimf(okey.universe, [1, 1.5, 2])

    # El Ham Gücü Üyelik Fonksiyonu
    el_ham_guc["D"] = fuzz.trimf(el_ham_guc.universe, [0, 0, 90])
    el_ham_guc["O"] = fuzz.trimf(el_ham_guc.universe, [45, 110.75, 176.5])
    el_ham_guc["Y"] = fuzz.trimf(el_ham_guc.universe, [140, 233, 233])

    # El Gücü Üyelik Fonksiyonları
    el_gucu["D"] = fuzz.trimf(el_gucu.universe, [0, 0, 45])
    el_gucu["O"] = fuzz.trimf(el_gucu.universe, [30, 85, 140])
    el_gucu["Y"] = fuzz.trimf(el_gucu.universe, [110, 211, 211])

    # Kazanma Oranı Üyelik Fonksiyonları
    kazanma_orani["İ"] = fuzz.trimf(kazanma_orani.universe, [0, 0, 20]) # İMKANSIZ
    kazanma_orani["İY"] = fuzz.trimf(kazanma_orani.universe, [10, 20, 30]) # İMKANSIZA YAKIN
    kazanma_orani["B"] = fuzz.trimf(kazanma_orani.universe, [20, 30, 40]) # BELKİ
    kazanma_orani["ÇA"] = fuzz.trimf(kazanma_orani.universe, [30, 40, 50]) # ÇOK AZ
    kazanma_orani["A"] = fuzz.trimf(kazanma_orani.universe, [40, 50, 60]) # AZ
    kazanma_orani["O"] = fuzz.trimf(kazanma_orani.universe, [50, 60, 70]) # ORTA
    kazanma_orani["Y"] = fuzz.trimf(kazanma_orani.universe, [60, 70, 80]) # YÜKSEK
    kazanma_orani["ÇY"] = fuzz.trimf(kazanma_orani.universe, [70, 80, 90]) # ÇOK YÜKSEK
    kazanma_orani["K"] = fuzz.trimf(kazanma_orani.universe, [80, 100, 100]) # KESİN


    #kural1 = ctrl.Rule(el_gucu["Az"] & seri["Az"] & per["Az"], kazanma_orani["10"])

    # İMKANSIZLAR
    kural1 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["İ"])
    kural2 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["İ"])
    kural3 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["İ"])

    # İMKANSIZA YAKIN

    kural4 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["İY"])
    kural5 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["İY"])
    kural6 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["İY"])

    # BELKİ

    kural306 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural307 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural308 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])

    kural309 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural310 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural311 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])

    kural312 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural313 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural314 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["2"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])

    kural315 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural316 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])
    kural317 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["2"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["B"])

    kural300 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural301 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural302 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])

    kural303 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural304 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural305 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])

    kural7 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural8 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural9 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["2"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])

    kural10 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural11 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])
    kural12 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["2"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["B"])

    kural330 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural331 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural332 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])

    kural333 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural334 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural335 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])

    kural336 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural337 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural338 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["2"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])

    kural339 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural340 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural341 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["2"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])

    kural342 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural343 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural344 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural345 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural346 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])
    kural347 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["Y"] & el_gucu["D"], kazanma_orani["B"])



    # ÇOK AZ

    kural318 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["ÇA"])
    kural319 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["ÇA"])

    kural320 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["ÇA"])
    kural321 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["ÇA"])

    kural13 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["ÇA"])
    kural14 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["ÇA"])

    kural16 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["ÇA"])
    kural17 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["ÇA"])

    kural322 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])
    kural323 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])

    kural324 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])
    kural325 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])

    kural326 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])
    kural327 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])

    kural328 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["2"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])
    kural329 = ctrl.Rule(
        seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["2"] & el_ham_guc["Y"] & el_gucu[
            "D"], kazanma_orani["ÇA"])

    # AZ

    kural18 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural19 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural20 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])

    kural21 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural22 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural23 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])

    kural24 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural25 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural26 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])

    kural27 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural28 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])
    kural29 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["A"])

    # ORTA

    kural30 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural31 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural32 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural33 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural34 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural35 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural36 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural37 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural38 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural39 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural40 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural41 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural42 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural43 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural44 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural45 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural46 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural47 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural48 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural49 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural50 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural51 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural52 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural53 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural54 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural55 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural56 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural57 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural58 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural59 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural60 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural61 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural62 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural63 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural64 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural65 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural66 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural67 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural68 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural69 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural70 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural71 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural72 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural73 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural74 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural75 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural76 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural77 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural78 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural79 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural80 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural81 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural82 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural83 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural84 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural85 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural86 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural87 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural88 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural89 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural90 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural91 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural92 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural93 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural94 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural95 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural96 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural97 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural98 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural99 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural100 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])
    kural101 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["O"] & el_gucu["D"], kazanma_orani["O"])

    kural102 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural103 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural104 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural105 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural106 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural107 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])

    kural108 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural109 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])
    kural110 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["O"])



    # YÜKSEK

    kural111 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural112 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural113 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural114 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural115 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural116 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural117 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural118 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural119 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural120 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural121 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural122 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural123 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural124 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural125 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural126 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural127 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural128 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural129 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural130 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural131 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural132 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural133 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural134 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural135 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural136 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural137 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural138 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural139 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural140 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural141 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural142 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural143 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural144 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural145 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural146 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural147 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural148 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural149 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural150 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural151 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural152 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural153 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural154 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural155 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural156 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural157 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural158 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural159 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural160 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural161 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural162 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural163 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural164 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural165 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural166 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural167 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural168 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural169 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural170 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["A"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural171 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural172 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural173 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural174 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural175 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural176 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural177 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural178 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural179 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural180 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural181 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural182 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["O"] & cift_tas["O"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural183 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural184 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural185 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural186 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["A"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural187 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["A"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])
    kural188 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["Y"])

    kural189 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["1"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["Y"])
    kural190 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["A"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["Y"])
    kural191 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["A"] & cift_tas["O"] & gosterge["2"] & okey["0"] & el_ham_guc["D"] & el_gucu["D"], kazanma_orani["Y"])

    # ÇOK YÜKSEK

    kural192 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural193 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural194 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural195 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural196 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural197 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural198 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural199 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural200 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural201 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural202 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural203 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural204 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural205 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural206 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural207 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural208 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural209 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural348 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural349 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural350 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural351 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural352 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural356 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural353 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural354 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural355 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural210 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural211 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural212 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural213 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural214 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural215 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural216 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural217 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural218 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural219 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural220 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural221 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural222 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural223 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural224 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural225 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural226 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural227 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural228 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural229 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural230 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural231 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural232 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural233 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural234 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural235 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural236 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural237 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural238 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural239 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural240 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural241 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural242 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural243 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural244 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural245 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural246 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural247 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural248 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural249 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural250 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural251 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural252 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural253 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural254 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural255 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural256 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural257 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural258 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural259 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural260 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural261 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural262 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])
    kural263 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["ÇY"])

    kural264 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural265 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural266 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural267 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural268 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural269 = ctrl.Rule(seri["O"] & per["A"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural270 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural271 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural272 = ctrl.Rule(seri["A"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural273 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural274 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural275 = ctrl.Rule(seri["Ç"] & per["A"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural276 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural277 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural278 = ctrl.Rule(seri["A"] & per["Ç"] & farkli_renk["A"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    kural279 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural280 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])
    kural281 = ctrl.Rule(seri["A"] & per["A"] & farkli_renk["Ç"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["ÇY"])

    # KESİN

    kural282 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])
    kural283 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])
    kural284 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])

    kural285 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])
    kural286 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])
    kural287 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["0"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])

    kural288 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])
    kural289 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])
    kural290 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])

    kural291 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])
    kural292 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])
    kural293 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["1"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])

    kural294 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["2"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])
    kural295 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["2"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])
    kural296 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["2"] & el_ham_guc["Y"] & el_gucu["Y"], kazanma_orani["K"])

    kural297 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["0"] & okey["2"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])
    kural298 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["1"] & okey["2"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])
    kural299 = ctrl.Rule(seri["O"] & per["O"] & farkli_renk["O"] & cift_tas["ÇA"] & gosterge["2"] & okey["2"] & el_ham_guc["Y"] & el_gucu["O"], kazanma_orani["K"])




    kazanma_orani_ctrl = ctrl.ControlSystem([kural1,kural2,kural3,kural4,kural5,kural6,kural7,kural8,kural9,kural10,kural11,kural12,kural13,kural14,kural16,kural17,kural18,kural19,kural20,kural21,kural22,kural23,kural24,kural25,kural26,kural27,kural28,kural29,kural30,kural31,kural32,kural33,kural34,kural35,kural36,kural37,kural38,kural39,kural40,kural41,kural42,kural43,kural44,kural45,kural46,kural47,kural48,kural49,kural50,kural51,kural52,kural53,kural54,kural55,kural56,kural57,kural58,kural59,kural60,kural61,kural62,kural63,kural64,kural65,kural66,kural67,kural68,kural69,kural70,kural71,kural72,kural73,kural74,kural75,kural76,kural77,kural78,kural79,kural80,kural81,kural82,kural83,kural84,kural85,kural86,kural87,kural88,kural89,kural90,kural91,kural92,kural93,kural94,kural95,kural96,kural97,kural98,kural99,kural100,kural101,kural102,kural103,kural104,kural105,kural106,kural107,kural108,kural109,kural110,kural111,kural112,kural113,kural114,kural115,kural116,kural117,kural118,kural119,kural120,kural121,kural122,kural123,kural124,kural125,kural126,kural127,kural128,kural129,kural130,kural131,kural132,kural133,kural134,kural135,kural136,kural137,kural138,kural139,kural140,kural141,kural142,kural143,kural144,kural145,kural146,kural147,kural148,kural149,kural150,kural151,kural152,kural153,kural154,kural155,kural156,kural157,kural158,kural159,kural160,kural161,kural162,kural163,kural164,kural165,kural166,kural167,kural168,kural169,kural170,kural171,kural172,kural173,kural174,kural175,kural176,kural177,kural178,kural179,kural180,kural181,kural182,kural183,kural184,kural185,kural186,kural187,kural188,kural189,kural190,kural191,kural192,kural193,kural194,kural195,kural196,kural197,kural198,kural199,kural200,kural201,kural202,kural203,kural204,kural205,kural206,kural207,kural208,kural209,kural210,kural211,kural212,kural213,kural214,kural215,kural216,kural217,kural218,kural219,kural220,kural221,kural222,kural223,kural224,kural225,kural226,kural227,kural228,kural229,kural230,kural231,kural232,kural233,kural234,kural235,kural236,kural237,kural238,kural239,kural240,kural241,kural242,kural243,kural244,kural245,kural246,kural247,kural248,kural249,kural250,kural251,kural252,kural253,kural254,kural255,kural256,kural257,kural258,kural259,kural260,kural261,kural262,kural263,kural264,kural265,kural266,kural267,kural268,kural269,kural270,kural271,kural272,kural273,kural274,kural275,kural276,kural277,kural278,kural279,kural280,kural281,kural282,kural283,kural284,kural285,kural286,kural287,kural288,kural289,kural290,kural291,kural292,kural293,kural294,kural295,kural296,kural297,kural298,kural299,kural300, kural301, kural302, kural303, kural304, kural305, kural306, kural307, kural308, kural309, kural310, kural311, kural312, kural313, kural314, kural315, kural316, kural317, kural318, kural319, kural320, kural321, kural322, kural323, kural324, kural325, kural326, kural327, kural328, kural329, kural330, kural331, kural332, kural333, kural334, kural335, kural336, kural337,kural338, kural339, kural340, kural341, kural342, kural343, kural344, kural345, kural346, kural347, kural348, kural349, kural350, kural351, kural352, kural353, kural354, kural355, kural356])
    kazanma_orani_sim = ctrl.ControlSystemSimulation(kazanma_orani_ctrl)

    print(f"Seri : {seri_sayisi}", f"Per : {per_sayisi}",
          f"Farkli : {farkli_renk_sayisi}",
            f"gösterge : {gosterge_sayisi}", f"Okey : {okey_sayisi}",
          f"Ham güç : {el_ham_gucu_sayisi}", f"Güç : {el_gucu_sayisi}")

    kazanma_orani_sim.input["S"] = seri_sayisi
    kazanma_orani_sim.input["P"] = per_sayisi
    kazanma_orani_sim.input["FR"] = farkli_renk_sayisi
    kazanma_orani_sim.input["ÇT"] = cift_sayisi
    kazanma_orani_sim.input["G"] = gosterge_sayisi
    kazanma_orani_sim.input["O"] = okey_sayisi
    kazanma_orani_sim.input["EHG"] = el_ham_gucu_sayisi
    kazanma_orani_sim.input["EG"] = el_gucu_sayisi

    kazanma_orani_sim.compute()

    print(kazanma_orani_sim.output["KO"])
    print(kazanma_orani_sim.output)
    kazanma_orani.view(sim=kazanma_orani_sim)

    plt.show()


#bulanik_hesap(30,30,30,0,0,150,150)


# Üyelik fonksiyonları
#seri.view()
#per.view()
#farkli_renk.view()
#cift_tas.view()
#gosterge.view()
#okey.view()
#el_ham_guc.view()
#el_gucu.view()
#kazanma_orani.view()


