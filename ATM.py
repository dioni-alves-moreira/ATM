# SIMULADOR DE CONTROLE DE FLUXO

from datetime import datetime

estoque_notas = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
}

def ver_estoque():
    print("""
        --- ESTOQUE ATUAL ---""")
    for denominacao in [100, 50, 20, 10]:
        print(f"""
        NOTAS R${denominacao},00: {estoque_notas[denominacao]}""")

def abastecer():
    print("""
        --- ABASTECER ATM ---""")
    for denominacao in [100, 50, 20, 10]:
        entrada = input(f"""
        NOTAS R${denominacao},00: """).strip()
        if entrada == "":
            continue
        estoque_notas[denominacao] += int(entrada)
    print("""
        ATM ABASTECIDO COM SUCESSO""")

def sacar():
    entrada = input("""
        VALOR DO SAQUE: R$""")
    valor = int(entrada)

    if valor <= 0:
        print("""
        ERRO! VALOR DEVE SER POSITIVO""")
    elif valor % 10 != 0:
        print("""
        ERRO! VALOR DEVE SER MULTIPLO DE R$10,00""")
    else:
        restante = valor
        uso = {100: 0, 50: 0, 20: 0, 10: 0}

        for denominacao in [100, 50, 20, 10]:
            if restante <= 0:
                break
            quantidade = min(estoque_notas[denominacao], restante // denominacao)
            uso[denominacao] = quantidade
            restante -= quantidade * denominacao

        if restante != 0:
            print("""
        SAQUE NEGADO!
        SEM COMBINAÇÃO DE NOTAS DISPONÍVEL""")
        else:
            for denominacao in uso:
                estoque_notas[denominacao] -= uso[denominacao]

            print(f"""
        SAQUE REALIZADO COM SUCESSO!
        VALOR: R${valor},00
        
        NOTAS DISPENSADAS: """)
            for denominacao in [100, 50, 20, 10]:
                print(f"""
        NOTAS R${denominacao},00: {uso[denominacao]}""")
                
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"""
        DATA/HORA: {agora}""")

def menu():
    while True:
        agora = datetime.now().strftime("%d/%m/%Y")
        option = input(f""" 
        UNICSUL - SIMULADOR DE CONTROLE DE FLUXO - VERSÃO 2026 {agora}
            0 - VER ESTOQUE
            1 - ABASTECER
            2 - SACAR
            9 - SAIR
        ESCOLHA A OPÇÃO DESEJADA: """)

        if option == "0":
            ver_estoque()
        elif option == "1":
            abastecer()
        elif option == "2":
            sacar()
        elif option == "9":
            break
        else:
            print("""
                ERRO!!!
                OPÇÃO DIGITADA É INVÁLIDA""")
            
menu()