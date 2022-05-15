entrada = str(input('Digite: '))
entrada = entrada.split(' ')

if entrada[0] == 'Regular:':
    lake_semana = 110
    lake_fim = 90

    brid_semana = 160
    brid_fim = 60

    rid_semana = 220
    rid_final = 150

else:
    lake_semana = 80
    lake_fim = 80

    brid_semana = 110
    brid_fim = 50

    rid_semana = 100
    rid_final = 40

nentradas = len(entrada)
total_lakewood = 0
total_bridgewood = 0
total_ridfewood = 0
total=[]
menor=''
for c in range(1, nentradas):
    data = entrada[c].split('(')
    if 'sat' in data[1] or 'sun' in data[1]:
        total_lakewood += lake_fim
        total_bridgewood += brid_fim
        total_ridfewood += rid_final    
    else:
        total_lakewood += lake_semana
        total_bridgewood += brid_semana
        total_ridfewood += rid_semana

valores=[]
hoteis=[]

valores.append(total_ridfewood)
valores.append(total_bridgewood)
valores.append(total_lakewood)

hoteis.append("Ridfewood")
hoteis.append("Bridgewood")
hoteis.append("Lakewood")

posicao_menor = min(valores)

print(hoteis[valores.index(posicao_menor)])