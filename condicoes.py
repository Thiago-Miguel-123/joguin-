#banco de dados para condiçoes
#condicoes estarao em uma lista dentro do personagem

#*basico sobre condiçoes
# toda condição tem um tipo, 0 = da dano, 1 = cura, 3= nenhum dos dois
#tipo dano é somente usado por tipos 1, sendo o id do tipo do dano ex:5 é dano de veneno
# cada atributo dentro da condição é um valor aplicado ao atributo de mesmo nome do personagem afetado
# podendo ser um None, caso esse atributo não seja afetado, ou uma lista onde o [0] é o simbolo do operador e [1] sendo o valor
#um atributo não pode ser reduzido ao um valor negativo
# stack é quantas vezes um personagem pode sofrer de instancias da mesma condição simultaniamente,
# ativa é quando o dano\cura é aplicado, 0 = uma vez por rodada no inicio do turno, 1= uma vez por rodada final do turno
# 2= começo do turno, 3 = fim do turno, 5 = quando alvo leva dano uma vez por rodada, 6= quando leva dano
# se o alvo tem resistencia ao tipo de dano da caondição as modicaçoes a atributos são reduzidos em uma porcentagem igual
# esp são efeitos especiais e unicos, nao serao implementados agora mais futuramente serao efeitos como multiplos turnos, fazer todasa as habiladades afetarem alvos especificos e perder turno em certas condicoes*#


condicoes = [
    {
        'id':0,
        'nome':"veneno basico",
        'tipo': 0,
        'tipoDano': 5,
        'valor': 10,
        'forca': None,
        'agili': None,
        'sabed': None,
        'resis': [0,0,0,0,0,0,0,0],
        'stack': 10,
        'ativa': 1,
        'esp': None,
        'desc': "veneno basico"
    },
    {
        'id':1,
        'nome':"enfraki",
        'tipo': 0,
        'tipoDano': 5,
        'valor': 10,
        'forca': ['-',5],
        'agili': None,
        'sabed': None,
        'resis': [5,5,5, 0, 0, 0, 0, 0],
        'stack': 5,
        'ativa': 1,
        'esp': None,
        'desc': "veneno que reduz a força"
    },
    {
        'id':2,
        'nome':"meimaki",
        'tipo': 0,
        'tipoDano': 5,
        'valor': 20,
        'forca': ["/",2],
        'agili': ["/",2],
        'sabed': ["/",2],
        'resis': [-5, -5, -5, -5, -5, -5, -5, -5],
        'stack': 1,
        'ativa': 1,
        'esp': None,
        'desc': "veneno que faz alguem perder metade de sua capacidade"
    },
    {
        'id':3,
        'nome':"adreliki",
        'tipo': 0,
        'tipoDano': 5,
        'valor': 5,
        'forca': None,
        'agili': None,
        'sabed': None,
        'resis': [0, 0, 0, 0, 0, 0, 0, 0],
        'stack': 20,
        'ativa': 2,
        'esp': None,
        'desc': "veneno que ativa com picos de adrenalina"
    },
    {
        'id':4,
        'nome':"ultimaki",
        'tipo': 0,
        'tipoDano': 5,
        'valor': 100,
        'forca': ["*",5],
        'agili': ["*",2],
        'sabed': None,
        'resis': [25, 25, 25, 0, 0, 0, 0, 0],
        'stack': 1,
        'ativa': 1,
        'esp': None,
        'desc': "Toxina extremamente letal que força o corpo alem de seus limites"
    },
    {
        'id': 5,
        'nome': "regillar",
        'tipo': 1,
        'tipoDano': None,
        'valor': 10,
        'forca': None,
        'agili': None,
        'sabed': None,
        'resis': [0, 0, 0, 0, 0, 0, 0, 0],
        'stack': 3,
        'ativa': 1,
        'esp': None,
        'desc': "restaura o corpo lentamente"
    },
    {
        'id': 6,
        'nome': "inflamavel",
        'tipo': 3,
        'tipoDano': None,
        'valor': 10,
        'forca': None,
        'agili': None,
        'sabed': None,
        'resis': [0, 0, 0, -20, 0, 0, 0, 0],
        'stack': 3,
        'ativa': None,
        'esp': None,#futuramente tambem ira colocar o alvo em chamas caso acertado por ataques de fogo
        'desc': "restaura o corpo lentamente"
    },

]