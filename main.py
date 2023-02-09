#megoldas
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    jatekospont: int = szamolas(jatekoslapok)
    geppont: int = szamolas(geplapok)
    jatekoslapok = len(jatekoslapok)
    geplapok = len(geplapok)
    if jatekospont <= 21 and geppont <= 21:
        if jatekospont > geppont:
            s = "Játékos nyert!"
        elif geppont > jatekospont:
            s = "Gép nyert!"
        elif geppont == jatekospont:
            if jatekoslapok < geplapok:
                s = "Játékos nyert!"
            elif jatekoslapok > geplapok:
                s = "Gép nyert!"
            else:
                s = "Döntetlen osztoztok a nyereségen"
    else:
        if jatekospont > 21:
            s = "Játékos vesztett!"
        if geppont > 21:
            s = "Gép vesztett!"
        if jatekospont > 21 and geppont > 21:
            s = "Döntetlen osztoztok a nyereségen"

    return s

def szamolas(lapok)->int:
    pontok: int = 0
    i: int = 0
    while i < len(lapok):
        pontok += lapok[i]
        i += 1
    return pontok
#tesztek
def jatekos_vesztett_teszt():
    jatekospontok = [10, 5, 7]
    geppontok = [2, 7, 9]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos vesztett!"
    if kapott == vart:
        print("Az első teszt sikeres!")
    else:
        print("Az első teszt megbukott")

def gep_vesztett_teszt():
    jatekospontok = [2, 7, 9]
    geppontok = [10, 5, 7]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép vesztett!"
    if kapott == vart:
        print("A második teszt sikeres!")
    else:
        print("A második teszt megbukott")

def lapok_osszege_teszt():
    jatekospontok = [11, 11]
    geppontok = [10, 10]
    #teszt
    osszeg = szamolas(jatekospontok)
    if osszeg > 21:
        print("A harmadik teszt sikeres!")
    else:
        print("A harmadik teszt megbukott!")

def jatekos_kozelebb_teszt():
    jatekospontok = [9, 10]
    geppontok = [8, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A negyedik teszt sikeres!")
    else:
        print("A negyedik teszt megbukott")

def gep_kozelebb_teszt():
    jatekospontok = [8, 10]
    geppontok = [9, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("Az ötödik teszt sikeres!")
    else:
        print("Az ötödik teszt megbukott")

def gep_vesztett_dontetlen_teszt():
    jatekospontok = [9, 10]
    geppontok = [9, 5, 5]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A hatodik teszt sikeres!")
    else:
        print("A hatodik teszt megbukott")

def jatekos_vesztett_dontetlen_teszt():
    jatekospontok = [9, 5, 4]
    geppontok = [9, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A hetedik teszt sikeres!")
    else:
        print("A hetedik teszt megbukott")

def dontetlen_teszt():
    jatekospontok = [10, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A nyolcadik teszt sikeres!")
    else:
        print("A nyolcadik teszt megbukott")




def jatekos_nyer_huszonegy():
    jatekospontok = [11, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A kilencedik teszt sikeres!")
    else:
        print("A kilencedik teszt megbukott")

def jatekos_nyer_tobb_lap():
    jatekospontok = [10, 5, 4]
    geppontok = [10, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A tizedik teszt sikeres!")
    else:
        print("A tizedik teszt megbukott")

def jatekos_nyer_kevesebb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A tizenegyedik teszt sikeres!")
    else:
        print("A tizenegyedik teszt megbukott")

def jatekos_veszit_tobb_lap():
    jatekospontok = [10, 5, 4]
    geppontok = [10, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A tizenkettedik teszt sikeres!")
    else:
        print("A tizenkettedik teszt megbukott")

def jatekos_veszit_kevesebb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos vesztett!"
    if kapott == vart:
        print("A tizenharmadik teszt sikeres!")
    else:
        print("A tizenharmadik teszt megbukott")




def gep_nyer_huszonegy():
    jatekospontok = [10, 10]
    geppontok = [11, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A tizenötödik teszt sikeres!")
    else:
        print("A tizenötödik teszt megbukott")

def gep_nyer_tobb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A tizenhatodik teszt sikeres!")
    else:
        print("A tizenhatodik teszt megbukott")

def gep_nyer_kevesebb_lap():
    jatekospontok = [10, 5, 4]
    geppontok = [10, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A tizenhetedik teszt sikeres!")
    else:
        print("A tizenhetedik teszt megbukott")

def gep_veszit_tobb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A tizennyolcadik teszt sikeres!")
    else:
        print("A tizennyolcadik teszt megbukott")

def gep_veszit_kevesebb_lap():
    jatekospontok = [10, 5, 4]
    geppontok = [10, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A tizenkilencedik teszt sikeres!")
    else:
        print("A tizenkilencedik teszt megbukott")




def dontetlen_huszonegy():
    jatekospontok = [10, 11]
    geppontok = [10, 11]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A huszadik teszt sikeres!")
    else:
        print("A huszadik teszt megbukott")

def dontetlen_lap():
    jatekospontok = [10, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A huszonegyedik teszt sikeres!")
    else:
        print("A huszonegyedik teszt megbukott")

def dontetlen_tobb_mint_huszonegy():
    jatekospontok = [12, 11]
    geppontok = [12, 11]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A huszonkettedik teszt sikeres!")
    else:
        print("A huszonkettedik teszt megbukott")

def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    lapok_osszege_teszt()
    jatekos_kozelebb_teszt()
    gep_kozelebb_teszt()
    gep_vesztett_dontetlen_teszt()
    jatekos_vesztett_dontetlen_teszt()
    dontetlen_teszt()
    jatekos_nyer_huszonegy()
    jatekos_nyer_tobb_lap()
    jatekos_nyer_kevesebb_lap()
    jatekos_veszit_tobb_lap()
    jatekos_veszit_kevesebb_lap()
    gep_nyer_huszonegy()
    gep_nyer_tobb_lap()
    gep_nyer_kevesebb_lap()
    gep_veszit_tobb_lap()
    gep_veszit_kevesebb_lap()
    dontetlen_huszonegy()
    dontetlen_lap()
    dontetlen_tobb_mint_huszonegy()


tesztek()