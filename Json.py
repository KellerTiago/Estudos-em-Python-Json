from funcoes import *

dicionario = abrir("dados.json")
opcao = opcoes()
while opcao > 0 and opcao < 3:
    if opcao == 1:
        registrar(dicionario)
    elif opcao == 2:
        exibir(dicionario)
    opcao = opcoes()


