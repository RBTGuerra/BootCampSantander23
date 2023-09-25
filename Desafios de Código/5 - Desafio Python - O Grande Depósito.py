# Neste desafio o Objetivo é testar os conhecimentos em, funções, condições, if, else, elif.
# A idéia é construir um app que auxilie o cliente a realizar um depósito ficticio, verificando se o 
# valor é valido, condicionando se o mesmo for maior que zero o app deve adicionar o valor ao saldo
# da conta ficticia, caso contrário o app deve exibir uma mensagem de erro.

valor = float(input())

if valor > 0:
    saldo_atual = valor
    print("Deposito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo_atual:.2f}")
elif valor < 0:
    print("Valor invalido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")