# Aula 7: Padrões de desenho de fábrica.
#- São para ser uados apenas em projetos grandes, com muitos arquivos e módulos.

from abc import ABCMeta, abstractstaticmethod

class IPerson(meta=ABCMeta): 
       """Se lgo está em interface chamamos de 'I'. no caso 'IPerson'.
o meta=abcmeta, significa que isso é abstrato e não pode ser criado nada com ele."""

@abstractstaticmethod   
def person_method():
    """Método de Interface"""

#p1 = IPerson()#
#p1.person_method() #Não seria possível instanciar, pois é um método ABSTRATO!    


class Estudante(IPerson): #Ténica para alterar o abstrato, 'Bypassar'.

    def __init__(self):
        self.nome = "Nome de Estudante"

    def person_method(self):
        print('Eu sou estudante!')    


class Professor(IPerson):

    def __init__(self):
        self.nome = "Nome do Professor"
        print('Eu sou Professor!')       

s1 = Estudante()
s1.person_method()

p1 = Professor()
p1.person.method() 

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type  == "Estudante":
            return Estudante()
        if person_type == "Professor":
            return Professor()
        print('Erro de digitação!')
        return -1  


if __name__ == "__main__":
    choice =  input('Que tipo de vadastro gostaria de fazer?\n')
    pessoa = PersonFactory.build.person(choice) 
    person.person_method()           
