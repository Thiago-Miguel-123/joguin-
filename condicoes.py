#banco de dados para condiçoes
#condicoes estarao em uma lista dentro do personagem

#*venenos sao as condicoes mais basicas
# todo veneno dano de veneno igual ao seu valor
# cada atributo dentro do veneno é um valor aplicado ao atributo de mesmo nome do personagem envenenado 
# podendo ser um valor,multiplicação ou divisão
#um atributo não pode ser reduzido ao um valor negativo
# stack é quantas vezes um personagem pode sofrer desse veneno simultaniamente,
# ativa é quando o dano é aplicado, 0 = uma vez por rodada no inicio do turno, 1= uma vez por rodada final do turno
# 2= começo do turno, 3 = fim do turno 
# se o alvo tem resistencia a veneno as modicaçoes a atributos são reduzidos em uma porcentagem igual*#


venenos = [
    {
        'id':0,
        'nome':"veneno basico",
        'valor': 10,
        'forca': 0,
        'agili': 0,
        'sabed': 0,
        'stack': 10,
        'ativa': 1,
        'desc': "veneno basico"
    },
    {
        'id':1,
        'nome':"enfraki",
        'valor': 10,
        'forca': -5,
        'agili': 0,
        'sabed': 0,
        'stack': 5,
        'ativa': 1,
        'desc': "veneno que reduz a força"
    },
    {
        'id':2,
        'nome':"meimaki",
        'valor': 20,
        'forca': ["/",2],
        'agili': ["/",2],
        'sabed': ["/",2],
        'stack': 1,
        'ativa': 1,
        'desc': "veneno que faz alguem perder metade de sua capacidade"
    },
    {
        'id':3,
        'nome':"adreliki",
        'valor': 5,
        'forca': 0,
        'agili': 0,
        'sabed': 0,
        'stack': 20,
        'ativa': 2,
        'desc': "veneno que ativa com picos de adrenalina"
    },
    {
        'id':4,
        'nome':"ultimaki",
        'valor': 80,
        'forca': ["*",5],
        'agili': ["*",2],
        'sabed': 0,
        'stack': 1,
        'ativa': 1,
        'desc': "Toxina extremamente letal que força o corpo alem de seus limites"
    }
]