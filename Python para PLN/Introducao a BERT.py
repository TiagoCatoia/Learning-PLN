'''
Bidirectional Encoder Representations from Transformers
BERT (Representação de codificadores bidirecionais para transformadores)

BERT é o algoritmo de aprendizado profundo (Deep Learning) do Google para PLN.

Nível linguístico mais semântico

- Basicamente, o BERT analisa o contexto à esquerda
e à direita do token
- Compreensão muito mais profunda sobre as relações entre
palavras e entre frases.
- Ajuda o computador a enterder o texto, ajudando na predição de palavras.

O BERT constrói um modelo de linguagem e após o
treinamento do modelo, passa pelo “ajuste fino”
- O que o submete a tarefas específicas com entradas e
saídas conforme preferido.

RELEMBRANDO: 
- "modelos de linguagem" referem-se a abordagens e sistemas de aprendizado de máquina
que têm a capacidade de entender, gerar e manipular linguagem natural.

MATERIAL DE ESTUDA BERT:
https://rockcontent.com/br/blog/bert/
https://www.deeplearningbook.com.br/o-que-e-bert-bidirectional-encoder-representations-from-transformers/
https://www.deeplearningbook.com.br/modelo-bert-para-processamento-de-linguagem-natural/
https://www.deeplearningbook.com.br/modelo-bert-previsao-da-proxima-frase/

CURSOS GRATUITOS:
https://www.datascienceacademy.com.br/cursosgratuitos


O que vamos precisar para fazer o BERT rodar:
BERT (Representação de codificadores bidirecionais para transformadores)

- Os transformadores(Vão fazer o arcabouço para o treinamento e execução do BERT)
- Os modelos BERT treinados(Ajuste fino, além dos trasnformadores)
- Um módulo que permita execução dos modelos()
- O ambiente de execução do processo
'''
from transformers import BertTokenizer, BertModel
'''
Os modelos BERT treinados:
- BERTimbau – Portuguese BER: https://github.com/neuralmind-ai/portuguese-bert
Módulos que permitem execução dos modelos:
- PyTorch 
- TensorFlow
Tutoriais de como começar a usar e instalação:
https://pytorch.org/get-started/locally/
https://www.tensorflow.org/overview?hl=pt-br

Duas tarefas práticas:
- 1. Predizer qual palavra completa uma dada parte de uma sentença.
- 2. Verificar a similaridade entre duas palavras dentro do contexto da sentença.

UTILIZAREI O GOOGLE COLAB:

ATIVIDADE 1:
Predição de uma palavra pelo contexto da sentença
https://colab.research.google.com/drive/1_KCDZ-XeGNAkb1TvV93LVWOgsZM5L2ex#scrollTo=qNiKf1vpMRsr

ATIVIDADE 2:
Verificar a similaridade de contexto entre duas palavras dentro de uma sentença
https://colab.research.google.com/drive/1gUV_jFv_TBR262FK_zqHec-9Cs4l-ffK#scrollTo=Ila-CdmZgoBV
'''