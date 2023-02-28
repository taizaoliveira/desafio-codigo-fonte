# definindo o faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calculando o valor total mensal da distribuidora
total = sum(faturamento.values())

# calculando o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentuais[estado] = (valor / total) * 100

# exibindo os resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
