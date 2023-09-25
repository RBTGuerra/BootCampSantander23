# Neste desafio, o objetivo é testar os conhecimentos em variaveis, input's etc;
# A ideia é desenvolver uma solução permitindo que o cliente equilibre o saldo Bancário.
# o Programa solicita uma entrada de um valor ficticio, depois que seja informado duas 
# transações, um depósito e um saque, o programa deve atualizar o saldo com base nas 
# transações e exibir o saldo final.

saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

saldo_atualizado = saldo_atual + valor_deposito - valor_retirada

print(f"Saldo atualizado na conta: {saldo_atualizado:.1f}")