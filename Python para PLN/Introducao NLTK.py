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

from nltk import bigrams
tokenizer = RegexpTokenizer(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)
print(list(bigrams(tokens)))
from nltk import ngrams
print(list(ngrams(tokens, 4)))


 -Os n-gramas são importantes para várias
análises. Um exemplo, no nosso caso, seria
conseguir as entidades nomeadas do nosso trecho.

from nltk import bigrams, trigrams
tokenizer = RegexpTokenizer(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)
bigramas_lista = list(bigrams (tokens))
trigramas_lista = list(trigrams (tokens))
for info in bigramas_lista:
    if (info[0][0].isupper() and info [1][0].isupper()):
        print(info)
for info in trigramas_lista:
    if (info[0][0].isupper() and info[1][0].isupper() and info[2][0].isupper()):
        print(info)

        
STEMMING 
 -Consiste em reduzir a palavra ao
seu Radical.
amig: amigo, amiga, amigão
gat: gato, gata, gatos
prop: propõem, propuseram, propondo
 -O NLTK tem implementado vários algoritmos de
para stemmer:
RSLP, Porter, ISRI, Lancaster, Snowball
RSLP – Removedor de Sufixos da Língua Portuguesa
'''
stemmer = nltk.RSLPStemmer()
print(stemmer.stem('amigão'))
print(stemmer.stem('propuseram'))
print(stemmer.stem('propõem'))
print(stemmer.stem('propondo'))

'''
LEMATIZAÇÃO:
 -Consiste em reduzir a palavra à
sua Forma Canônica, levando em conta sua
classe gramatical.
propor: propõem, propuseram, propondo
estudar: estudando, estudioso, estudei

 -Ainta não tem um lematizador para o Português bom o bastante.
Tentativa: WordNet Lemmatizer
Funciona somente para o inglês...
Mas fiquem tranquilos, no spaCy tem para o português...

lemmatizer = nltk.stem.WordNetLemmatizer()
lemmatizer.lemmatize('studying', pos='v')
= study
lemmatizer.lemmatize('sings', pos='v')
= sing

ETIQUETADORES
 -O NLTK possui dois corpus que servem como
base para o etiquetador em português: o
Floresta e o Mac Morpho.
 -Para o inglês já existe um etiquetador padrão
treinado: o nltk.pos_tag().
 -Como resultado, os etiquetadores retornam uma
tupla (‘palavra’, ‘classe gramatical’) classe gramatical depende do treinamento

from nltk.corpus import mac_morpho
from nltk.tag import UnigramTagger
tokens = nltk.word_tokenizer(texto)
sentencas_treinadoras = mac_morpho.tagged_sents()
etiq = UnigramTagger.(sentencas_treinadoras) // treinamento das sentencas_treinadoras e armazena o modelo
tags = etiq.tag(tokens) // etiquetar o meu texto utilizando oque aprendeu
print(tags)

Uma solução para evitar os 'None' é pré-classificar todas as palavras
do texto como substantivos (N)

from nltk.corpus import mac_morpho
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger // pacote usado para definir tag padrao
tokens = nltk.word_tokenizer(texto)
etiq_padrao = DefaultTagger('N')
sentencas_treinadoras = mac_morpho.tagged_sents()
etiq = UnigramTagger.(sentencas_treinadoras, backoff=etiq_padrao) // treinamento das sentencas_treinadoras e armazena o modelo
tags = etiq.tag(tokens) // etiquetar o meu texto utilizando oque aprendeu
print(tags) // lista de tuplas

É possível, então, fazer várias manipulações com
a lista de tuplas resultante:

- Análises descritivas
- Análises sintáticas
- Chunking
- Reconhecimento de Entidades Nomeadas, etc...
ex:  Reconhecimento de Entidades Nomeadas

from nltk.chunk import RegexpParser
pattern = 'NP:{<NPROP><NPROP>|<N><N>}'
analiseGramatical = RegexParser(pattern)
arvore = analiseGramatical.parse(tags)
print(arvore)
arvore.draw()
-------------------------------------------------------------------------------------------------------------------------------

NLTK (Natural Language Toolkit): O NLTK é uma biblioteca em Python que fornece ferramentas
e recursos para a análise de texto e processamento de linguagem natural.
Ele é amplamente utilizado para tarefas como tokenização, lematização,
análise gramatical, extração de informações e muito mais. 
O NLTK oferece uma ampla gama de funcionalidades e é frequentemente
usado para fins educacionais e de pesquisa.

spaCy: O spaCy é outra biblioteca de processamento de linguagem natural
em Python que se concentra em oferecer alto desempenho e eficiência.
Ele é conhecido por ser rápido e eficaz para tarefas de NLP em grande escala.
O spaCy também oferece recursos como tokenização, lematização, análise sintática,
reconhecimento de entidades nomeadas, entre outros. Uma característica notável
do spaCy é sua capacidade de fornecer modelos treinados para várias línguas,
que podem ser usados para análise de texto em diferentes contextos.

'''
arquivo.close()


