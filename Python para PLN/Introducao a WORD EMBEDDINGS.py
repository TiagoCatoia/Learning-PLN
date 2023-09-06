'''
 WORD EMBEDDINGS

 Hipótese distribucional
- Palavras tem significados parecidos quando são usadas
em contextos parecidos.
 Modelos de linguagem
- Predizem a próxima palavra, dado um conjunto de
palavras (também pode ser usado para autocorreção de ortografia)
- Exemplo: “O gato corre atrás do ________”
- Qual a próxima palavra? “rato”? “cachorro”? “carro”?
 Os modelos de linguagem são usados para tarefas como
processamento de voz, autocorreção de ortografia, etc.

Oque realmente é: 
 - Uma representação vetorial de uma palavra
 - Uma tradução de texto para números.
 Exemplo: Definição da palavra “rainha” com uma Escala “Gênero”, que vai de -1 a 1:
  - Quanto mais perto de -1, mais feminina.
# Material de Estudo: https://medium.com/turing-talks/word-embedding-fazendo-o-computador-entender-o-significado-das-palavras-92fe22745057

Podem ser adicionadas várias outras dimensões/escalas
 - No exemplo anterior, imagine “rainha” e “rei” em escalas de “Realeza”, “Fruta” e “Violência”, por exemplo.

 E como esses valores são atribuídos?
- A partir de aprendizado de máquina!
- Usa-se algum algoritmo para gerar, a partir do seu
contexto.

E o tamanho ideal do vetor, ou seja, a quantidade
de dimensões?
- Depende do seu corpus/dataset de treinamento: quanto
menor, menos dimensões
- Geralmente é um valor entre 100 e 1000.

Um algoritmo muito utilizado para obter as word
embeddings é chamado Word2Vec.


SIMILARIDADE DO COSSENO

O cálculo da similaridade é feito por meio da
medida do cosseno (f e v no algoritmo são vetores)

Quanto mais próximo de 0: diferentes
Quanto mais próximo de 1: iguais


SPACY – SIMILARIDADE ENTRE PALAVRAS

Por ter um bom e grande modelo de linguagem
para o Português, o spaCy permite avaliar
similaridade entre palavras!

 - Utilizar o método similarity()!

import spacy
nlp = spacy.load("pt_core_news_lg") # Carrega o modelo de linguagem
texto = "conversar falar correr"
doc = nlp(texto) # Armazena o resultado do processamento do texto pelo modelo de linguagem
tokens = [token for token in doc]
print(tokens[0].similarity(tokens[1]))
print(tokens[0].similarity(tokens[2]))
print(tokens[1].similarity(tokens[2]))

print(tokens[0].vector) # Um vetor de números que representa uma palavra ou token específico

Cada valor nesse vetor representa uma dimensão específica no espaço vetorial.
Essas dimensões são aprendidas pelo modelo durante o treinamento e capturam informações sobre a semântica,
contexto e relações entre palavras. O vetor é uma representação densa da palavra, onde valores próximos no
espaço vetorial tendem a ter significados semelhantes ou relacionados.

Quando você calcula a similaridade entre duas palavras ou frases usando esses vetores de palavras (ou embeddings),
 na verdade, está calculando a similaridade entre os pontos nesses espaços vetoriais multidimensionais.

A similaridade entre duas palavras ou frases é frequentemente medida usando métricas como a similaridade de cosseno.
Essa métrica mede o ângulo entre os vetores no espaço vetorial. Quanto mais próximos os vetores estão, ou seja,
quanto menor o ângulo entre eles, maior é a similaridade.

Por exemplo, se você quisesse calcular a similaridade entre duas palavras "cachorro" e "gato",
você pegaria os vetores de palavras correspondentes para cada uma delas e usaria a similaridade de cosseno
para calcular o quão próximos esses vetores estão no espaço vetorial.
Se essas duas palavras forem semanticamente semelhantes, os vetores terão uma alta similaridade de cosseno.


SIMILARIDADE: WORD2VEC

# Artigo: https://arxiv.org/pdf/1301.3781.pdf
O Word2Vec é uma técnica cuja a ideia é
transformar cada token do texto em um vetor
numérico para representação semântica.

- É uma das técnicas mais utilizadas no pré-processamento de textos e aprendizado de word embeddings.
- É possível a utilização dessa técnica dentro do spaCy
- É parecido com o atributo similarity(), porém, como geralmente usam-se modelos maiores e
treinados com mais dados, pode ser mais eficiente o uso do word2vec em outros casos não.

Em vez de usar o modelo de linguagem ("pt_core_news_lg") utilizaremos o modelo que o Word2Vec gerou(o resultado do algoritmo).

Precisamos seguir 3 passos para usar os
princípios do word2vec no spaCy:

1. Encontrar modelos de embeddings treinados

Existem vários modelos de word embeddings
treinados, um para cada fim. Utilizaremos as word
embeddings do NILC, link: http://www.nilc.icmc.usp.br/embeddings

Dois modelos são disponibilizados: CBOW e SKIP-GRAM
- CBOW: modelo utilizado para descobrir a palavra
central de uma sentença, baseado nas palavras que o
cercam.
- SKIP-GRAM: modelo utilizado para descobrir as
palavras de contexto a partir de uma palavra central.

UTILIZANDO O CBOW PARA 50 DIMENSÕES:

# Converter um modelo de incorporação de palavras (word embeddings) em um formato compatível com a biblioteca spaCy
python -m spacy init vectors pt 'C:\\Users\\Principal\Desktop\\Python para PLN\\Words2Vec Similaridade\\cbow_s50.txt' 'C:\\Users\Principal\\Desktop\\Python para PLN\\Words2Vec Similaridade'

 python: Este é o interpretador Python que você está usando para executar o comando.

 -m spacy: Isso significa que você está chamando o módulo spaCy, que é uma biblioteca Python para processamento de linguagem natural.

 init vectors pt: Aqui você está instruindo spaCy a inicializar vetores de palavras para o idioma português (pt).
Essa ação irá configurar um modelo spaCy com vetores de palavras para que você possa usá-los para tarefas
de processamento de linguagem natural em português.

Essa parte do comando é responsável por iniciar o processo de criação de
modelos de vetores de palavras para o idioma português usando a biblioteca spaCy.

# Na pasta 'Words2Vec Similaridade' Ao final, é criada uma pasta com vários itens que são usados pelo spaCy na manipulação dos vetores.
# Agora podemos utilizar o modelo Word2Vec dentro do código com spacy(já que está convertido)

import spacy
from spacy import util as spc_util # spc_util faz com que util passe a chamar spc_util(spc = spacy)

O Módulo 'util' da biblioteca spaCy fornece funções e utilitários auxiliares que são úteis em várias partes do framework spaCy.
Ele contém uma variedade de funcionalidades que podem ajudar a simplificar tarefas comuns de processamento
de linguagem natural, treinamento de modelos e manipulação de dados linguísticos.

palavras_similaridade = "conversar falar"
nlp = spacy.load("pt_core_news_lg")
doc = nlp(palavras_similaridade)
# Armazena o resultado do processamento do texto pelo modelo de linguagem
tokens = [token for token in doc]

print("Similaridade - spaCy: ", tokens[0].similarity(tokens[1]))

# Adequar o código do spaCy para utilização do Word2Vec

pathw2v = 'C:\\Users\\Principal\Desktop\\Python para PLN\\Words2Vec Similaridade' # Caminho da pasta dos itens criados do Word2Vec
# pathw2v: O caminho para a pasta onde os itens do modelo Word2Vec estão localizados.

spc_util.load_model(pathw2v, vocab=nlp.vocab) # faz com que o spacy utilize o modelo do Word2Vec(cbow.50) em vez do modelo de linguagem do nlp('pt_core_news_lg')
# vocab=nlp.vocab: O argumento vocab é opcional e está relacionado ao vocabulário do spaCy (nlp.vocab). 
# Ao passar isso como um argumento, você está instruindo o spaCy a usar o modelo Word2Vec carregado a partir
# da pasta especificada em vez do modelo de linguagem padrão do spaCy ('pt_core_news_lg').

print("Similatirade - Word2Vec: ", tokens[0].similarity(tokens[1]))

 Resultados:
Similaridade - spaCy:  0.7350154519081116
Similatirade - Word2Vec:  0.7504553198814392
Perceba que a similaridade aumentou com o modelo word2vec comparado com o modelo do spaCy.

Agora testando para palavras_similaridade = "justiça trabalho"

palavras_similaridade = "justiça trabalho"
nlp = spacy.load("pt_core_news_lg")  OU  spc_util.load_model("pt_core_news_lg", vocab=nlp.vocab)
doc = nlp(palavras_similaridade)
tokens = [token for token in doc]
print("Similaridade - spaCy: ", tokens[0].similarity(tokens[1]))

pathw2v = 'C:\\Users\\Principal\Desktop\\Python para PLN\\Words2Vec Similaridade'
spc_util.load_model(pathw2v, vocab=nlp.vocab)
print("Similatirade - Word2Vec: ", tokens[0].similarity(tokens[1]))

O modelo do spaCy foi melhor. Veja que vai depender muito do
modelo word2vec treinado e de quantas dimensões os vetores estão
dispostos.
 - Talvez algum outro corpus do CBOW que tenha treinamento no gênero jurídico tenha melhor desempenho.

 

OPERAÇÃO ENTRE VETORES 

MADRI – ESPANHA + FRANÇA ≈ PARIS
# Madri capital de Espanha, mas eu retirei e coloque outro país França, logo temos a capital do outro páis

Precisamos fazer operações entre vetores.
- O spaCy tem um atributo que retorna o vetor do token em
questão: vector

Para as operações com vetores utilizaremos o módulo Numpy
- Instalação: pip install numpy

Para o cálculo da similaridade, utilizaremos o método pronto proveniente do módulo Scikit-learn
- Instalação: pip install –U scikit-learn (Se não for tente: pip install --upgrade scikit-learn)

'''
import spacy
from spacy import util as spc_util
import numpy as np # biblioteca NumPy possui uma coleção de funções matemáticas(operações numéricas) para operar eficientemente nesses arrays.
from sklearn.metrics.pairwise import cosine_similarity # Similaridade do cosseno
''' 
"from sklearn.metrics.pairwise import cosine_similarity" Importa a função cosine_similarity do scikit-learn, 
uma biblioteca de aprendizado de máquina em Python.

O scikit-learn (ou sklearn) fornece várias ferramentas para tarefas de aprendizado de máquina,
incluindo pré-processamento de dados, seleção de modelos e métricas de avaliação.

"scikit", que é uma abreviação de "sci" (ciência) e "kit" (conjunto de ferramentas)
'''
palavras_similaridade = "madri espanha frança paris"
nlp = spacy.load("pt_core_news_lg")
doc = nlp(palavras_similaridade)
tokens = [token for token in doc]

pathw2v = 'C:\\Users\\Principal\Desktop\\Python para PLN\\Words2Vec Similaridade'
spc_util.load_model(pathw2v, vocab=nlp.vocab)

# np.array: transformamos os vetores em arrays do numpy, para realizar as operações vetorias
vetor_resultante = np.array(tokens[0].vector) - np.array(tokens[1].vector) + np.array(tokens[2].vector)

# É necessário remodelar o vetor retornado pelo spaCy, pois ele está em 1 dimensão e para isso o uso da similaridade do cosseno.
# É necessário um vetor de 2 dimensões, para isso utilizamos o numpy possui uma função chamada 'reshape'
# reshape(1 , -1) transforma o vetor de 1 dimensões em 2
# Ler a documentação do scikit-learn
vetor_resultante = vetor_resultante.reshape(1, -1)
vetor_paris = tokens[3].vector.reshape(1, -1)
# 2 dimensões quer dizer lista dentro de lista
similaridade = cosine_similarity(vetor_resultante, vetor_paris)
# Calcular a similaridade do cosseno entre dois vetores.
# O resultado da função é um valor numérico que indica o quão semelhantes ou relacionados dois vetores são com base na direção e magnitude dos vetores.
# A similaridade do cosseno mede o ângulo entre dois vetores em um espaço vetorial.
# Quanto mais próximos os vetores estiverem na direção, mais similares eles são, resultando em um valor de similaridade mais próximo de 1
# Quanto mais diferentes estiverem em direção seu resultando em um valor de similaridade mais próximo de -1
# Se os vetores forem ortogonais (com um ângulo de 90 graus entre eles), a similaridade será 0, indicando completa dissimilaridade.
print(similaridade)

'''
Até agora vimos:
- Teoria do PLN(níveis morfológicos/morfosintáticos/semântico/sintático (semântico usando o spacy))
- Operações em todas as fases linguísticas/representacional(regras-oque queremos fazer)/operacional(código),
linguística(w2v) representacional(regra de similaridade com spacy) implementaciona(código)

Agora veremos na área de PLN/IA sobre APRENDIZADO PROFUNDO
- Um deles é o BERT (Representação de codificadores bidirecionais para transformadores)
'''