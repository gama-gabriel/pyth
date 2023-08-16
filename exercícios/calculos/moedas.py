def moeda(valor):
    valor = str(f'{valor:.2f}')
    valor = valor.replace('.', ',')
    return f'R${valor}'


def dobro(quantia):
    return (quantia * 2)


def metade(quantia):
    return(quantia / 2)


def aumentar(quantia, porcentagem):
    return quantia * (1 + (porcentagem / 100))



def diminuir(quantia, porcentagem):
    return quantia * (1 - (porcentagem / 100))

def resumo (quantia, aumento, diminuicao):
    print('-='*15)
    print (f'{"RESUMO":>15}')
    print('-='*15)
    print(f'Preço analisado: {moeda(quantia)}')
    print(f'A metade de {moeda(quantia)} equivale à {moeda(metade(quantia))}')
    print(f'O dobro de {moeda(quantia)} equivale à {moeda(dobro(quantia))}')
    print(f'Acrescentando {aumento}% = {moeda(aumentar(quantia, aumento))}')
    print(f'Dimunuindo {diminuicao}% = {moeda(diminuir(quantia, diminuicao))}')
    print('-='*15)