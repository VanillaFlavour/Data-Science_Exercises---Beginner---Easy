dic_bio = {'Área Norte': [2819, 7236],
           'Área Leste': [1440, 9492],
           'Área Sul': [5969, 7496],
           'Área Oeste': [14446, 49688],
           'Área Centro': [22558, 45148]}

soma_media = 0
maior_diversidade = ''
maior_soma = 0

for area, especies in dic_bio.items():
  soma_especies = sum(especies)
  media = soma_especies/len(especies)
  print(f'A {area} tem a média de {media} espécies')

  if soma_especies > maior_soma:
    maior_soma = soma_especies
    maior_diversidade = area

  soma_media += media

media_total = soma_media / len(dic_bio)
print(f'Média geral de espécies: {media_total}')
print(f'Área com a maior diversidade biológica: {maior_diversidade}')
