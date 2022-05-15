dice = '{hrana}\n,{nic}\n,{stred}\n,{nic}\n,{hrana}\n'.format(hrana='+-------+', nic='|       |', stred='|   o   |', leva='| o     |', prava='|     o |', dve='| o   o |')
x = 1
while True:
    vstup = int(input("Zadej cislo 1-6: "))
    if vstup == 1:
        dice = '{hrana}\n{nic}\n{stred}\n{nic}\n{hrana}\n'.format(hrana='+-------+', nic='|       |', stred='|   o   |', leva='| o     |', prava='|     o |', dve='| o   o |')
        break
    if vstup == 2:
        dice = '{hrana}\n{leva}\n{nic}\n{prava}\n{hrana}\n'.format(hrana='+-------+', nic='|       |', stred='|   o   |', leva='| o     |', prava='|     o |', dve='| o   o |')
        break
    if vstup == 3:
        dice = '{hrana}\n{leva}\n{stred}\n{prava}\n{hrana}\n'.format(hrana='+-------+', nic='|       |', stred='|   o   |', leva='| o     |', prava='|     o |', dve='| o   o |')
        break
    if vstup == 4:
        dice = '{hrana}\n{dve}\n{nic}\n{dve}\n{hrana}\n'.format(hrana='+-------+', nic='|       |', stred='|   o   |', leva='| o     |', prava='|     o |', dve='| o   o |')
        break
    if vstup == 5:
        dice = '{hrana}\n{dve}\n{stred}\n{dve}\n{hrana}\n'.format(hrana='+-------+', nic='|       |', stred='|   o   |', leva='| o     |', prava='|     o |', dve='| o   o |')
        break
    if vstup == 6:
        dice = '{hrana}\n{dve}\n{dve}\n{dve}\n{hrana}\n'.format(hrana='+-------+', nic='|       |', stred='|   o   |', leva='| o     |', prava='|     o |', dve='| o   o |')
        break
    x = 1
print(dice)