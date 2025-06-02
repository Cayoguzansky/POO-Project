from gato import Gato
from cachorro import Cachorro

def main():
    animais = [Gato("Rajado", "Mike"), Cachorro("Poodle", "Sharlot")]

    for animal in animais:
        print (animal.nome, ":", animal.emitir_som())

    
if __name__ == "__main__":
    main()