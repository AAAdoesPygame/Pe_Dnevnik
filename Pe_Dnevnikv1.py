#--// importani Library //--
import json
import os
import random
import math
import time
import threading
import subprocess
import pygame

# --// Variable //-- #

IsRunning = True
FirstTime = True
PrviPuta_sav_print = True
data_file = 'pe_dnevnik_data.json'

# --// Liste //--
#tp = Trajni Podatci
Tp = ["ime", "prezime", "adresa"]
Predmeti = ["Hj", "MAT", "GEO", "TZK", "FIZ", "KEM", "BIO", "GK", "ENG", "TK", "LK", "POV"]
PredmatiEX = ["NJEM", "VJ", "INF", "TALIJANSKI"]
brojPredmeta = []

#--// dictionarys //--

brojUC = {}
ucenik = {}
ucenici = {}
brojRAZ = {}
razredi_imena = {}
kojiPredmeti = {}

#--// funkcije //-- (sve ispod ovoga su funkcije)

#--// "Općenite" funkcije //--

#NESMOJE SE KORISTITI OSIM U //NoviUC//, //NoviRAZ//, //NOVIPREDMET//  functionima
def BrojUC():
    global ucenici, brojUC
    # brojUC_UR = broj učenika u razredu
    brojUC_UR = int(input("Unesite Broj Učenika:"))
    brojUC = {brojUC_UR: None}  # postavi valutu "brojUC_UR"
    print(brojUC)

def BROJRAZ():
    brojRAZ_uk = int(input("Unesite Broj Razreda:"))
    brojRAZ_uk[brojRAZ]
    print(brojRAZ)

def BROJPREDMETA():
    broj_Predmeta_razreda = int(input("Unesite Broj predmeta"))
    brojPredmeta.append(broj_Predmeta_razreda)

# --// kraj "Općenitih" funkcija //--

def NoviRAZ():
    BROJRAZ()
    for i in brojRAZ:
        imenaRAZ = input(f"Unesi ime {i} razredu.")
        razredi_imena[imenaRAZ]
        print(razredi_imena)
        temp_ucenik = {}  # Napravi "temporary" dict. u kojem idu učenici
        for j in Tp:
            x = input(f"Unesite --{j}--")
            temp_ucenik[j] = x
        ucenici[student_key] = temp_ucenik  # Postavi "temporary" dict. u main dict. (ucenici)
        print("SAVING DATA..")
        time.sleep(1)
        save_data()
        print("SAVING DATA Sucess")

    print(ucenici)

# --// POPRAVLJENO //--
def NoviUC(brojUC_UR):
    global ucenici

    for i in range(brojUC_UR):
        student_key = f"UČENIK ID {len(ucenici) + 1}"
        temp_ucenik = {}

        for j in Tp:
            x = input(f"Unesite --{j}--")
            temp_ucenik[j] = x

        temp_ucenik['OP_predmeti'] = []
        ucenici[student_key] = temp_ucenik

        NoviPredmetUC(temp_ucenik)
        ucenici[student_key] = temp_ucenik  # Corrected line

        ucenici[student_key]['OP_predmeti'] = Predmeti
        print(ucenici)www
        # sprema podatke
        print("SAVING DATA..")
        time.sleep(1)
        save_data()
        print("SAVING DATA Success")

    print(ucenici)

def NOVIPREDMET():
    BROJPREDMETA()
    for i in broj_Predmeta_razreda:
        x = input(f"""unesite hoće li predmet biti jedan koji svi moraju ići !(Upišite OP)!
                      ake je predmetkoji nije bitan "(Upišite EX)
                      ako neželite novi predmet upišite (F)" 
                      {i}: """)
        if x == "OP":
            Predmeti.append(x)
            print("predmet dodan u listu OP")
        elif x == "EX":
            PredmatiEX.append(x)
            print("predmet dodan u listu EX")
        elif x == "F":
            end()
        else:
            print("ERROR krivo upisan 'x' ")

# --// !!NE RADI!! //--
def NoviPredmetUC(temp_ucenik):
    x_1 = int(input("Koliko 'EX' predmeta ovaj učenik ima: (0 nijedan izađe) (>1 jedan ili više)"))
    x_1T = False
    print("Unesite T ako želite predmet i (ništa) ako ne želite!")
    temp_listNPUC = []

    for _ in range(x_1):
        for i in PredmatiEX:
            print("Nakon što upišete T ili (ništa) upišite prva 2 slova predmeta!")
            print("PRIMJER : TNJ, TTA, TIN")
            x_2 = input(f"{i}: ")

            if x_2 == "TNJ" and x_1T == False:
                print("ODBIJEN ODABIR.")
                continue

            if x_2 == "":
                print("ODBIJEN ODABIR.")
                continue

            temp_ucenik[PredmatiEX[i]] = x_2
            temp_listNPUC.append(PredmatiEX[i])
            x_1T = True



# --// POPRAVLJENO //--
def save_data():
    # Postavi podatke u .json file
    with open(data_file, 'w') as file:
        json.dump({
            'ucenici': ucenici,
            'razredi_imena': razredi_imena,
            'kojiPredmeti': kojiPredmeti
        }, file)

# --// POPRAVLJENO //--
def load_data():
    # Učita podatke of .json file
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            data = json.load(file)
            return data.get('ucenici', {})
    else:
        print(r"!!!ERROR!!! DID NOT FIND (pe_dnevnik_data.json) file!!!")
        return {}

# --// POPRAVLJENO //--
def print_students_info():
    global data_file
    # Provjerava jel postoji data_file
    if os.path.exists(data_file):
        ucenici = load_data()
        print(ucenici)

        # Isprinta informaciju o učenicima
        print("Informacija o Učenicima:")
        for key, ucenici_info in ucenici.items():
            print(f"{key}: {ucenici_info}")
    else:
        print(r"!!!ERROR!!! DID NOT FIND (pe_dnevnik_data.json) file!!!")
        komanda = ""

# --// kraj funkcija //--

ucenici = load_data()

#--// Main //-- (sve ispod ovog je glavni dio)
def MAIN():
    global IsRunning, PrviPuta_sav_print, ucenici

    #music_thread = threading.Thread(target=start_music)
    #music_thread.start()

    while IsRunning == True:

        print(""" _______      ______   _        _______           _       _________ _       
|-----\  (  ____ \    (  __  \ ( (    /|(  ____ \|\     /|( (    /|\__   __/| \    /| 
|      | | (__  _____ | |   ) ||   \ | || (__    | |   | ||   \ | |   | |   |  (_/ / 
|      | |  __)(_____)| |   | || (\ \) ||  __)   ( (   ) )| (\ \) |   | |   |   _ (  
|------/ | (          | |   ) || | \   || (       \ \_/ / | | \   |   | |   |  ( \ \ 
|        | (____/\    | (__/  )| )  \  || (____/\  \   /  | )  \  |___) (___|  /  \ (""")
        print("""DOBRO DOŠLI U  PE_DNEVNIK COMMAND BAR
        IMATE 5 OPCIJA:
        1 - UPISATI NOVOG UČENIKA (MOŽE SE SAMO JEDNOM KORISTITI KONTAKIRAJTE ADMINISTRATORA DA PROMJENITE NA pe_dnevniksupport@gmail.com )
        2 - UPISATI NOVI PREDMET (PROMJENJIVO)
        3 - UPISATI NOVI RAZRED (MOŽE SE SAMO JEDNOM KORISTITI KONTAKIRAJTE ADMINISTRATORA DA PROMJENITE NA pe_dnevniksupport@gmail.com)
        print - ISPRINTA PODATKE UČENIKA (samo nakon što ste upisali jedno od prva 3 podatka)
        exit - SAČUVA PODATKE UČENIKA I IZAĐE (samo nakon što ste upisali jedno od prva 3 podatka)""")

        # !IZBAČEN! --// Trepteći ">" character //-- !IZBAČEN!
        komanda = input(">")

        if PrviPuta_sav_print == True:
            if komanda == "1":
                brojUC_UR = int(input("Unesite Broj Učenika:"))
                NoviUC(brojUC_UR)
                PrviPuta_sav_print = False
                komanda = ""
            elif komanda == "2":
                NOVIPREDMET()
                PrviPuta_sav_print = False
                komanda = ""
            elif komanda == "3":
                NoviRAZ()
                PrviPuta_sav_print = False
                komanda = ""
            elif komanda.lower() == "print":
                print_students_info()
                komanda = ""
            elif komanda == "":
                continue
            else:
                print("ERROR")


        if PrviPuta_sav_print == False:
            if komanda == "1":
                brojUC_UR = int(input("Unesite Broj Učenika:"))
                NoviUC(brojUC_UR)
                komanda = ""
            elif komanda == "2":
                NOVIPREDMET()
                komanda = ""
            elif komanda == "3":
                NoviRAZ()
                komanda = ""
            elif komanda.lower() == "print":
                print_students_info()
                komanda = ""
            elif komanda.lower() == "exit":
                #--// save_data() //izbrisati OVO ako hocete da se save-a kada izađete ali to je beskoriso jer u svakoj funkcij ima save_data()//
                IsRunning = False
                komanda = ""
            elif komanda == "":
                continue
            else:
                print("ERROR")


# --// Main program //--
MAIN()