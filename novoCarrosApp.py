import json

class Carros:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def lerCarros(self):
        try:
            with open("carros.json", "r", encoding="utf-8") as arquivo:
                dadosDoJson = json.load(arquivo) 
                return dadosDoJson
        except FileNotFoundError:
            print("O arquivo json nao foi encontrado.")
            return {}
        except json.JSONDecodeError:
            print("Erro: O arquivo contém um erro de formato.")
            return {}
    
    def printCarros(self):
        carros = self.lerCarros()
        #a lista 'carros' fica atualizada com os dados do carros.json
        print("Dados que foram carregados do JSON 'carros': ")
        print(carros)

    def inserirCarros(self):
        carrosExistentes = self.lerCarros()
        dicionarioCarros = {
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "preco": self.preco
        }

        #Criacao do ID (ele pega a quantidade de IDS dentro de 'carrosExistentes' e define eles como chave para add os outros dicionarios)
        novo_id = (str(len(carrosExistentes)+ 1))
        carrosExistentes[novo_id] = dicionarioCarros

        with open("carros.json", "w", encoding="utf-8") as arquivo:
            json.dump(carrosExistentes, arquivo, ensure_ascii=False, indent=4 )
            print("Dados salvos com sucesso!")

while True:
    
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano que o carro foi fabricado: "))  
    preco = float(input("Digite o preco do carro: "))
    carro1 = Carros(marca, modelo, ano, preco)
    carro1.inserirCarros()

# Criação de um CRUD.    Abaixo temos o READ:

# def lerCarros():
#     try:
#         with open("carros.json", "r", encoding="utf-8") as arquivo:
#             dadosDoJson = json.load(arquivo) 
#             return dadosDoJson
#     except FileNotFoundError:
#         print("O arquivo json nao foi encontrado.")
#         return {}
#     except json.JSONDecodeError:
#         print("Erro: O arquivo contém um erro de formato.")
#         return {}

# def printCarros():    
#     carros = lerCarros()
#     #a lista 'carros' fica atualizada com os dados do carros.json
#     print("Dados que foram carregados do JSON 'carros': ")
#     print(carros)



# inserirCarros()
# printCarros()


