from models import Pessoas, Usuarios


def inserir_pessoa():
    pessoa = Pessoas(nome='Juliana', idade=21)
    pessoa.save()
    print(pessoa)


def consultar_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa[0].id)

    # pessoa = Pessoas.query.filter_by(nome='Gean Costa')  # .first()
    # print(pessoa[0].idade)


def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gean').first()
    pessoa.idade = 30
    pessoa.save()


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gean').first()
    pessoa.delete()

def inserir_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consultar_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)



if __name__ == "__main__":
    # inserir_pessoa()
    inserir_usuario('geandreson','12345')
    # alterar_pessoa()
    # excluir_pessoa()
    # consultar_pessoa()
    consultar_usuarios()
