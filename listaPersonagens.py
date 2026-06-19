#inimigos 

#ia: 
# 0 = aleatoria
# 1 = agressivo, sempre faz o ataque que deixa um inimigo com menos vida 

listaInimigos = [
    {
        "id": 0,
        "nome": "espectro",
        "vida": 30,
        "resis": [5,5,5,0,0,100,0,999],
        "forca": 3,
        "agili": 5,
        "sabed": 8,
        "habilidades": [6,7], #id das habilidades
        "drops": [{'cat':0,'id':4,'chance':5},{'cat':2,'id':3,'chance':55}], #cat,id e porcentagem{
        "ia": 1
    },
    {
        "id": 1,
        "nome": "golem",
        "vida": 100,
        "resis": [2,5,5,-5,-5,0,-5,0],
        "forca": 6,
        "agili": 1,
        "sabed": 1,
        "habilidades": [0,5], #id das habilidades
        "drops": [{'cat':1,'id':2,'chance':15},{'cat':2,'id':1,'chance':25}],
        "ia": 0
    }
]

#aliados

listaAliados = [
    {
        "id": 0,
        "nome": "python",
        "vida": 130,
        "resis": [0,-2,0,0,0,10,-8,0],
        "forca": 5,
        "agili": 2,
        "sabed": 2,
        "habilidades": [], #id das habilidades
        "armasEquipaveis": None, #tipos de arma equipaveis
        "armadurasEquipaveis": [0],
        "armaBase": None,
        "armaduraBase": None
    },
        {
        "id": 1,
        "nome": "Osso duro",
        "vida": 80,
        "resis": [-5,2,10,0,0,30,5,5],
        "forca": 3,
        "agili": 2,
        "sabed": 3,
        "habilidades": [], #id das habilidades
        "armasEquipaveis": [0,1,2,3,4,5], #tipos de arma equipaveis
        "armadurasEquipaveis": [0,1,2,3,4],
        "armaBase": 0,
        "armaduraBase": 1
    },
        {
        "id": 2,
        "nome": "Lenhador",
        "vida": 150,
        "resis": [0,-2,0,0,0,10,-8,0],
        "forca": 8,
        "agili": 1,
        "sabed": 2,
        "habilidades": [], #id das habilidades
        "armasEquipaveis": [1], #tipos de arma equipaveis
        "armadurasEquipaveis": [0,1],
        "armaBase": 2,
        "armaduraBase": 1
    },
        {
        "id": 3,
        "nome": "covarde",
        "vida": 100,
        "resis": [2,2,2,2,2,2,2,2],
        "forca": 2,
        "agili": 12,
        "sabed": 5,
        "habilidades": [], #id das habilidades
        "armasEquipaveis": [0,4], #tipos de arma equipaveis
        "armadurasEquipaveis": [1,2,3,4],
        "armaBase": 1,
        "armaduraBase": 0
    }
]