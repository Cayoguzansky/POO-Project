from usuario import Usuario

class UsuarioComum(Usuario):
    def __init__(self, nome:str, email:str):
        self.nome = nome
        self.email = email
        self.data = "banco_usuarios.txt"
    
    def cadastrar(self):
        with open(self.data, "a") as arquivo:
            arquivo.write(f"\n{self.nome}->{self.email}")
            print(f"Usuário {self.nome} cadastrado!")
    
    def verify(self):
        try:
            with open(self.data , "r") as arquivo:
                #verifica usuario duplicado 
                for linha in arquivo:
                #linhas = [linha.strip() for linha in arquivo]
                    #print(f"{linha.strip()}")
                    user = (f"{self.nome}->{self.email}")
                    if user.strip() in linha.strip():
                        print(f"Usuário {self.nome} já cadastrado!")
                        return

                self.cadastrar()
        except FileNotFoundError:
            print("Iniciando arquivo de dados...")
            self.cadastrar()