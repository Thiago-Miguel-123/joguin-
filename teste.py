import random

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]

# a.append(b)

# print(a)

# a = ""

# if a:
#     print("tem algo")

# array = [1,2,3]

# for a in array:
#     print(a)

# print(f"ultimo elemento:{a}") 

# array1 = []
# array2:list

# for i in array1:
#     print(1)

# for i in array2:
#     print(2)

# print("dwsafdwsqag")

class teste:
    def __init__(self,valor:int):
        self.valor = valor
        self.listaT = []




# testando = teste(1)

# print(testando.valor)

# testando2 = testando

# testando2.valor = 2

# print(testando.valor)


lista = []

def aplicarCond(valor):

        newTeste = teste(valor)
        lista.append(newTeste)

aplicarCond(1)
aplicarCond(3)
aplicarCond(1)


for l in lista:
    print(l.valor)
    if l.valor == 1:
         lista.remove(l)
         print("renovido") 

for l in lista:
    print(l.valor)
