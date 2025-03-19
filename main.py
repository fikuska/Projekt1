"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martina Drobná
email: fiamar@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registrovani_uzivatele = {"bob": "123", "ann": "pass123", 
                          "mike": "password123", "liz": "pass123"} 
pomlcka = 40 * "-"

prihlas_jmeno = input("Zadej své přihlašovací jméno! ")
prihlas_heslo = input("Zadej heslo! ")


if registrovani_uzivatele.get(prihlas_jmeno) == prihlas_heslo:
    print("")
    print("Uživatelské jméno:",prihlas_jmeno, "\nHeslo:", prihlas_heslo)
    print(pomlcka)
    print("Vítej v aplikaci,", prihlas_jmeno, "\nMáme 3 texty k analýze!")
    print(pomlcka)
    vyber = input("Zadej číslo textu od 1 do 3: ")

    def pocet_slov(texty):
        '''Spočítá počet slov v zadaném textu'''
        return len(texty.split())
    
    def pocet_slov_zac_velkym_pismenem(texty):
        '''Spočítá počet slov začínající velkým písmenem'''
        pocet = 0
        for pocet_slov in texty.split():
            if pocet_slov.istitle():
                pocet += 1
        return pocet

    def pocet_slov_velka_pismena(texty):
        '''Spočítá počet slov, která obsahují jen velká písmena'''
        pocet = 0
        for pocet_slov in texty.split():
            if pocet_slov.isupper():
                pocet += 1
        return pocet
        
    def pocet_slov_mala_pismena(texty):
        '''Spočítá počet slov, která obsahují jen malá písmena'''
        pocet = 0
        for pocet_slov in texty.split():
            if pocet_slov.islower():
                pocet += 1
        return pocet
        
    def pocet_cisel(texty):
        '''Spočítá počet slov, která obsahují čísla'''
        pocet = 0
        for pocet_slov in texty.split():
            if pocet_slov.isnumeric():
                pocet += 1
        return pocet
        
    def suma_cisel(texty):
        '''Spočítá sumu všech čísel v textu'''
        pocet = 0   
        for suma in texty.split():
            if suma.isnumeric():
                pocet += int(suma)
        return pocet
        
    def pocet_pismen_ve_slove(texty):
        '''Spočítá četnost různých délek slov v textu'''
        pocet_vyskytu = dict()           
        for slovo in texty.split():
            slovo_bez_znaku = slovo.strip(",.!?:")
            delka = len(slovo_bez_znaku)
            pocet_vyskytu[delka] = pocet_vyskytu.get(delka, 0) + 1
        for delku, pocet in sorted(pocet_vyskytu.items()):
            print(f"{delku:>7} | {'*' * pocet:20}| {pocet}", sep="\t")

    def vyber_textu(text):
        print(pomlcka)
        print(f"Ve vybraném textu je {pocet_slov(text)} slov.")
        print(
            f"Ve vybraném textu je {pocet_slov_zac_velkym_pismenem(text)}"
            " slov začínajících velkým písmenem."
            )
        print(
            f"Ve vybraném textu je {pocet_slov_velka_pismena(text)}"
            " slov obsahující velká písmena."
            )
        print(
            f"Ve vybraném textu je {pocet_slov_mala_pismena(text)}"
            " slov obsahující malá písmena."
            )
        print(f"Ve vybraném textu je {pocet_cisel(text)} slov obsahující čísla.")
        print(f"Ve vybraném textu je součet všech čísel {suma_cisel(text)}.")
        print(pomlcka)
        print(f"{"  délka":6} | {"výskyt":20}| počet")
        print(pomlcka)
        pocet_pismen_ve_slove(text)
        print(" ")

    if vyber == "1":
        vyber_textu(TEXTS[0])
    elif vyber == "2":
        vyber_textu(TEXTS[1])  
    elif vyber == "3":
        vyber_textu(TEXTS[2])
    elif vyber.isdigit():
        print("Zadali jste špatné číslo. Ukončuji program")
        exit()
    else:
        print("Nezadali jste číslo. Ukončuji program")
        exit()
else:
    print("Neregistrovaný uživatel. Ukončuji program!")
    exit()   
     