'''
Dada uma palavra, encontrar no córpus as 3
outras palavras que mais são próximas
semanticamente e as 3 palavras que são mais
distantes.

- Faça o teste com o modelo do próprio spaCy e algum
modelo word2vec do NILC Embeddings
'''

import spacy

arquivo = open("C:\\Users\\Principal\\Desktop\\Python para PLN\\corpus.txt", 'r', encoding='utf-8')
corpus = arquivo.read()

print("Córpus: ")
print(corpus)
palavra = input("Digite uma palavra para ver as 3 mais próximas e as 3 mais distantes semanticamente do corpus: ")

# Carrega o modelo no corpus
nlp = spacy.load("pt_core_news_lg")
# Passa o corpus para o modelo spaCy que foi carregado
doc = nlp(corpus)

# Passa a palavra inserida pelo usuário para o modelo spaCy para que ela seja representada como um objeto Doc(assim como o foi feito com o corpus)
doc_palavra = nlp(palavra)

tokens = [token for token in doc if token.is_alpha]

# UTILIZANDO O SPACY APENAS
'''
palv_prox_semanticamente = []
palv_dist_semanticamente = []

# Use a primeira palavra do corpus como base para comparação
base_token = tokens[0]

# Defino valores impossíveis para comparação inicial, e que são resetados no loop
maisProx = -2 
maisDist = 2
for i in range(0, 3):
    palv_prox_semanticamente.append(base_token) # adiciona nas listas o valor base para fazer a substituição caso a condição ocorra
    palv_dist_semanticamente.append(base_token)
    maisProx = -2 
    maisDist = 2
    for token in tokens:
        similaridade = doc_palavra.similarity(token)
        print(similaridade, "   ", token)

        # token.text not in [palv.text for palv in palv_prox_semanticamente] -> Garante que apenas o texto do token seja considerado na verificação
        if similaridade > maisProx and token.text not in [palv.text for palv in palv_prox_semanticamente]:
            maisProx = similaridade
            palv_prox_semanticamente[i] = token

        elif similaridade < maisDist and token.text not in [palv.text for palv in palv_dist_semanticamente]:
            maisDist = similaridade
            palv_dist_semanticamente[i] = token

print("\n")
print("Palavras mais próximas sintaticamente: ", palv_prox_semanticamente)
print("Palavras mais distantes sintaticamente: ", palv_dist_semanticamente)



# PROBLEMA ENCONTRADO: "hoje" 3 'de' do corpus é adicionado mesmo com a verificação not in (considerados tokens diferentes???)

# Outra maneira criar um dicionário com os tokens(k) e similaridade(v) e mostrar os 3 maiores/menores
# ou adcionar todos os valores em uma lista e ordena-los


'''
# UTILIZANDO O SPACY E O WORD2VEC

# Iniciar o processo de criação de modelos:
# python -m spacy init vectors pt 'C:\\Users\\Principal\Desktop\\Python para PLN\\Words2Vec Similaridade\\cbow_s50.txt' 'C:\\Users\Principal\\Desktop\\Python para PLN\\Words2Vec Similaridade'

from spacy import util as spc_util

# Adequar o código do spaCy para utilização do Word2Vec
pathw2v = 'C:\\Users\\Principal\Desktop\\Python para PLN\\Words2Vec Similaridade'

# Faz com que o spacy utilize o modelo do Word2Vec(cbow.50) em vez do modelo de linguagem do nlp('pt_core_news_lg')
spc_util.load_model(pathw2v, vocab=nlp.vocab)

# Modelo do Word2Vec(cbow.50) já carregado 
palv_prox_semanticamente = []
palv_dist_semanticamente = []
base_token = tokens[0]

maisProx = -2 
maisDist = 2
for i in range(0, 3):
    palv_prox_semanticamente.append(base_token)
    palv_dist_semanticamente.append(base_token)
    maisProx = -2 
    maisDist = 2
    for token in tokens:
        similaridade = doc_palavra.similarity(token)
        print(similaridade, "   ", token)

        if similaridade > maisProx and token.text not in [palv.text for palv in palv_prox_semanticamente]:
            maisProx = similaridade
            palv_prox_semanticamente[i] = token

        elif similaridade < maisDist and token.text not in [palv.text for palv in palv_dist_semanticamente]:
            maisDist = similaridade
            palv_dist_semanticamente[i] = token

print("\n")
print("Palavras mais próximas sintaticamente: ", palv_prox_semanticamente)
print("Palavras mais distantes sintaticamente: ", palv_dist_semanticamente)


arquivo.close()