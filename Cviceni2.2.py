# Program prevede ciselny vstup na 32-bit binarni cislo
vstup = int(input("Zadej cislo: "))
vystup = "{0:032b}".format(vstup)
print(vystup)