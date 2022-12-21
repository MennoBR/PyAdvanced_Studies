#Aula 9: Padrão de design Singleton.
# Basicamente Singleton é um padrão de projeto criacional, que garante que
# Apenas um objeto desse tipo exista e forneça um único ponto de acesso
# A ele para qualquer outro código.

#Exemplo:

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod                   #Método abstrato para implementação.
    def print_data():
        """Implementando na sub classe"""

class PersonSingleton(IPerson):

    __instance = None

    @staticmethod                            #Usando método estático de novo.
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, nome, idade):           #Definindo que não pode ser reutilizada.
        if PersonSingleton.__instance != None:
            raise Exception('Singleton Não pode ser atribuído mais de uma vez.')
        else:
            self.nome = nome
            self.idade = idade
            PersonSingleton.__instance = self 

@staticmethod
def print_data():
    print(f'Nome: {PersonSingleton.__instance.nome}, Idade: {PersonSingleton.__instance.idade}')


p = PersonSingleton('Carla', 30)
print(p)
p.print_data() 

