# Aula 2: Decoradores (decorators)

def meudecor(function):

    def embala():
        print('Eu estou decorando sua função!')
        function()

    return meudecor

@meudecor    # Adiciona a função decorativa a outra função.
def ola_trox():
    print('Olá Biba!')
          