'''
2. Pensando em uma agenda, construa um
dicionário com informações do contato sendo:
CPF, nome, telefone e user no Twitter. Ao
final, imprima todos os contatos na forma

CPF: nome, telefone (user)
'''
print("Contatos:")
contatos = {
    '423.234.321-10': {'nome':'João Pedro', 'telefone':'(016) 1234-45672','user':'@JP'},
    '323.324.122-05': {'nome':'Maria Helena', 'telefone':'(016) 9872-65435','user':'@MariHelena'},
    '221.211.721-08': {'nome':'Gustavo Neto', 'telefone':'(016) 5553-12128','user':'@GusNeto'},
    '963.894.525-11': {'nome':'Julia Fonseca', 'telefone':'(016) 7891-12346','user':'@FonsecaJu'}
}

for cpf, infos in contatos.items():
    nome = infos['nome']
    telefone = infos['telefone']
    user = infos['user']
    print(f"CPF: {cpf}  Nome: {nome}  Telefone: {telefone}  Twiter User: {user}")