#Python Avançado: Geradores
# Sequencia de 1 a 9,000,000 com raíz cúbica sequencial.

import sys 

def meugerador(n):
    for x in range(n):
        yield x ** 3

valores = meugerador(9000000)

print(next(valores))
print(next(valores))
print(next(valores))
print(next(valores))
print(next(valores))
print(next(valores))
print(f'A quantidade de valores é de: {sys.getsizeof(valores)}', end='')