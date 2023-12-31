from particula import Particula
import json

class listaParticulas:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def mostrar(self):
        for p in self.__particulas:
            print(p)

    def ordenar_porDistancia(self, particula:Particula):
        self.__particulas.sort(reverse = True, key = lambda particula: particula.distancia)
        # self.__particulas.sort(reverse = True)

    def ordenar_porVelocidad(self, particula:Particula):
        self.__particulas.sort(key =  lambda particula: particula.velocidad)

    def ordenar_porID(self, particula:Particula):
        self.__particulas.sort(key = lambda particula: particula.id)

    def __str__(self):
        return "".join(
            str(p) + "\n" for p in self.__particulas
        )
    
    def __len__(self):
        return(
            len(self.__particulas)
        )
    
    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        
        else:
            raise StopIteration
        
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
                return 1
        except:
            return 0
        
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
            
        except:
            return 0