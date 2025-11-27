# main.py

from models.carro import Carro

def menu():
    print("\n=== SISTEMA DE CADASTRO DE CARROS ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def menuMarca():
    print("\nEscolha a marca: ")
    print("1 - Fiat")
    print("2 - Chevrolet")
    print("3 - Volkswagen")
    marcaEscolhida = int(input("Escolha uma opção: "))
    match(marcaEscolhida):
        case 1:
            return ["Fiat", marcaEscolhida]
        case 2: 
            return ["Chevrolet", marcaEscolhida]
        case 3: 
            return ["Volkswagen", marcaEscolhida]
        case _:
            print("Numero inválido")


def menuModelo(inputMarca):
    if inputMarca == 1:
        print("\nEscolha o modelo: ")
        print("1 - Uno")
        print("2 - Argo")
        print("3 - Mobi")
        modeloEscolhido = int(input("Escolha uma opção: "))
        match(modeloEscolhido):
            case 1:
                return "Uno"
            case 2: 
                return "Argo"
            case 3: 
                return "Mobi"
    elif inputMarca == 2:
        print("\nEscolha o modelo: ")
        print("1 - Classic")
        print("2 - Onix")
        print("3 - Tracker")
        modeloEscolhido = int(input("Escolha uma opção: "))
        match(modeloEscolhido):
            case 1:
                return "Classic"
            case 2: 
                return "Onix"
            case 3: 
                return "Tracker"
    elif inputMarca == 3:
        print("\nEscolha o modelo: ")
        print("1 - Classic")
        print("2 - Onix")
        print("3 - Tracker")
        modeloEscolhido = int(input("Escolha uma opção: "))
        match(modeloEscolhido):
            case 1:
                return "Gol"
            case 2: 
                return "Fox"
            case 3: 
                return "Tcross"
    else:
        print("O numero digitado foi inválido.")


while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR CARRO ---")
        listaMarca = menuMarca()
        marca = listaMarca[0]
        numeroMarca = listaMarca[1]

        modelo = menuModelo(numeroMarca)
        ano = input("Ano: ")
        while not ano.isdigit():
            print("Ano inválido! Digite apenas números.")
            ano = input("Ano: ")

        carro = Carro(marca, modelo, ano)
        carro.salvar_carro()
        print("Carro salvo com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE CARROS ---")

        lista = Carro("", "", "").carregar_todos()

        if not lista:
            print("Nenhum carro cadastrado ainda.")
        else:
            for c in lista:
                print(f"{c['marca']} - {c['modelo']} - {c['ano']}")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

