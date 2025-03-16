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

registrovani_uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
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
    def počet_slov_zač_velkým_písmenem(texty):
        '''Spočítá počet slov začínající velkým písmenem'''
        počet = 0
        for počet_slov in texty.split():
            if počet_slov.istitle():
                počet += 1
        return počet

    def počet_slov_velká_písmena(texty):
        '''Spočítá počet slov, která obsahují jen velká písmena'''
        počet = 0
        for počet_slov in texty.split():
            if počet_slov.isupper():
                počet += 1
        return počet
        
    def počet_slov_malá_písmena(texty):
        '''Spočítá počet slov, která obsahují jen malá písmena'''
        počet = 0
        for počet_slov in texty.split():
            if počet_slov.islower():
                počet += 1
        return počet
        
    def počet_čísel(texty):
        '''Spočítá počet slov, která obsahují čísla'''
        počet = 0
        for počet_slov in texty.split():
            if počet_slov.isnumeric():
                počet += 1
        return počet
        
    def suma_čísel(texty):
        '''Spočítá sumu všech čísel v textu'''
        počet = 0   
        for suma in texty.split():
            if suma.isnumeric():
                počet += int(suma)
        return počet
        
    def počet_písmen_ve_slově(texty):
        '''Spočítá četnost různých délek slov v textu'''
        počet_výskytů = dict()           
        for slovo in texty.split():
            slovo_bez_znaků = slovo.strip(",.!?:")
            délka = len(slovo_bez_znaků)
            počet_výskytů[délka] = počet_výskytů.get(délka, 0) + 1
        for délku, počet in sorted(počet_výskytů.items()):
            print(f"{délku:>6}|{'*' * počet:20}| {počet}", sep="\t")

    if vyber == "1":
        print(pomlcka)
        print(f"Ve vybraném textu je {pocet_slov(TEXTS[0])} slov.")
        print(f"Ve vybraném textu je {počet_slov_zač_velkým_písmenem(TEXTS[0])} slov začínajících velkým písmenem.")
        print(f"Ve vybraném textu je {počet_slov_velká_písmena(TEXTS[0])} slov obsahující velká písmena.")
        print(f"Ve vybraném textu je {počet_slov_malá_písmena(TEXTS[0])} slov obsahující malá písmena.")
        print(f"Ve vybraném textu je {počet_čísel(TEXTS[0])} slov obsahující čísla.")
        print(f"Ve vybraném textu je součet všech čísel {suma_čísel(TEXTS[0])}.")
        print(pomlcka)
        print(f"{"délka":6}|{"výskyt":20}|počet")
        print(pomlcka)
        počet_písmen_ve_slově(TEXTS[0])
        print(" ")
    elif vyber == "2":
        print(pomlcka)
        print(f"Ve vybraném textu je {pocet_slov(TEXTS[1])} slov.")
        print(f"Ve vybraném textu je {počet_slov_zač_velkým_písmenem(TEXTS[1])} slov začínajících velkým písmenem.")
        print(f"Ve vybraném textu je {počet_slov_velká_písmena(TEXTS[1])} slov obsahující velká písmena.")
        print(f"Ve vybraném textu je {počet_slov_malá_písmena(TEXTS[1])} slov obsahující malá písmena.")
        print(f"Ve vybraném textu je {počet_čísel(TEXTS[1])} slov obsahující čísla.")
        print(f"Ve vybraném textu je součet všech čísel {suma_čísel(TEXTS[1])}.")
        print(pomlcka)
        print(f"{"délka":6}|{"výskyt":20}|počet")
        print(pomlcka)
        počet_písmen_ve_slově(TEXTS[1])
        print(" ")
    elif vyber == "3":
        print(pomlcka)
        print(f"Ve vybraném textu je {pocet_slov(TEXTS[2])} slov.")
        print(f"Ve vybraném textu je {počet_slov_zač_velkým_písmenem(TEXTS[2])} slov začínajících velkým písmenem.")
        print(f"Ve vybraném textu je {počet_slov_velká_písmena(TEXTS[2])} slov obsahující velká písmena.")
        print(f"Ve vybraném textu je {počet_slov_malá_písmena(TEXTS[2])} slov obsahující malá písmena.")
        print(f"Ve vybraném textu je {počet_čísel(TEXTS[2])} slov obsahující čísla.")
        print(f"Ve vybraném textu je součet všech čísel {suma_čísel(TEXTS[2])}.")
        print(pomlcka)
        print(f"{"délka":6}|{"výskyt":20}|počet")
        print(pomlcka)
        počet_písmen_ve_slově(TEXTS[2])
        print(" ")
    elif vyber.isdigit():
        print("Zadali jste špatné číslo. Ukončuji program")
    else:
        print("Nezadali jste číslo. Ukončuji program")
else:
    print("Neregistrovaný uživatel. Ukončuji program!")
        
     