class Pessoa:
    def __init__(self, nome, email, sexo, numero, cpf):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.numero = numero
        self.cpf = cpf

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Email:", self.email)
        print("Sexo:", self.sexo)
        print("Número:", self.numero)
        print("CPF:", self.cpf)
        print("-" * 20)


# Criando dois objetos
pessoa1 = Pessoa(
    "Miguel",
    "paragamestops@gmail.com",
    "Masculino",
    "61994151207",
    "123.456.789-00"
)

pessoa2 = Pessoa(
    "Ana",
    "ana@gmail.com",
    "Feminino",
    "61888888888",
    "987.654.321-00"
)

# Mostrando os dados
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()