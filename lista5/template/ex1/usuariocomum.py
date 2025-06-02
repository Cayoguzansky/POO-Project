from usuario import Usuario

class UsuarioComum(Usuario):
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def cadastrar(self, banco_dados):
        if self.email in banco_dados:
            print(f"Usuário {self.email} já cadastrado.")
        else:
            banco_dados[self.email] = {'nome': self.nome, 'tipo': 'comum'}
            print(f"Usuário comum {self.nome} cadastrado com sucesso.")