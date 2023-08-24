'''
1. Dado o arquivo qbdata.txt, retorne o rating de
cada QB na forma “nome do QB teve valor XX.X’

- Percebe-se que as informações que são requeridas são a
primeira e a última de cada linha;
- É visto também que a separação entre as informações é
feita por meio de espaços ou tabulação;
- Algoritmo: para cada linha, fazer a separação dela e por
meio do slicing de listas, pegar a primeira e a última
informação e montar a string final.
'''
arquivo = open('C:\\Users\\Principal\\Desktop\\Python para PLN\\EXERCÍCIOS\\qbdata.txt', 'r')

rating = arquivo.readline()
primeiraLinha = True
while rating:
    rating = rating.split()
    rating = rating[:1] + rating[1:2] + rating[len(rating)-1:]
    if primeiraLinha == False:
        print(f"{rating[0]} {rating[1]} teve valor {rating[2]}")
    primeiraLinha = False
    rating = arquivo.readline()

arquivo.close()