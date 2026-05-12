# PARTE 1 - INPUT E PRINT


# Peça o nome do usuário
nome = input("Digite seu nome: ")

# Mostre uma mensagem com o nome
print("Olá,", nome)


# PARTE 2 - CONCATENAÇÃO


# Crie duas variáveis
nome = "João"
sobrenome = "Silva"

# Junte as duas em uma frase
print("Seu nome completo é:", nome, sobrenome)



# PARTE 3 - EQUAÇÃO MATEMÁTICA


# Peça dois números ao usuário
n1 = float(input("Digite o primeiro número: "))
operacao = input("Escolha a operação: (+, -, /, *) > ")
n2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = n1 + n2

if operacao == "-":
    resultado = n1 - n2

if operacao == "/":
    resultado = n1 / n2        

if operacao == "*":
    resultado = n1 * n2

print(f"Resultado: {resultado}")
# PARTE 4 - FOR


# Mostrar números de 1 até 10
for i in range(1, 11):
    print(i)



# PARTE 5 - LISTA


# Lista com 3 nomes
nomes = ["Ana", "Carlos", "Pedro"]

# Mostrar nomes com for
for nome in nomes:
    print(nome)



# PARTE 6 - DICIONÁRIO

# Criar dicionário
pessoa = {
    "nome": "Miguel",
    "idade": 14,
    "cidade": "Brasília"
}

# Mostrar valores
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])


# PARTE 7 - CLASSE E OBJETO
# 

# Criar classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criar objeto
p1 = Pessoa("Miguel", 14)

# Mostrar dados
print("Nome:", p1.nome)
print("Idade:", p1.idade)

# PARTE 8 - DESAFIO FINAL


# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Lista para guardar pessoas
pessoas = []

# Menu
while True:
    print("=== MENU ===")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastrar pessoa
    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pessoa = Pessoa(nome, idade)
        pessoas.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    # Listar pessoas
    elif opcao == "2":
        print("=== LISTA DE PESSOAS ===")

        for pessoa in pessoas:
            print("Nome:", pessoa.nome)
            print("Idade:", pessoa.idade)
            print("---------------")

    # Sair
    elif opcao == "3":
        print("Programa encerrado!")
        break

    # Opção inválida
    else:
        print("Opção inválida!")