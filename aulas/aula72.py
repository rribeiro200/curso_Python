print()

def multiplica(*args):

    total = 1
    
    for numero in args:
        total = total * numero
    return total

multiplicação = multiplica(10, 2, 3, 4, 5)
print(multiplicação)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))



print()
print('-----------------------')