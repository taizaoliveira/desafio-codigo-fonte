import json

# Carrega o JSON do faturamento mensal
with open('faturamento_mensal.json') as f:
    faturamento = json.load(f)

# Inicializa as variáveis para o menor valor, o maior valor e o somatório dos valores de faturamento diário
menor_valor = float('inf')
maior_valor = 0
soma_valores = 0

# Percorre os registros de faturamento diário para calcular o menor valor, o maior valor e a soma dos valores
for dia in faturamento:
    valor = dia['valor']
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    soma_valores += valor

# Calcula a média mensal, desconsiderando os dias sem faturamento
media_mensal = soma_valores / len([dia for dia in faturamento if dia['valor'] > 0])

# Inicializa a variável para o número de dias com faturamento superior à média mensal
dias_acima_media = 0

# Percorre os registros de faturamento diário novamente para contar os dias com faturamento superior à média mensal
for dia in faturamento:
    if dia['valor'] > media_mensal:
        dias_acima_media += 1

# Imprime os resultados
print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias com faturamento acima da média mensal:', dias_acima_media)
