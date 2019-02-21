from flask import Flask, request, make_response
from flask import jsonify

import sqlite3


def conn():
    return sqlite3.connect('funcionarios.db')


def cria_tabela():
    try:
        c = conn().cursor()
        c.execute("""CREATE TABLE funcionario (nome varchar(50), cpf int, cargo varchar(50))""")

    except Exception:
        pass


# Definindo app
app = Flask(__name__)


@app.route('/cadastro', methods=['POST'])
def create():
    cria_tabela()
    try:

        dados = request.get_json()
        nome = dados['nome']
        cpf = dados['cpf']
        cargo = dados['cargo']

        conexao = conn()
        c = conexao.cursor()
        c.execute("INSERT INTO funcionario (nome, cpf, cargo) VALUES (?, ?, ?)", (nome, cpf, cargo))
        conexao.commit()

        c.close()
        conexao.close()

        response = {'funcionario': {'nome': nome, 'cpf': cpf, 'cargo': cargo}, 'response': True}
        return make_response(jsonify(response), 201, {'Content-Type': 'application/json'})

    except Exception as e:

        response = {'erro': 'não foi possivel executar a requisicao'}
        return make_response(jsonify(response), 500, {'Content-Type': 'application/json'})


@app.route('/cadastro/<cpf>', methods=['GET'])
def get(cpf):

    try:

        conexao = conn()
        c = conexao.cursor()
        c.execute("SELECT * FROM funcionario WHERE cpf = ?", (cpf,))

        if c.rowcount == 0:
            response = {'erro': 'funcionario não encontrado'}
            return make_response(jsonify(response), 404, {'Content-Type': 'application/json'})

        linhas = c.fetchall()

        c.close()
        conexao.close()

        resultados = []

        for linha in linhas:
            resultados.append({'nome': linha[0], 'cpf': linha[1], 'cargo': linha[2]})

        response = {'funcionarios': resultados, 'response': True}
        return make_response(jsonify(response), 200, {'Content-Type': 'application/json'})

    except Exception as e:

        response = {'erro': 'não foi possivel executar a requisicao'}
        return make_response(jsonify(response), 500, {'Content-Type': 'application/json'})


@app.route('/cadastro/<int:cpf>', methods=['DELETE'])
def delete(cpf):
    try:

        conexao = conn()
        c = conexao.cursor()
        c.execute("DELETE FROM funcionario WHERE cpf=?;", (cpf,))
        conexao.commit()

        if c.rowcount == 0:
            response = {'erro': 'funcionario não encontrado'}
            return make_response(jsonify(response), 404, {'Content-Type': 'application/json'})

        c.close()
        conexao.close()

        response = {'status': 'funcionario deletado', 'response': True}
        return make_response(jsonify(response), 200, {'Content-Type': 'application/json'})

    except Exception as e:

        response = {'erro': 'não foi possivel executar a requisicao'}
        return make_response(jsonify(response), 500, {'Content-Type': 'application/json'})


if __name__ == "__main__":
    app.run(port=8080)
