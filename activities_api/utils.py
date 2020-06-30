from models import Pessoas


def inserir():
    pessoa = Pessoas(nome='Juliana', idade=21)
    pessoa.save()
    print(pessoa)


def consultar():
    pessoa = Pessoas.query.all()
    print(pessoa[0].id)

    #pessoa = Pessoas.query.filter_by(nome='Gean Costa')  # .first()
    #print(pessoa[0].idade)


def alterar():
    pessoa = Pessoas.query.filter_by(nome='Gean').first()
    pessoa.idade = 30
    pessoa.save()


def excluir():
    pessoa = Pessoas.query.filter_by(nome='Gean').first()
    pessoa.delete()


if __name__ == "__main__":
    # inserir()
    # alterar()
    # excluir()
    consultar()
