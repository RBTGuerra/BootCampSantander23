# Neste Desafio o Objetivo é testar os conhecimentos em,funções, tipologia numerica, input's, 
# condições e variaveis.
# A idéia é desenvolver um app que calcule os juros compostos de um investimento ficticio.
# o mesmo deve receber 3 parametros: a taxa de juros anual e o periodo de tempo em anos, 
# logo a função deve calcular e retornal o valor final. 

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

for _ in range(periodo):
    valor_final *= (1 + taxa_juros)

print("Valor final do investimento: R$", round(valor_final, 2))