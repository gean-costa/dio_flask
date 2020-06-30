from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Pessoa não encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.nome = dados['idade']
        pessoa.save()
        response = {
            'status': 'sucessful',
            'message': 'Informação alterada',
            'dados': dados
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        response = {
            'status': 'sucessful',
            'message': f'Pessoa {pessoa.nome} deletada'
        }
        return response


class ListarPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': p.id, 'nome': p.nome, 'idade': p.idade} for p in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'status': 'sucessful',
            'message': f'Pessoa {pessoa.nome} adicionada'
        }
        return response

class ListarAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': a.id, 'pessoa': a.pessoa.nome, 'nome': a.nome} for a in atividades]
        return response
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'atividade': atividade.nome
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListarPessoas, '/pessoas/')
api.add_resource(ListarAtividades, '/atividades/')

if __name__ == "__main__":
    app.run(debug=True)
