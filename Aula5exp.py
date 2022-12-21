#Encapsulamento e "Data Hiding"(Escondendo arquivos).

class Pessoa:

    def __init__(self, nome, idade, genero):
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero

    @property #Transforma em propriedade.
    def Nome(self):
        return self.__nome    

    @Nome.setter  #.setter permite passar por cima do método com o mesmo nome.
    def Nome(self, valor):
        self.__nome = valor     

    
    @staticmethod # Não é relacionado a um objeto específico. Sempre importante 
    #definir que é um método estático, mesmo quando não se está usando a função.
    def mymethod():
        print('Bem vindo T-1000')


Pessoa.mymethod() #Assim não precisamos de um objeto para chamar a função.        

p1 = Pessoa('Rick', 78, 'm')
print(p1.Nome)        