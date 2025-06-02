from usuariocomum import UsuarioComum

class UsuarioAdministrador(UsuarioComum):
    
    def __init__(self, nome, email, nivel_acesso):
        super().__init__(nome, email)
        self.nivel_acesso = nivel_acesso

    def cadastrar(self, banco_dados):
        if self.email in banco_dados:
            print(f"Administrador {self.email} já cadastrado.")
        else:
            banco_dados[self.email] = {
                'nome': self.nome,
                'tipo': 'admin',
                'nivel_acesso': self.nivel_acesso
            }
            print(f"Administrador {self.nome} cadastrado com sucesso.")