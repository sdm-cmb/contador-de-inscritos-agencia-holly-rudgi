from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

# Sua chave de API do Google
api_key = 'AIzaSyCK4eLeqFanz4VeuPRat_Tqj3yNpQUQxKI'

# Dicionário com os nomes dos canais e seus respectivos IDs
channels = {
    'holly rudgi': 'UC76-9Ko_wzj-qEb9tpx5CiA',
    'ruan mania': 'UCieyr0CxKua_fvnoxGmfRfw',
    'edy brown': 'UCIsDomRfezzVctmghlaBkVg',    
    'brisando com o ruy': 'UCsDMQS_NmSXEfbOQHQeQDNw',
    'ruy cardoso': 'UCbMh-6Uh2QGMLotae_E6xMA',
    'brisando com o rudgi': 'UC3Tmv6Bv0O_XuPyswDhLabw',
    'brisando house': 'UCMVa9W9bntnXHu3Knet1Idw',
    'yas mania': 'UCJvxwAkxOiZpe51PV0IVC-A',
    'lunatica': 'UCKGSkpjwUAQ7W8XroEwJw3Q',
    'sdm cmb': 'UCBCDtTbfzu-imnSSSklkDjg'
}

# Função para obter o número de inscritos de um canal
def get_subscriber_count(channel_id, api_key):
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    inscritos = int(data['items'][0]['statistics']['subscriberCount'])
    return inscritos

@app.route('/')
def index():
    # Obtém a contagem de inscritos para cada canal
    channel_data = []
    total_subscribers = 0
    for nome, channel_id in channels.items():
        inscritos = get_subscriber_count(channel_id, api_key)
        total_subscribers += inscritos
        inscritos_formatados = '{:,.0f}'.format(inscritos).replace(',', '.')  # Formata os inscritos com ponto como separador de milhar
        total = '{:,.0f}'.format(total_subscribers).replace(',', '.') 
        channel_data.append({'nome': nome, 'inscritos': inscritos_formatados})

    # Ordena a lista de canais com base no número de inscritos
    channel_data = sorted(channel_data, key=lambda x: int(x['inscritos'].replace('.', '')))

    return render_template('index.html', lista=channel_data, total_inscritos=total)

@app.route('/subscribers/<channel_name>')
def subscribers(channel_name):
    channel_id = channels.get(channel_name)
    if channel_id:
        inscritos = get_subscriber_count(channel_id, api_key)
        return jsonify({'channel_name': channel_name, 'subscriber_count': inscritos})
    else:
        return jsonify({'error': 'Channel not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
