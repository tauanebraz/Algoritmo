# TRANFORMANDO PORTOGOL EM PYTHON 
#   ==== EXERCICIO 10 ====

custo = float(input("qual foi o custo do produto?"))
percent = float(input("taxa de serviço:"))

percent = (percent/100) + 1
valvenda = custo * percent

print(f"O valor de venda sera R$", valvenda)