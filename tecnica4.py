print('=' * 35)
print('FATURAMENTO MENSAL - DISTRIBUIDORA')
print('=' * 35)

print('''SP - R$67.836,43
RJ - R$36.678,66
MG - R$29.229,88
ES - R$27.165,48
OUTROS - R$19.849,53''')

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'OUTROS': 19849.53
}

total_faturamento = sum(faturamento.values())
print('-' * 40)
print('Percentual de representação por estado: ')

for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f'{estado}: {percentual:.2f}%')
print('-' * 40)
