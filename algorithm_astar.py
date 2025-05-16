#matriz de adjacencias da academia, com distancias
grafo = {
    'Esteira': [],
    'Bicicleta': [('Supino', 9), ('Crossover', 3), ('Scott', 7)],
    'Cadeira Extensora': [('Supino', 4), ('Scott', 6), ('Crossover', 9)],
    'Panturrilha': [('Supino', 6), ('Scott',7), ('Crossover',9), ('Banco Reclinável',7)],
    'Smith': [('Supino',8), ('Scott', 6), ('Crossover',8), ('Banco Reclinável', 4)],
    'Leg Press': [('Supino', 4), ('Crossover', 5), ('Scott', 4), ('Banco Reclinável', 9)],
    'Banco Reclinável': [],
    'Crossover': [],
    'Supino': [('Bicicleta', 9), ('Leg Press',4), ('Scott',3), ('Cadeira Extensora', 4), ('Smith', 8), ('Panturrilha',7), ('Banco Reclinável',8)],
    'Scott': [],
}

energia = {
    'Esteira': ,
    'Bicicleta': 7,
    'Cadeira Extensora': ,
    'Panturrilha': ,
    'Smith': ,
    'Leg Press': ,
    'Banco Reclinável': ,
    'Crossover': ,
    'Supino': ,
    'Scott': ,
}

tempo = {
    'Esteira': ,
    'Bicicleta': 5,
    'Cadeira Extensora': ,
    'Panturrilha': ,
    'Smith': ,
    'Leg Press': ,
    'Banco Reclinável': ,
    'Crossover': ,
    'Supino': ,
    'Scott': ,
}

def personalizar_caminho():
    estado_inicial = int(input('Qual é o seu equipamento inicial?'))
    estado_final = int(input('Qual será o equipamento que finalizará seu treino?'))
    intensidade = float(input('Qual a intensidade do treino? \n0.5 = Leve\n1 = Moderado \n2 = Intenso\n')) #Mudar a qtd de máquinas visitadas antes de chegar na final
    peso_distancia = float(input('Qual a importância da distância entre máquinas? (0 a 1):'))
    peso_energia = float(input('Qual a importância da energia gasta em cada exercício? (0 a 1):'))
    peso_tempo = float(input('Qual a importância do tempo de execução de um exercício? (0 a 1):'))
    # esses 3 últimos que são float, acho que vale mais a pena pedir de 1 a 10, e depois converter, pra ficar mais intuitivo


def main():
    personalizar_caminho()

if __name__ == "__main__":
    main()
