# para alvo, 0= voce, 1 = inimigo,2 = aliado, 3 = todos aliados, 4 = todos inimigos, 5 = todos, 6 = aliado aleatorio, 7 = inimigo aleatorio
# para tipo, 0= dano, 1= cura, 2= condição, 3= casos especiais
# add sao efeitos adicionais, se None nao tem se um numero igual a tipo
#attr = atributo usado na habilidade, 0 = nenhum, 1 = força, 2= agili, 3= sabed, 4 = vida,5 = vidaMax todos acima são as resis em ordem
#attr segundo numero é como é usado, 1 = +, 2 = -, 3 = +*2, 4 = +/2, 5 = *
#em habilidades de condicao o valor é uma lista com o id da cond,stacks e duracao
listaHabilidades = [
    {
        'id': 0,
        'nome': 'Golpe poderoso',
        'alvo': 1,
        'tipo': 0,
        'tipoDano': "arma",
        'attr': [1,5],
        'valor': 10,
        'add': None,
        'addTipoDano': None,
        'addValor': None,
        'cooldown': 2,
        'desc': "um podereso golpe, causando dano adicional"
    },
    {
        'id': 1,
        'nome': 'Regis',
        'alvo': 2,
        'tipo': 1,
        'tipoDano': None,
        'attr': [3,1],
        'valor': 25,
        'add': None,
        'addTipoDano': None,
        'addValor': None,
        'cooldown': 3,
        'desc': "uma arte magica esquecida, curando o corpo"
    },
    {
        'id': 2,
        'nome': 'Regiuno',
        'alvo': 0,
        'tipo': 1,
        'tipoDano': None,
        'attr': [3,1],
        'valor': 50,
        'add': None,
        'addTipoDano': None,
        'addValor': None,
        'cooldown': 5,
        'desc': "Uma arte ancia, remendando o seu corpo"
    },
    {
        'id': 3,
        'nome': 'Regiali',
        'alvo': 3,
        'tipo': 1,
        'tipoDano': None,
        'attr': [3,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None,
        'cooldown': 3,
        'desc': "uma arte magica esquecida, uma leve e resfrescante brisa, reustarando o corpo de muitos "
    },
    {
        'id': 4,
        'nome': "Lamiali",
        'alvo': 4,
        'tipo': 0,
        'tipoDano': 1,
        'attr' : [0,0],
        'valor' : 25,
        "add": None,
        'addTipoDano': None,
        'addValor': None,
        "cooldown":3,
        "desc":"Uma arte magica esquecida, uma chuva de espadas caindo sobre aqueles que se opõem a tu"
    },
    {
        'id': 5,
        'nome': "iLaki",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 1,
        'attr' : [2,1],
        'valor' : 5,
        "add": 2,
        'addTipoDano': None,
        'addValor': [1,1,2],
        "cooldown":3,
        "desc":"Uma arte magica esquecida, uma minuscula lamina que carrega uma potente toxina"
    },
    {
        'id': 6,
        'nome': "iki",
        'alvo': 1,
        'tipo': 2,
        'tipoDano': None,
        'attr' : [0,0],
        'valor' : [0,1,5],
        "add": None,
        'addTipoDano': None,
        'addValor': None,
        "cooldown":0,
        "desc":"Uma arte magica esquecida, infecta um alvo com uma fraca porem persistente toxina"
    }
]

ListaHabMonstros = [
    {
        'id': 0,
        'nome': "Soco",
        'alvo':1,
        'tipo': 0,
        'tipoDano' : 0,
        'attr' : [1,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 1,
        'nome': "aranhão",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 1,
        'attr' : [1,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 2,
        'nome': "Mordida",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 2,
        'attr' : [1,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 3,
        'nome': "faisca",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 3,
        'attr' : [1,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 4,
        'nome': "choque",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 4,
        'attr' : [1,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 5,
        'nome': "gas",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 5,
        'attr' : [0,0],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 6,
        'nome': "vento gelido",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 6,
        'attr' : [3,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 7,
        'nome': "toque sinistro",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 7,
        'attr' : [3,4],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },
    {
        'id': 8,
        'nome': "ataque direto",
        'alvo': 1,
        'tipo': 0,
        'tipoDano': 8,
        'attr' : [1,1],
        'valor': 15,
        'add': None,
        'addTipoDano': None,
        'addValor': None
    },

]
