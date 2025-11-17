import csv
import pprint 

def apresentar_dado(colunas):
    with open("data/populacao.csv", "r", newline='', encoding='utf-8') as f:
        dados = csv.DictReader(f)
        for linha in dados:
            dados = {col: linha[col] for col in colunas}
            print(dados)

print('"Esta é uma lista de países e dependências por população."')
print(".\n.\n.")
apresentar_dado(["País", "População", "% no Mundo", "Data", "Fonte"])

print("\n" + "-"*60 + "\n")   

def apresentar_pais(nome_pais):
    with open("data/populacao.csv", "r", newline='', encoding="utf-8") as f:
        dados = csv.DictReader(f)
        for linha in dados:
            if linha["País"] == nome_pais:
                return linha
    return "País náo cadastrado, tente outro!"

try:
    dados = input("Digite o nome de um país: ")
    dados_pais = apresentar_pais(dados)
except ValueError:
    print("País näo cadastrado, tente outro!")
print(dados_pais)

print("\n" + "-"*60 + "\n")  

def apresentar_dado(colunas):
    with open("data/aposentadoria.csv", "r", newline='', encoding='utf-8') as f:
        dados = csv.DictReader(f)
        for linha in dados:
            dados = {col: linha[col] for col in colunas}
            print(dados)

print('"Este artigo lista a idade legal de aposentadoria em diferentes países"')
print(".\n.\n.")
apresentar_dado(["País", "Homem", "Mulher", "Ano"])

print("\n" + "-"*60 + "\n")   

def apresentar_pais(nome_pais):
    with open("data/aposentadoria.csv", "r", newline='', encoding="utf-8") as f:
        dados = csv.DictReader(f)
        for linha in dados:
            if linha["País"] == nome_pais:
                return linha
    return "País náo cadastrado, tente outro!"

try:
    dados = input("Digite o nome de um país: ")
    dados_pais = apresentar_pais(dados)
except ValueError:
    print("País näo cadastrado, tente outro!")
print(dados_pais)

print("\n" + "-"*60 + "\n") 

def apresentar_dado(colunas):
    with open("data/trabalho.csv", "r", newline='', encoding='utf-8') as f:
        dados = csv.DictReader(f)
        for linha in dados:
            dados = {col: linha[col] for col in colunas}
            print(dados)

print('"Esta é uma lista de países por composição setorial da força de trabalho em 2023, principalmente com base no Banco Mundial."')
print(".\n.\n.")
apresentar_dado(["País", "Agricultura(%)", "Indústria(%)", "Serviços(%)"])

print("\n" + "-"*60 + "\n")   

def apresentar_pais(nome_pais):
    with open("data/trabalho.csv", "r", newline='', encoding="utf-8") as f:
        dados = csv.DictReader(f)
        for linha in dados:
            if linha["País"] == nome_pais:
                return linha
    return "País náo cadastrado, tente outro!"

try:
    dados = input("Digite o nome de um país: ")
    dados_pais = apresentar_pais(dados)
except ValueError:
    print("País näo cadastrado, tente outro!")
print(dados_pais)

print("\n" + "-"*60 + "\n")   

def apresentar_dado(colunas):
    with open("data/idh.csv", "r", newline='', encoding='utf-8') as f:
        dados = csv.DictReader(f)
        for linha in dados:
            dados = {col: linha[col] for col in colunas}
            print(dados)

print('"Esta é uma lista de países por Índice de Desenvolvimento Humano (IDH)."')
print(".\n.\n.")
apresentar_dado(["Posição", "País", "IDH"])

print("\n" + "-"*60 + "\n")  

def apresentar_pais(nome_pais):
    with open("data/idh.csv", "r", newline='', encoding="utf-8") as f:
        dados = csv.DictReader(f)
        for linha in dados:
            if linha["País"] == nome_pais:
                return linha
    return None

try:
    dados = input("Digite o nome de um país: ")
    dados_pais = apresentar_pais(dados)
except ValueError:
    print("País não cadastrado, tente outro!")
print(dados_pais)

print("\n" + "-"*60 + "\n")   

def apresentar_dado(colunas):
    with open("data/salario.csv", "r", newline='', encoding='utf-8') as f:
        dados = csv.DictReader(f)
        for linha in dados:
            dados = {col: linha[col] for col in colunas}
            print(dados)

print('"Esta é uma lista dos países com o salário mínimo mensal na moeda local e data de efetividade"')
print(".\n.\n.")
apresentar_dado(["País", "Salário(MoedaLocal)", "Ano"])

print("\n" + "-"*60 + "\n")   

def apresentar_pais(nome_pais):
    with open("data/salario.csv", "r", newline='', encoding="utf-8") as f:
        dados = csv.DictReader(f)
        for linha in dados:
            if linha["País"] == nome_pais:
                return linha
    return None

try:
    dados = input("Digite o nome de um país: ")
    dados_pais = apresentar_pais(dados)
except ValueError:
    print("País não cadastrado, tente outro!")
print(dados_pais)

print("\n" + "-"*60 + "\n")   

def calcular_media(arquivo_csv, colunas):
    resultados = {}
    with open(arquivo_csv, "r", newline='', encoding="utf-8") as f:
        dados = csv.DictReader(f)
        valores = {col: [] for col in colunas}
        for linha in dados:
            for col in colunas:
                try:
                    valor = float(linha[col])
                    valores[col].append(valor)
                except ValueError:
                    pass  
    for col in colunas:
        if valores[col]:
            resultados[col] = sum(valores[col]) / len(valores[col])
        else:
            resultados[col] = "Não foi possível calcular (coluna não numérica ou vazia)."

    return resultados

print("Média da População:", calcular_media("data/populacao.csv", ["População"]))
print("Média da aposentadoria:", calcular_media("data/aposentadoria.csv", ["Homem", "Mulher"]))
print("Média da Agricultura/Indústria/Serviços:", calcular_media("data/trabalho.csv", ["Agricultura(%)", "Indústria(%)", "Serviços(%)"]))
print("Média do IDH:", calcular_media("data/idh.csv", ["IDH"]))
print("Média do Salário:", calcular_media("data/salario.csv", ["Salário(MoedaLocal)"]))

def calcular_variancia(arquivo_csv, nome_dado):
    valores = []
    with open(arquivo_csv, "r", newline='', encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            try:
                valor = float(linha[nome_dado])
                valores.append(valor)
            except ValueError:
                pass  
    
    if not valores:
        return "Não foi possível calcular (coluna não numérica ou vazia)."
    
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia

print("Variância da Agricultura(%):", calcular_variancia("data/trabalho.csv", "Agricultura(%)"))
print("Variância do IDH:", calcular_variancia("data/idh.csv", "IDH"))
print("Variância do Salário:", calcular_variancia("data/salario.csv", "Salário(MoedaLocal)"))

def calcular_media_ponderada(arquivo_csv, nome_dado):
    valores = []
    pesos = []
    with open(arquivo_csv, "r", newline='', encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            try:
                valor = float(linha[nome_dado])
                valores.append(valor)
            except ValueError:
                pass 
    
    if valores and pesos and sum(pesos) > 0:
        media_ponderada = sum(v * p for v, p in zip(valores, pesos)) / sum(pesos)
        return media_ponderada
    else:
        return "Não foi possível calcular (coluna não numérica ou pesos inválidos)."

print("Média ponderada do IDH (por população):", calcular_media_ponderada("data/idh.csv", "IDH"))
print("Média ponderada da Agricultura(%):", calcular_media_ponderada("data/trabalho.csv", "Agricultura(%)"))
print("Média ponderada do Salário (por PIB):", calcular_media_ponderada("data/salario.csv", "Salário(MoedaLocal)"))

import csv

def calcular_media(arquivo_csv, nome_dado):
    valores = []
    with open(arquivo_csv, "r", newline='', encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            try:
                valor = float(linha[nome_dado])
                valores.append(valor)
            except ValueError:
                pass  
    
    if valores:
        return sum(valores) / len(valores)
    else:
        return "Não foi possível calcular a média (coluna não numérica ou vazia)."

print("Média da População:", calcular_media("data/populacao.csv", "População"))
print("Média do IDH:", calcular_media("data/idh.csv", "IDH"))
print("Média do Salário:", calcular_media("data/salario.csv", "Salário(MoedaLocal)"))