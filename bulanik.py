import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from skfuzzy import control as ctrl

seri = ctrl.Antecedent(np.arange(0, 216, 1), "Seri")
per = ctrl.Antecedent(np.arange(0, 230, 1), "Per")
farkli_renk = ctrl.Antecedent(np.arange(0, 186, 1), "Farklı Renk")
cift_tas = ctrl.Antecedent(np.arange(0, 10, 0.2), "Çift Taş")

gosterge = ctrl.Antecedent(np.arange(0, 2, 0.01), "Gösterge")
okey = ctrl.Antecedent(np.arange(0, 2, 0.01), "Okey")

el_ham_guc = ctrl.Antecedent(np.arange(0, 234, 1), "El Ham Gücü")
el_gucu = ctrl.Antecedent(np.arange(0, 211, 1), "El Gücü")

kazanma_orani = ctrl.Consequent(np.arange(0, 101, 10), "Kazanma Oranı")


# Seri Taşların Kombinasyonları Üyelik Fonksiyonları
seri["Az"] = fuzz.trimf(seri.universe, [0, 0, 36])
seri["Orta"] = fuzz.trimf(seri.universe, [18, 105.75, 193.5])
seri["Çok"] = fuzz.trimf(seri.universe, [171, 216, 216])

# Per Taşların Üyelik fonksiyonları
per["Az"] = fuzz.trimf(per.universe, [0, 0, 50])
per["Orta"] = fuzz.trimf(per.universe, [25, 107.5, 190])
per["Çok"] = fuzz.trimf(per.universe, [150, 230, 230])

# Farklı Renk Kombinasyonları Üyelik fonksiyonları
farkli_renk["Az"] = fuzz.trimf(farkli_renk.universe, [0, 0, 49])
farkli_renk["Orta"] = fuzz.trimf(farkli_renk.universe, [24, 97, 170])
farkli_renk["Çok"] = fuzz.trimf(farkli_renk.universe, [153, 187, 187])

# Çift taş üyelik Fonksiyonları
cift_tas["0-2"] = fuzz.trimf(cift_tas.universe, [0, 0, 2])
cift_tas["2-6"] = fuzz.trimf(cift_tas.universe, [2, 4, 6])
cift_tas["4-8"] = fuzz.trimf(cift_tas.universe, [4, 6, 8])
cift_tas["8-10"] = fuzz.trimf(cift_tas.universe, [8, 10, 10])

# Gösterge üyelik fonksiyonu
gosterge["0"] = fuzz.trimf(gosterge.universe, [0, 0, 0])
gosterge["1"] = fuzz.trimf(gosterge.universe, [0, 0.5, 1])
gosterge["2"] = fuzz.trimf(gosterge.universe, [1, 1.5, 2])

# Okey üyelik Fonksiyonu
okey["Az"] = fuzz.trimf(okey.universe, [0, 0, 0])
okey["Orta"] = fuzz.trimf(okey.universe, [0, 0.5, 1])
okey["Cok"] = fuzz.trimf(okey.universe, [1, 1.5, 2])

# El Ham Gücü Üyelik Fonksiyonu
el_ham_guc["Düşük"] = fuzz.trimf(el_ham_guc.universe, [0, 0, 90])
el_ham_guc["Orta"] = fuzz.trimf(el_ham_guc.universe, [45, 110.75, 176.5])
el_ham_guc["Yüksek"] = fuzz.trimf(el_ham_guc.universe, [140, 233, 233])

# El Gücü Üyelik Fonksiyonları
el_gucu["Az"] = fuzz.trimf(el_gucu.universe, [0, 0, 45])
el_gucu["Orta"] = fuzz.trimf(el_gucu.universe, [30, 85, 140])
el_gucu["Çok"] = fuzz.trimf(el_gucu.universe, [110, 211, 211])

# Kazanma Oranı Üyelik Fonksiyonları
kazanma_orani["10"] = fuzz.trimf(kazanma_orani.universe, [0, 0, 20])
kazanma_orani["20"] = fuzz.trimf(kazanma_orani.universe, [10, 20, 30])
kazanma_orani["30"] = fuzz.trimf(kazanma_orani.universe, [20, 30, 40])
kazanma_orani["40"] = fuzz.trimf(kazanma_orani.universe, [30, 40, 50])
kazanma_orani["50"] = fuzz.trimf(kazanma_orani.universe, [40, 50, 60])
kazanma_orani["60"] = fuzz.trimf(kazanma_orani.universe, [50, 60, 70])
kazanma_orani["70"] = fuzz.trimf(kazanma_orani.universe, [60, 70, 80])
kazanma_orani["80"] = fuzz.trimf(kazanma_orani.universe, [70, 80, 90])
kazanma_orani["90"] = fuzz.trimf(kazanma_orani.universe, [80, 100, 100])


"""kural1 = ctrl.Rule(el_gucu["Az"] & seri["Az"] & per["Az"], kazanma_orani["10"])

kazanma_orani_ctrl = ctrl.ControlSystem([kural1])
kazanma_orani_sim = ctrl.ControlSystemSimulation(kazanma_orani_ctrl)

kazanma_orani_sim.input["El Gücü"] = 30
kazanma_orani_sim.input["Seri"] = 20
kazanma_orani_sim.input["Per"] = 30

kazanma_orani_sim.compute()
kazanma_oranii = kazanma_orani_sim.output["Kazanma Oranı"]
print(f"Kazanma Oranı: {kazanma_oranii}")"""




# Üyelik fonksiyonlarını çiz

#seri.view()
#per.view()
#farkli_renk.view()
#cift_tas.view()

#gosterge.view()
#okey.view()

#el_ham_guc.view()
#el_gucu.view()

kazanma_orani.view()

plt.show()

