# Neste Desafio o Objetivo é testar os conhecimentos em, condições, strings, input's etc;
# A idéia é melhorar a experiência do usuario, implementando uma solução que possa
# organizar em ordem alfabética a lista de ativos que será informada pelo usuario.


ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# Ordenar os ativos em ordem alfabética
ativos.sort()

# Imprimir a lista de ativos ordenada
for ativo in ativos:
    print(ativo)