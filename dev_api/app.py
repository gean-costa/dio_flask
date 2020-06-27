from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {
        'nome': 'Gean Costa',
        'habilidades': ['Python', 'R', 'Julia']
    },
    {
        'nome': 'Juliana Silva',
        'habilidades': ['Autocad', 'Revit', 'Excel']
    }
]

# lista todos os desenvolvedores / inclui um novo desenvolvedor
@app.route('/developers/', methods=['POST', 'GET'])
def developers():
    if request.method == 'GET':
        return jsonify(devs)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        devs.append(dados)
        response = {'status': 'sucessful', 'message': f'Entry has been recorded', 'entry': dados}
        return jsonify(response)

# seleciona, altera e apaga um desenvolvedor dado um id
@app.route('/developer/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            response = {'status': 'error',
                        'message': f'developer with id {id} does not exist'}
        except Exception:
            response = {'status': 'error', 'message': f'unkown error'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'sucessful', 'message': 'the entry has been deleted'})


if __name__ == "__main__":
    app.run(debug=True)
