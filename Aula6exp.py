# Aula 6: Type Hinting.
# Existe uma ferramenta chamada Mypy que checa a consistência de Type hinting.

def mifunc(meuparametro: int) -> str: #Ele espera que seja um int e o transforma numa str.
    return f"{meuparametro + 10}"


def outrafunc(outroparametro: str): #Indica que espera uma str em retorno.
    print(outroparametro)


def alista(param: list[int]) #Indica que espera uma lista de Ints.

outrafunc(mifunc(20)) #Vai printar 30, pois soma com os +10 do parâmetro.