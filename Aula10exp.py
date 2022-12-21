# Aula 10: 
# Padrão de design Composto.

# Exemplo com heranças de classe:

from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, empregados):
        """ Implementa na classe infantil """

    @abstractstaticmethod
    def print_department():
        """ Implementa na classe infantil """


class Accounting(IDepartment):

    def __init__(self, empregados):
        self.empregados = empregados

    def print_department(self):
        print(f'Departamento de Contabilidade: {self.empregados}')
        #Agora não há mais classes infantis aqui.


class Development(IDepartment):

    def __init__(self, empregados):
        self.empregados = empregados

    def print_department(self):
        print(f'Departamento de Desenvolvimento: {self.empregados}')


class ParentDepartment(IDepartment):

    def __init__(self, empregados):
        self.empregados = empregados
        self.base_empregados = empregados
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.empregados += dept.empregados      

    def print_department(self):
        print('Departamento Principal')
        print(f'Base de empregados do Departamento Principal: {self.base_empregados}')
        for dept in self.sub_depts:
            dept.print_department()
        print(f'Número total de empregados: {self.empregados}')  


dept1 = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()