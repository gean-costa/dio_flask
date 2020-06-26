from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def api():
    return 'Hallo leute!'


@app.route('/json')
def api_json():
    return jsonify({'Hallo': 'leute'})


@app.route('/pessoa/<int:id>')
def api_pessoa(id):
    return jsonify(
        {
            'id': id,
            'nome': 'Gean',
            'sobrenome': 'Costa'
        })


@app.route('/soma/<int:n1>/<int:n2>')
def api_soma(n1, n2):
    return f'{n1} + {n2} = {n1+n2}'


@app.route('/soma2', methods=['POST'])
def soma2():
    # no body do postman -> {"valores": [10, 10, 10]}
    dados = json.loads(request.data)
    soma = sum(dados['valores'])
    return jsonify({'soma': soma})

# OBS
# utilizando a biblioteca requests:
# response = requests.post('http://127.0.0.1:5000/soma2', json={"valores": [10, 10, 10]})
# dados = response.json()
# print(dados['soma'])

if __name__ == "__main__":
    app.run(debug=True)
