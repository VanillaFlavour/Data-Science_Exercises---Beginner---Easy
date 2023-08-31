dados = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
         'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
         'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
         'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

total = 0


for setor,idade in dados.items():
  media_idade = sum(idade) / len(idade)
  print(f'O {setor} tem a média de {media_idade}')

  total += sum(idade)

media_total = total / (len(idade) * len(dados))
print(f'A média de idade geral é {media_total}')

acima_media = 0

for setor,idade in dados.items():
  for id in idade:
    if id>media_total:
      acima_media += 1

print(f'{acima_media} pessoas estão acima da idade média geral')
