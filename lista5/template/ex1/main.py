#from usuario import Usuario
from usuariocomum import UsuarioComum
from usuarioadmin import UsuarioAdministrador

def salvar_banco_em_arquivo(banco_dados, nome_arquivo="banco_usuarios.txt"):
    with open(nome_arquivo, "w") as f:
        for email, dados in banco_dados.items():
            linha = f"{dados['nome']},{email},{dados['tipo']}"
            if dados['tipo'] == 'admin':
                linha += f",{dados['nivel_acesso']}"
            f.write(linha + "\n")

def main_ex1():
    banco_dados = {}

    u1 = UsuarioComum("João", "joao@email.com")
    u2 = UsuarioAdministrador("Maria", "maria@email.com", "admin")
    u3 = UsuarioComum("João", "joao@email.com")  # duplicado

    u1.cadastrar(banco_dados)
    u2.cadastrar(banco_dados)
    u3.cadastrar(banco_dados)

    salvar_banco_em_arquivo(banco_dados)

if __name__ == "__main__":
    print("Executando Exercício 1")
    main_ex1()