import requests


def cria_func(nome, cpf, cargo):

    funcionario = {
        "nome": nome,
        "cpf": cpf,
        "cargo": cargo
    }

    url = "http://127.0.0.1:5000/cadastro"
    r = requests.post(url, json=funcionario)
    return r


def altera_func(nome, cpf, cargo, cpf_antigo):

    funcionario = {
        "nome": nome,
        "cpf": cpf,
        "cargo": cargo
    }

    url = "http://127.0.0.1:5000/cadastro/"+cpf_antigo
    r = requests.put(url, json=funcionario)
    return r


def exclui_func(cpf):
    url = "http://127.0.0.1:5000/cadastro/"+cpf
    r = requests.delete(url)
    return r


def lista_funcs():
    url = "http://127.0.0.1:5000/"
    r = requests.get(url)
    return r


def get_func(cpf):
    url = "http://127.0.0.1:5000/cadastro/"+cpf
    r = requests.get(url)
    return r


sair = False
while not sair:
    print("A - Cadastrar funcionário")
    print("B - Alterar funcionário")
    print("C - Excluir funcionário")
    print("D - Listar funcionários")
    print("E - Listar funcionário específico")
    print("X - Sair")

    valor = input("Digite uma opção: ")

    if valor in ["A", "a"]:

        nome = input("NOME: ")
        cpf = input("CPF: ")
        cargo = input("CARGO: ")

        response = cria_func(nome, cpf, cargo)
        print({'status': '201 Criado', 'funcionario': response.json()})

    elif valor in ["B", "b"]:
        cpf_antigo = input("CPF Antigo: ")
        nome = input("NOME: ")
        cpf = input("CPF: ")
        cargo = input("CARGO: ")

        response = altera_func(nome, cpf, cargo, cpf_antigo)
        print({'status': '202 Alterado', 'funcionario': response.json()})

    elif valor in ["C", "c"]:
        cpf = input("Digite o CPF:")
        response = exclui_func(cpf)
        print({'status': response.status_code})

    elif valor in ["D", "d"]:
        response = lista_funcs()
        print({'status': '200'}, response.json())

    elif valor in ["E", "e"]:
        cpf = input("Digite o CPF:")
        response = get_func(cpf)
        print({'status': '200'}, response.json())

    elif valor in ["X", "x"]:
        sair = True

    else:
        print("Opção inválida. Tente novamente.")

    print('\n')
