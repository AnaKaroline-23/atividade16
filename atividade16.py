# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30
peso = float(input("Digite o peso em kg"))
altura = float (input("Digite a altura em m"))
IMC = (peso/altura**2)
print (IMC)
if IMC < 18.5:
    print ("Você esta abaixo do peso")
elif 18.5 <= IMC <25:
    print ("Peso normal")
elif 25 <= IMC <30:
    print ("Esta sobrepeso")
elif IMC >=30:
    print ("Esta na obesidade")