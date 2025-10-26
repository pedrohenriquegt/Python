itens = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 40)
print(f'{'LISTAGEM DE PRECOS':^40}')
print('-' * 40)
for i in range(0, len(itens)):
    if i % 2 == 0:
        print(f'{itens[i]:.<30}', end='')
    else:
        print(f'R$ {itens[i]:>6.2f}')
print('-' * 40)