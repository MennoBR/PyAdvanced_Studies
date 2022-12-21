#funções avançadas(métodos mágicos) com dupla __ :
'''class Pessoa:    

     def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

     def __del__(self):
        print('Objeto está sendo destruído!')

 
p = Pessoa('Marcos', 27)
del p'''

class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)


    def __repr__(self):
        return f"X: {self.x}, V: {self.y}"    


v1 = Vetor(10, 20)
v2 = Vetor(50, 60)
v3 = v1 + v2 

print(v3.x)
print(v3.y)

    