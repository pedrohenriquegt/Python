from calendar import isleap
from datetime import date

ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year

if isleap(ano):
    print('O ano {} e BISSEXTO'.format(ano))
else:
    print('O ano {} nao e BISSEXTO'.format(ano))

"""if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0"""  # Outro jeito de fazer o calculo de ano bissexto