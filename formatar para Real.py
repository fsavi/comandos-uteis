def moeda (valor=0, moeda='R$'):
    return f'{moeda}{valor:_.2f}'.replace('.', ',').replace('_', '.')

lucro = 1500

print(f'{moeda(lucro)}')
