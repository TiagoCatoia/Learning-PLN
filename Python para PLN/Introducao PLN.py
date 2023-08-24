import nltk
from nltk.tokenize import RegexpTokenizer

# Especificar a codificação correta ao abrir o arquivo usando o argumento encoding. No seu caso UTF-8. 
arquivo = open('C:\\Users\\Principal\\Desktop\\Python para PLN\\corpus.txt', 'r', encoding='utf-8')
texto = arquivo.read()

''' https://drive.google.com/drive/folders/141dt2jxvhx2_JNZqwZLV-ojJtf1KsuPq

TOKENIZAÇÃO

 -Tokenização é o processo de dividir um texto
em unidades individuais, chamadas tokens.
Um token pode ser uma palavra, um número,
um símbolo de pontuação ou qualquer unidade significativa de texto.

tokens = nltk.word_tokenize(texto)
print(tokens)

PADRÃO DE BUSCA: EXPRESSÕES REGULARES

SEM PONTUAÇÂO:

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(texto)
print(tokens)

OUTROS PADRÕES DE BUSCA/EXPRESSÕES REGULARES https://www.w3schools.com/python/python_regex.asp

SEM PONTUAÇÃO E NUMEAIS:

tokenizer = RegexpTokenizer(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)
print(tokens)

FREQUÊNCIA/CONTAGEM

 -Uso da classe FreqDist()
A função most_common() ordena a frequência dos
tokens.

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(texto)

frequencia = nltk.FreqDist(tokens)
print(tokens)
print(frequencia) # <FreqDist with 87 samples and 117 outcomes>
print(frequencia.most_common()) # print(frequencia.most_common(5) para ver os 5 com maior frequência)


LIST COMPREHESION

 -Caso o objetivo da contagem seja de
palavras iguais, por exemplo, é necessário usar as
funções lower() ou upper() para normalizar
os tokens, se não 'A' e 'a' serão considerados diferentes.


tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(texto)
frequencia = nltk.FreqDist(word.lower() for word in tokens)
print(tokens)
print(frequencia) # <FreqDist with 87 samples and 117 outcomes>
print(frequencia.most_common()) # print(frequencia.most_common(5) para ver os 5 com maior frequência)

STOPWORDS

 -São palavras que podem ser
consideradas irrelevantes para um certo
resultado buscado.
ex: Artigos, preposições, conjunções, por exemplo...

Na prática: Facilita o entendimento da máquina
ex: na frase "O celular está tocando" oque realmente importa é "celular tocando"

FREQUÊNCIA DE PALAVRAS SEM STOPWORDS:

tokenizer = RegexpTokenizer(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)
stopwords = nltk.corpus.stopwords.words('portuguese')
frequencia = nltk.FreqDist(word.lower() for word in tokens if word.lower() not in stopwords)
print(frequencia)
print(frequencia.most_common())

N-GRAMAS

 -Com a lista de tokens, é possível ter os n-gramas
necessários para qualquer análise.
Por exemplo: Predição da próxima palavra de uma
sentença em smartphones.

- Bigramas: from nltk import bigrams
- Trigramas: from nltk import trigrams
- 4-gram ou mais: from nltk import ngrams
ex: Texto = "A casa de Pedro fica próxima de Carlos"
Possíveis Bigramas "A casa", "casa de", Pedro fica"...
Possíveis Trigramas "A casa de", "casa de Pedro"...
'''
from nltk import bigrams
tokenizer = RegexpTokenizer(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)
print(list(bigrams(tokens)))
from nltk import ngrams
print(list(ngrams(tokens, 4)))

arquivo.close()

