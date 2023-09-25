# Neste Desafio o Objetivo é testar os conhecimentos em condições, if, else, input's etc;
# A ideia é implementar uma solução algorítmica que permita o cliente realizar saques 
# ficticios, com algumas condições, o cliente deve digitar o saldoTotal de sua conta ficticia
# e o valorSaque da mesma, o saque so podera ser realizado se o saldoDisponivel na conta ficticia 
# for igual ou superior ao valor solicitado.


# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if saldo_total >= valor_saque:
    saldo_total -= valor_saque
    print(f"Saque realizado com sucesso. Novo saldo: {saldo_total}")
else:
    print("Saldo insuficiente. Saque nao realizado!")