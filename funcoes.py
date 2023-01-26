import json
import os
def opcoes ():
    opcao = int(input("Digite <1> para registrar um ativo ou <2> para exibir arquivos armazenados"))
    return opcao
def registrar (dados):
    resp = "S"
    while resp == "S":
        dados[input("Digite o seu CPF: ")]=[input("Digite seu nome: "),input("Digite seu sobrenome: ")]
        resp = input("Deseja continuar ? S ou N: ").upper()
    with open("dados.json","w") as arq_json:
        json.dump(dados, arq_json)
    return print("Json gerado!")
def exibir (resultado):
    with open("dados.json","r") as arq_json:
        resultado = json.load(arq_json)
        for chave, dado in resultado.items():
            print(f"Nome------:{dado[0]}")
            print(f"Sobrenome-:{dado[1]}")
            print(f"CPF-------:{chave}")
def abrir (arquivo):
    if os.path.exists(arquivo):
        with open(arquivo,"r") as arq_json:
            return json.load(arq_json)
    else:
        dicionario ={}
    return dicionario
def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario=json.load(arq_json)
    else:
        dicionario = {}
    return dicionario







