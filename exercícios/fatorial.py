def fatorial(valor, show = False):
    n = 1
    for i in range (valor, 0, -1):
        n *= i
        if show == True:
            if i == 1:
                print(f'{i} = ', end = '')
            else:
                print(f'{i} x ', end = '')
    return(n)


print(fatorial(6, True))
