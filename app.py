from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_frase', methods=['GET'])
def gerar_frase():
    response = requests.get("http://xinga-me.appspot.com/api")
    if response.status_code == 200:
        data = response.json()
        xingo = data["xingamento"]
        xingo_formatado = xingo.capitalize()
        return jsonify({'frase': xingo_formatado})

    else:
        return jsonify({'error': 'Não foi possível obter um xingamento.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
