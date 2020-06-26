from flask import Flask

app = Flask(__name__)

@app.route('/<nome>/<int:idade>')
def hello(nome: str, idade: int) -> str:
    return f'Hello World, {nome} de {idade} anos.'

if __name__ == "__main__":
    # quando em produção, debug=False
    app.run(debug=True)