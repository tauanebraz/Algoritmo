# TRANFORMANDO PORTOGOL EM PYTHON 
#   ==== EXERCICIO 11 ====

fabric_car = float(input("qual o custo da fabricação de um carro?"))

imposto = fabric_car * 28/100
taxa = imposto * 45/100

final = imposto + fabric_car + taxa

print(f"O custo ao consumidor e no valor R$", final," Mil")