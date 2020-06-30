from models import Pessoas


def inserir():
    pessoa = Pessoas(nome='Juliana Silva', idade=21)
    pessoa.save()
    print(pessoa)


def consultar():
    pessoa = Pessoas.query.all()
    print(pessoa)

    #pessoa = Pessoas.query.filter_by(nome='Gean Costa')  # .first()
    #print(pessoa[0].idade)


def alterar():
    pessoa = Pessoas.query.filter_by(nome='Gean Costa').first()
    pessoa.idade = 30
    pessoa.save()


def excluir():
    pessoa = Pessoas.query.filter_by(nome='Gean Costa').first()
    pessoa.delete()


if __name__ == "__main__":
    # inserir()
    # alterar()
    excluir()
    consultar()
