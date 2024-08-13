import requests
import json
url = 'https://raw.githubusercontent.com/Danielessa/Json-para-treino/main/sistema-biblioteca.json'

response = requests.get(url)

if response.status_code ==200:
    data = response.json()

else:
    print(f'Erro ao importar Json: Codigo:  {response.text}')

for nome_dado, dados in data.items():
    with open(f'{nome_dado}.json','w') as arquivo:
        json.dump(dados, arquivo, indent=4)
