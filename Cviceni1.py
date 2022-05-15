import os
from datetime import date

jmeno = input("Jméno: ")
rok = input("Rok narození: ")
adresa = input("Adresa: ")
# Zjisti aktualni rok
aktualni_rok = date.today().year
separator = "="

int; vek = int(aktualni_rok) - int(rok)

clear = lambda: os.system('cls')
clear()

print(separator*20)
print("Jméno: ", jmeno)
print("Věk: ", vek)
print("Adresa:", adresa)
print(separator*20)