import random

int; spatne = 0
int; spravne = 0
int; celkem = 0

cislo = random.randint(1,5)

print("""

  __  __           _            __  __ _           _ 
 |  \/  |         | |          |  \/  (_)         | |
 | \  / | __ _ ___| |_ ___ _ __| \  / |_ _ __   __| |
 | |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` |
 | |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| |
 |_|  |_|\__,_|___/\__\___|_|  |_|  |_|_|_| |_|\__,_|
                                                     
                                                     
""")

jmeno = input("Zadej jmeno hrace: ")
if jmeno == "":
    jmeno = "Player"

print("\nVitej ve hre MasterMind", jmeno ,".\nPro ukonceni hry napis 'KONEC'\n")

nekonecno = True
while (nekonecno):
    print("Myslim si cislo...")
    vstup = input("")
    if vstup == "KONEC":
        break
    else:
        vstup = int(vstup)
    if cislo != vstup and vstup!= "KONEC":
        spatne = spatne + 1
        celkem = celkem + 1
        print("Spatne, hadej znovu nebo napis 'KONEC'!")
    elif cislo == vstup:
        spravne = spravne + 1
        celkem = celkem + 1
        print("Spravne! Vymyslim nove cislo...")
        cislo = random.randint(1,5)
print("\nSpravnych odpovedi:", spravne)
print("Spatnych odpovedi:", spatne)
print("Celkem jsi hadal:", celkem)
