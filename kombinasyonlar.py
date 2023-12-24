def seri_bul(taslar):
    seri_listesi = []
    for i in range(len(taslar)):
        for j in range(i + 1, len(taslar)):
            for k in range(j + 1, len(taslar)):
                if (
                    taslar[i].renk == taslar[j].renk
                    and taslar[i].renk == taslar[k].renk
                    and taslar[i].deger + 1 == taslar[j].deger
                    and taslar[j].deger + 1 == taslar[k].deger
                ):
                    seri_listesi.append([taslar[i].deger, taslar[j].deger, taslar[k].deger])
                    # seri_listesi.append([str(taslar[i]), str(taslar[j]), str(taslar[k])])
    return seri_listesi

def per_bul(taslar):
    per_listesi = []
    for i in range(len(taslar)):
        for j in range(i + 1, len(taslar)):
            for k in range(j + 1, len(taslar)):
                for l in range(k + 1, len(taslar)):
                    if (
                        taslar[i].renk == taslar[j].renk
                        and taslar[i].renk == taslar[k].renk
                        and taslar[i].renk == taslar[l].renk
                        and taslar[i].deger + 1 == taslar[j].deger
                        and taslar[j].deger + 1 == taslar[k].deger
                        and taslar[k].deger + 1 == taslar[l].deger
                    ):
                        per_listesi.append([taslar[i].deger, taslar[j].deger, taslar[k].deger, taslar[l].deger])
                        # per_listesi.append([str(taslar[i]), str(taslar[j]), str(taslar[k]), str(taslar[l])])

    return per_listesi

def farkli_renk_bul(taslar):
    farkli_renk_listesi = []
    for i in range(len(taslar)):
        for j in range(i + 1, len(taslar)):
            for k in range(j + 1, len(taslar)):
                if taslar[i].deger == taslar[j].deger == taslar[k].deger and taslar[i].renk != taslar[j].renk and taslar[i].renk != taslar[k].renk and taslar[j].renk != taslar[k].renk:
                    farkli_renk_listesi.append([taslar[i].deger, taslar[j].deger, taslar[k].deger])
                    # farkli_renk_listesi.append([str(taslar[i]), str(taslar[j]), str(taslar[k])]) liste döndürecek gerek olursa

    return farkli_renk_listesi

def el_gucu(taslar):
    guc = 0
    for tas in taslar:
        guc += tas.deger
    return guc
