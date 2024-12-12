class Animal :
    def emitir_som():
        print("Grunhido")

class Cachorro(Animal):

    def emitir_som(self):
        print("Au Au")

class Gato(Animal):

    def emitir_som(self):
        print("Miau")

class Vaca(Animal):

    def emitir_som(self):
        print("Muu")

cachorro =  Cachorro()
cachorro.emitir_som()

gato =  Gato()
gato.emitir_som()

vaca =  Vaca()
vaca.emitir_som()