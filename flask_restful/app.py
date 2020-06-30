from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

devs = [
    {
        'id': 0,
        'nome': 'Gean Costa',
        'habilidades': ['Python', 'R', 'Julia']
    },
    {
        'id': 1,
        'nome': 'Juliana Silva',
        'habilidades': ['Autocad', 'Revit', 'Excel']
    }
]

class Developers(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        pos = len(devs)
        dados['id'] = pos
        devs.append(dados)
        response = {'status': 'sucessful', 'message': f'Entry has been recorded', 'entry': dados}
        return response

class Developer(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            response = {'status': 'error',
                        'message': f'developer with id {id} does not exist'}
        except Exception:
            response = {'status': 'error', 'message': f'unkown error'}
        return response
        # return {'method': 'get', 'message': 'Olá, Dev'}

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados
        # return {'method': 'put', 'message': 'Olá, Dev'}

    def delete(self, id):
        devs.pop(id)
        return {'status': 'sucessful', 'message': 'the entry has been deleted'}
        # return {'method': 'delete', 'message': 'Olá, Dev'}

api.add_resource(Developers, '/devs')
api.add_resource(Developer, '/dev/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)
