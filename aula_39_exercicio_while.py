"""
Iterando strings com while
"""

nome = 'Maria Helena'

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{nome[indice]}'
    indice += 1

    if indice == len(nome):
        novo_nome += '*'
        print(f'nova string gerada: {novo_nome}')