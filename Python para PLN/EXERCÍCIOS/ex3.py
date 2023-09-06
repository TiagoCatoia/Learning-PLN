'''
Faça uma análise descritiva completa do nosso
corpus de teste, utilizando as funções do NLTK.

Exemplos de atributos:
- Quantidade de tokens
- Quantidade de sentenças
- Quantidade de substantivos, adjetivos
- Quantidade de palavras com o mesmo radical
- Palavras mais frequentes do corpus
'''
import nltk
from nltk.corpus import mac_morpho
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger
from nltk.tokenize import RegexpTokenizer
arquivo = open('C:\\Users\\Principal\\Desktop\\Python para PLN\\corpus.txt', 'r', encoding='utf-8')
texto = arquivo.read()

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(texto)
print(f"Quantidade de tokens: {len(tokens)}")

tokenizer = RegexpTokenizer(r'\W')
tokens = tokenizer.tokenize(texto)
countSents = 0
for i in range(len(tokens)):
    if tokens[i] == '.':
        countSents += 1
print(f"Quantidade de sentenças: {countSents}")
'''
#tokens = nltk.word_tokenize(texto)
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(texto)
etiq_padrao = DefaultTagger('N')
sents_treinadoras = mac_morpho.tagged_sents()
etiq = UnigramTagger(sents_treinadoras, backoff=etiq_padrao)
tags = etiq.tag(tokens)
count_substantivos = 0
count_adjetivos = 0
for i in range(len(tags)):
    if tags[i][1] == 'N' or tags[i][1] == 'NPROP':
        count_substantivos += 1
    elif tags[i][1] == 'ADJ':
        count_adjetivos += 1
print(f"Quantidade de substantivos: {count_substantivos}")
print(f"Quantidade de adjetivos: {count_adjetivos}")
'''
tokenizer = RegexpTokenizer(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)
stemmer = nltk.RSLPStemmer()
lista_radicais = []
count_mesmo_radical = 0
for i in range(len(tokens)):
    stemmer_token = stemmer.stem(tokens[i])
    if stemmer_token not in lista_radicais:
        lista_radicais.append(stemmer_token)
    else:
        count_mesmo_radical += 1
print(f"Quantidade de palavras com o mesmo radical: {count_mesmo_radical}")

frequencia = nltk.FreqDist(words.lower() for words in tokens)
print("Palavras mais frequentes do corpus:", end=" ")
for i in range(5):
    print(f"{frequencia.most_common()[i][0]} |", end=" ")
arquivo.close()