import json


def ler_carros():
    try:
        with open("carros.json", "r", encoding="utf-8") as arquivo:
           return json.load(arquivo)
    except FileNotFoundError:
        return []
#Pega os arquivos de carros.json e joga pra lista "carros"



def salvar_carros(carro):
    with open("carros.json", "w", encoding="utf-8") as arquivo:
        json.dump(carros, arquivo)

carro = ler_carros()


def criar_carro():
    print("--- Adicionar Novo Carro ---")

    marca = input("Digite a marca do Carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano do carro: "))
    preco = float(input("Digite o preço do carro: "))

    carro_novo = { 
        "id":teste, 
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "preco": preco
    }
    
    carros.append(carro_novo)

    salvar_carros(carros)

    print(f"\n Você criou um {marca} do modelo: {modelo}.")


def listar_carros():
    
    ler_carros()

    for carro in carros:
        print(f"a marca do Carro é: {carro['marca']} e o id é {carro['teste']}")

criar_carro()

        