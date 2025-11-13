import json

carros = []

# Criação de um CRUD.    Abaixo temos o READ:
def lerCarros():
    try:
        with open("carros.json", "r", encoding="utf-8") as arquivo:
            dadosDoJson = json.load(arquivo) 
            return dadosDoJson
    except FileNotFoundError:
        print("O arquivo json nao foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo contém um erro de formato.")
        return []
    
carros = lerCarros()
#a lista 'carros' fica atualizada com os dados do carros.json
print("Dados que foram carregados do JSON 'carros': ")
print(carros)

def inserirCarros():
    with open("carros.json", "w", encoding="utf-8") as arquivo:
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        try:
            ano = int(input("Digite o ano que o carro foi fabricado: "))
        except ValueError:
            print("O valor digitado para o ano não é um inteiro.")
            ano = int(input("Digite o ano que o carro foi fabricado: "))
            return ano
        
        try:
            preco = float(input("Digite o preco do carro: "))
        except ValueError:
            print("O valor digitado para o preço nao segue o padrão float, digite novamente")
            preco = float(input("Digite o preco do carro: "))
            return preco


        insereCarro = json.dump()