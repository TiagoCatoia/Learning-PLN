import spacy

arquivo = open('corpus.txt', 'r', encoding='utf-8')
texto = arquivo.read()
'''
SPACY

- Biblioteca Python para processamento de textos
- Escala industrial
- Feito para uso em produção
- Criação de aplicações que conseguem processar um
grande volume de dados

Para o spaCy conseguir realizar suas funções, é
necessário que um modelo de linguagem esteja
presente.
- Modelos pré-treinados
- Entidades Nomeadas
- Classes gramaticais
- Dependências sintáticas

- Parecido com os córpus que utilizamos como
treinamento no NLTK

Para o uso das funções poderosas do spaCy, é
preciso entender dois objetos importantes:
- O objeto Doc
- O objeto Token

- Um Doc é um conjunto de tokens
- Métodos da classe Doc levam em consideração a
manipulação desses tokens
- Exemplo: quantidade de tokens no documento

- Um Token é o token que aprendemos na aula de
NLTK: pode ser uma palavra, uma pontuação,
numeral, espaços...

Assim, antes de qualquer utilização das funções
do spaCy, deve-se criar a variável que vai
guardar o modelo de linguagem

* IMPORTANTE: no NLTK era utilizado sempre a lista de
tokens, mas aqui no spaCy, o parâmetro é sempre a string
do texto!
Portanto, a partir de agora, todas as funções
serão provenientes da variável doc!
'''
nlp = spacy.load('pt_core_news_lg') # variável (nlp) que guarda o modelo de linguagem
doc = nlp(texto)
# Doc armazenar o resultado do processamento do texto pelo modelo spaCy. O objeto doc é um objeto especial do spaCy
# que contém todas as informações e análises linguísticas extraídas do texto, como tokens, análise sintática, entidades nomeadas, etc.
''' 

TOKENIZAÇÃO

tokens = [token.orth_ for token in doc] # .orth_ Retorna uma lista de tokens no formato de strings
print(tokens)
print(type(tokens[0])) # <class 'str'>

Em nltk utilizavamos as expreções regulares, no spacy podemos fazer:

# .orth_ para retornar uma lista de tokens em string
tokens = [token.orth_ for token in doc if token.is_digit] # if token.is_digit retorna apenas dígito numéricos
tokens = [token.orth_ for token in doc if token.is_punct] # if token.is_punct retorna apenas pontuação
tokens = [token.orth_ for token in doc if token.is_alpha] # if token.is_alpha retorna apenas palavras
print(tokens)

# ATRIBUTOS DO SPACY: https://spacy.io/api/token#attributes

Retorno com tipos de tokens diferentes:
- Pontuação esquerda ou direita
- Parênteses e colchetes
- Espaços
- Símbolos financeiros
- Números (10.9, 10, “dez”)
- E-mail
- Stopwords...


STEMMING E LEMATIZAÇÃO

Olha que interessante (e surpreendente): o spaCy
não tem um stemmer padrão...

- Porém, o spaCy tem um lematizador!
- O inverso do NLTK, pelo menos para o Português!

- Lematizar é simples: só utilizar o atributo: lemma_

lemmas = [token.lemma_ for token in doc if token.pos_ == 'VERB'] # ver o lemma de cada token
print(lemmas) # retorna uma lista de lemmas de verbos

O atributo: pos_ 
 - é referente ao Part-Of-Speech, ou
simplesmente, a classe gramatical do token.

Vale ressaltar que a lematização geralmente remete
à forma canônica da palavra para os verbos, então é
necessária essa condição.

etiquetas = [(token.orth_, token.pos_) for token in doc if token.is_alpha]
print(etiquetas)

# CONJUNTO DE ETIQUETAS: https://universaldependencies.org/docs/u/pos/

O atributo: morph
 - Retorna Características mais Morfológicas dos tokens.

etiquetas = [(token.orth_, token.morph) for token in doc]
print(etiquetas)


ENTIDADES NOMEADAS

Propriedade: ents na variável doc.

entidades = list(doc.ents)
print(entidades)

entidades_detalhadas = [(entidades, entidades.label_) for entidades in doc.ents]
print(entidades_detalhadas)

É possível visualizar essas entidades nomeadas
de forma gráfica, por meio do displaCy.

from spacy import displacy
html = displacy.render(doc, style='ent')
output_path = Path("entidades_nomeadas.html")
output_path = open('w', encoding='utf-8').write(html)

from spacy import displacy
html = displacy.render(doc, style='ent')
output_path = open('C:\\Users\\Principal\\Desktop\\Python para PLN\\corpus.txt', 'w', encoding='utf-8')
output_path.write(html)
output_path.close()
# Grava no arquivo 'corpus.txt' no diretório especificado. Você pode verificar isso abrindo manualmente o arquivo 'corpus.txt
# Layout modificável: https://spacy.io/usage/visualizers#ent


ANÁLISE SINTÁTICA

 - O atributo dep_ retorna a dependência sintática
do token em questão

sintatica = [(token.orth_, token.dep_) for token in doc]
print(sintatica)

# CONJUNTO DE ETIQUETAS: https://emorynlp.github.io/nlp4j/components/dependency-parsing.html

 - O spaCy também permite a visualização das
dependências de forma gráfica pelo displaCy:

from spacy import displacy
svg = displacy.render(doc, style='dep')
output_path = open('C:\\Users\\Principal\\Desktop\\Python para PLN\\corpus.txt', 'w', encoding='utf-8')
output_path.write(svg)
output_path.close()
# Grava no arquivo 'corpus.txt' no diretório especificado. Você pode verificar isso abrindo manualmente o arquivo 'corpus.txt
# ex: https://drive.google.com/file/d/1kmzR3iE9uvb75VIHCPZh3QcIKrSLsqbH/view


 - O spaCy contém dois sites onde podem ser feitas
as análises de entidades nomeadas e de
dependências de forma bem simples:

- Visualizador de Entidades Nomeadas: https://explosion.ai/demos/displacy-ent

- Visualizador de Dependências: https://explosion.ai/demos/displacy

- Basta selecionar o modelo para português (ou
qualquer outra linguagem)
'''