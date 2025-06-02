from usuariocomum import UsuarioComum

class UsuarioAdiministrador(UsuarioComum):
    def __init__(self, nome:str, email:str, n_acesso:str):
        self.nome = nome
        self.email = email
        self.nivel_acesso = n_acesso
        self.data = "banco_usuarios.txt"

    def cadastrar(self):
        with open(self.data, "a") as arquivo:
            arquivo.write(f"\n{self.nome}->{self.email}->{self.nivel_acesso}")
            print(f"Usuário {self.nome} cadastrado!")
            return
    
    def verify(self):
        try:
            with open(self.data, "r") as arquivo:
                #verifica usuario duplicado 
                for linha in arquivo:
                    user = (f"{self.nome}->{self.email}->{self.nivel_acesso}")
                    if linha.strip() == user.strip():
                        print(f"Usuário {self.nome} já cadastrado!")
                        #return

                    self.cadastrar()
                    return
        except FileNotFoundError: 
            print("Iniciando arquivo de dados...")
            self.cadastrar()
            #return