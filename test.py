if not durum:
    ekran.blit(sagok, (775, 90))
    ekran.blit(solok, (325, 90))
    ekran.blit(birak, (100, 250))
    if batar_secili:
        ekran.blit(batar2, (200, 700))
    elif not batar_secili:
        ekran.blit(batar1, (200, 700))
    if batmaz_secili:
        ekran.blit(batmaz2, (800, 700))
    elif not batmaz_secili:
        ekran.blit(batmaz1, (800, 700))
objeler[gecerli_obje].ciz()
if durum:
    if dusus:
        if gecerli_sise < len(sise) and objeler[gecerli_obje].konum.y > 230 and degis:
            if gecerli_sise + 0.085 > 6:
                gecerli_sise = 0
                degis = False
            else:
                gecerli_sise += 0.085

        if objeler[gecerli_obje].yogunluk == 1:
            if objeler[gecerli_obje].konum.y < 230:
                objeler[gecerli_obje].konum.y += hiz * dt
            elif 230 <= objeler[gecerli_obje].konum.y < 515:
                objeler[gecerli_obje].konum.y += hiz * dt
                if hiz - 8 > 125:
                    hiz -= 8
            elif objeler[gecerli_obje].konum.y >= 515:
                hiz = 750
                dusus = False

        if objeler[gecerli_obje].yogunluk == 0:
            if objeler[gecerli_obje].konum.y < 230:
                if objeler[gecerli_obje].konum.y <= 230 and hiz < 0:
                    hiz = 750
                    dusus = False
                objeler[gecerli_obje].konum.y += hiz * dt
            elif 230 <= objeler[gecerli_obje].konum.y < 515:
                objeler[gecerli_obje].konum.y += hiz * dt
                if hiz - 8 > 125 or -125 < hiz - 8 < 0:
                    hiz -= 8
            elif objeler[gecerli_obje].konum.y >= 515:
                hiz = -hiz
                objeler[gecerli_obje].konum.y += hiz * dt
    else:
        if tahmin == objeler[gecerli_obje].yogunluk == 1:
            ekran.blit(yazi1, (875, 250))
        if tahmin == objeler[gecerli_obje].yogunluk == 0:
            ekran.blit(yazi3, (875, 250))
        if tahmin != objeler[gecerli_obje].yogunluk == 1:
            ekran.blit(yazi4, (875, 250))
        if tahmin != objeler[gecerli_obje].yogunluk == 0:
            ekran.blit(yazi2, (875, 250))
        ekran.blit(tekrarla, (875, 550))
siseq.ciz()