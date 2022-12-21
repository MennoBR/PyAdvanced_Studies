# Aula 8: Padrão de Design Proxy.
# Um Proxy envolve funcionalidades em algo, 
# E pega funcionalidade da criação do objeto.

#Exemplo de Proxy:

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """Método de interface"""

class Person(IPerson):

    def person_method(self):
        print("Eu sou uma AI.")


class ProxyPerson(IPerson):

     def __init__(self):
        self.person = Person()


     def person.method(self):
         print("Eu sou a funcionalidade Proxy!")
         self.person.person_method()


p1 = Person()
p1.person_method

p2 = ProxyPerson()
p2.person_method

