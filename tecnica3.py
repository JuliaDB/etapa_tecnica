import json

with open('dados.json') as arquivo:
    dados = json.load(arquivo)

primeiro_dia = 3 # quarta-feira
valor_min_atual = dados[0]['valor'] # ancorando o menor valor no primeiro dia util do mês
valor_max_atual = 0

for dado in dados:
    # pegando o dia atual que está no 'for' e obtendo o numero correspondete da semana (1=seg,2=ter,3=quart,4=quint,5=sext,6=sab,0=dom)
    dia_atual = (primeiro_dia + (dado['dia'] - 1)) % 7

    # verificando se este dia é util, ou seja, não é sabado e domingo, por isso tem um not no if.
    if dia_atual not in (6, 0): # 6 = sábado e 7 = domingo

        # verificando VALOR MÍNIMO atual com o VALOR corrente que está no FOR.
        if dado['valor'] < valor_min_atual:
            valor_min_atual = dado['valor']

        # verificando VALOR MÁXIMO atual com o VALOR corrente que está no FOR.
        if dado['valor'] > valor_max_atual:
            valor_max_atual = dado['valor']

print(valor_min_atual)
print(valor_max_atual)
