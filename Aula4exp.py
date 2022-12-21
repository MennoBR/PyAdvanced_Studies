#Aula 4: Análise de Argumentos.
# Exemplos:

#import getopt = Biblioteca padrão para ARGUMENTOS OPCIONAIS.

'''def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

myfunction('hey', True, 19, 'wow', KEYONE='TEST', KEYTWO=7)'''   

import sys

#Uso: main.py FILENAME

filename = sys.argv[1]
message = sys.argv[2]

len(filename)

with open(filename, 'w+') as f:
    f.write(message)