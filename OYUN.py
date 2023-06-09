import pygame as py


def main():
    py.init()
    g, y = 1200, 900
    ekran = py.display.set_mode((g, y))
    clock = py.time.Clock()
    dt = 0
    py.display.set_caption("Yoğunluk Oyunu")
    oynat = False
    giris = True
    fiziklab = py.image.load("fiziklab.png")
    girisekran = py.image.load("girispng.png")
    hi = py.image.load("hi.png")
    hi2 = py.image.load("hi2.png")
    hi3 = py.image.load("hi3.png")
    hi4 = py.image.load("hi4.png")
    hi5 = py.image.load("hi5.png")
    hi6 = py.image.load("hi6.png")
    hi7 = py.image.load("hi7.png")
    sagok = py.image.load("sagok.png")
    solok = py.image.load("solok.png")
    batar1 = py.image.load("batar.png")
    batar2 = py.image.load("batar2.png")
    batmaz1 = py.image.load("batmaz.png")
    batmaz2 = py.image.load("batmaz2.png")
    birak = py.image.load("birak.png")
    yazi1 = py.image.load("yazi1.png")
    yazi2 = py.image.load("yazi2.png")
    yazi3 = py.image.load("yazi3.png")
    yazi4 = py.image.load("yazi4.png")
    sifiralti = py.image.load("0-6.png")
    altisekiz = py.image.load("6-8.png")
    sekiz = py.image.load("8.png")
    tekrarla = py.image.load("tekrarla.png")
    smallfont = py.font.SysFont('Calibri', 35)
    bigfont = py.font.SysFont("Calibri", 70)
    sise = [hi, hi2, hi3, hi4, hi5, hi6, hi7]
    gecerli_sise = 0
    gecerli_obje = 0

    class Obje:
        def __init__(self, cesit, yogunluk, konum):
            self.cesit = cesit
            self.yogunluk = yogunluk
            self.konum = py.Vector2(konum[0], konum[1])

        def ciz(self):
            gorsel = py.image.load(f"{self.cesit}.png")
            ekran.blit(gorsel, self.konum)

    class Sise:
        def __init__(self, faz, konum):
            self.faz = faz
            self.konum = py.Vector2(konum[0], konum[1])

        def ciz(self):
            ekran.blit(self.faz, self.konum)

    pos = [550, 100]
    hiz = 750
    dusus = True
    degis = True
    durum = False
    batar_secili = False
    batmaz_secili = False
    puan = 0
    tahmin = ""
    objeler = [Obje("para", 1, pos), Obje("tas", 1, pos), Obje("bilye", 1, pos), Obje("petsise", 0, pos),
               Obje("balon", 0, pos), Obje("atac", 1, pos), Obje("tahtablok", 0, pos), Obje("kapak", 0, pos)]
    siseq = Sise(sise[gecerli_sise], (350, 200))
    while giris:
        mouse = py.mouse.get_pos()
        for olay in py.event.get():
            if olay.type == py.QUIT:
                giris = False
            if olay.type == py.MOUSEBUTTONDOWN:
                if 400 <= mouse[0] <= 800 and 550 <= mouse[1] <= 700:
                    giris = False
                    oynat = True
        ekran.blit(girisekran, (0, 0))
        py.display.flip()
    while oynat:
        if len(objeler) == 0:
            for olay in py.event.get():
                if olay.type == py.QUIT:
                    oynat = False
            if 0 <= puan < 6:
                ekran.blit(sifiralti, (0, 0))
            elif 6 <= puan < 8:
                ekran.blit(altisekiz, (0, 0))
            elif puan == 8:
                ekran.blit(sekiz, (0, 0))
            yazi5 = bigfont.render(f"Puaniniz: {puan}", True, "black")
            ekran.blit(yazi5, (875, 60))
        else:
            mouse = py.mouse.get_pos()
            ekran.blit(fiziklab, (0, 0))
            siseq.faz = sise[int(gecerli_sise)]
            secili_obje = smallfont.render(f"Seçili obje: {objeler[gecerli_obje].cesit}", True, "black")
            ekran.blit(secili_obje, (490, 200))
            for olay in py.event.get():
                if olay.type == py.QUIT:
                    oynat = False
                if olay.type == py.MOUSEBUTTONDOWN:
                    if 325 <= mouse[0] <= 425 and 90 <= mouse[1] <= 190:
                        if gecerli_obje - 1 == -1:
                            gecerli_obje = len(objeler) - 1
                        else:
                            gecerli_obje -= 1
                    if 775 <= mouse[0] <= 875 and 90 <= mouse[1] <= 190:
                        if gecerli_obje + 1 == len(objeler):
                            gecerli_obje = 0
                        else:
                            gecerli_obje += 1
                    if 200 <= mouse[0] <= 400 and 700 <= mouse[1] <= 800:
                        batar_secili = True
                        if batmaz_secili:
                            batmaz_secili = False
                        tahmin = 1
                    if 800 <= mouse[0] <= 1000 and 700 <= mouse[1] <= 800:
                        batmaz_secili = True
                        if batar_secili:
                            batar_secili = False
                        tahmin = 0
                    if 100 <= mouse[0] <= 300 and 250 <= mouse[1] <= 350:
                        durum = True
                        dusus = True
                        degis = True
                        if objeler[gecerli_obje].yogunluk == tahmin:
                            puan += 1
                    if 850 <= mouse[0] <= 1150 and 550 <= mouse[1] <= 650:
                        durum = False
                        for i in objeler:
                            [i.konum.x, i.konum.y] = pos
                        objeler.remove(objeler[gecerli_obje])
                        batar_secili = batmaz_secili = False
            if len(objeler) != 0:
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
                            elif 230 <= objeler[gecerli_obje].konum.y < 270:
                                objeler[gecerli_obje].konum.y += hiz * dt
                                if hiz - 8 > 125 or -125 < hiz - 8 < 0:
                                    hiz -= 8
                            elif objeler[gecerli_obje].konum.y >= 270:
                                hiz = -hiz
                                objeler[gecerli_obje].konum.y += hiz * dt
                            gecerli_sise = 0
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
        dt = clock.tick(144) / 1000
        py.display.flip()


if __name__ == "__main__":
    main()

# SELAM OLSUN
