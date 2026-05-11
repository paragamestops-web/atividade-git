# Exercício 8: 
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o primeiro produto.")
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")