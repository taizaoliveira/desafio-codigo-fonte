import json

with open('faturamento_mensal.json') as f:
    faturamento = json.load(f)

menor_valor = float('inf')
maior_valor = 0
soma_valores = 0

for dia in faturamento:
    valor = dia['valor']
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    soma_valores += valor

media_mensal = soma_valores / len([dia for dia in faturamento if dia['valor'] > 0])

dias_acima_media = 0

for dia in faturamento:
    if dia['valor'] > media_mensal:
        dias_acima_media += 1

print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias com faturamento acima da média mensal:', dias_acima_media)
