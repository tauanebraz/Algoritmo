# TRANFORMANDO PORTOGOL EM PYTHON 
#    ==== EXERCICIO 03 ====

nome = input("Qual o nome do vendedor?")
salfixo = int(input("Qual e o seu salário fixo?"))
total = int(input("Qual o total de vendas efetuadas em dinheiro no mes?"))

comissao = total * 15/100
salfinal = salfixo + comissao 

print(f"Nome do vendedor:", nome,"Salario fixo sera", salfixo,"Salario final sera R$", salfinal)