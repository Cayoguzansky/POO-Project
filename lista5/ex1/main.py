from usuariocomum import UsuarioComum
from usuarioadministrador import UsuarioAdiministrador

def main():

    u1 = UsuarioComum("João", "joaoabs@gmail.com")
    u2 = UsuarioAdiministrador("Maria", "mariazinha@gmail.com", "Admin")
    u3 = UsuarioComum("João", "joaoabs@gmail.com")

    u1.verify()
    u2.verify()
    u3.verify()

if __name__ == "__main__":
    main()