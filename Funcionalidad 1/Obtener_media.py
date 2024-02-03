import statistics

#Se define una clase abstracta MediaStrategy que especifica un método get_media(data).
class MediaStrategy:
    def get_media(self, data):
        pass

# Agente A: calcula la media aritmética o promedio de los datos.
class AgenteA(MediaStrategy):
    def get_media(self, data):
        return sum(data) / len(data)

# Agente B: calcula la media armónica de los datos.
class AgenteB(MediaStrategy):
    def get_media(self, data):
        if 0 in data:
            return 0
        return len(data) / sum(1 / x for x in data)

# Agente C: calcula la mediana de los datos utilizando la función median del módulo statistics.
class AgenteC(MediaStrategy):
    def get_media(self, data):
        return statistics.median(data)

# MediaContext actúa como el contexto para la selección dinámica del agente y el cálculo de la media.
class MediaContext:
    def __init__(self, strategy):
        self.strategy = strategy

#Se usa para establecer la estrategia que se utilizará para el cálculo de la media.
    def set_strategy(self, strategy):
        self.strategy = strategy

#Invoca el método get_media(data) de la estrategia seleccionada para calcular la media
    def get_media(self, data):
        return self.strategy.get_media(data)

# Prueba del sistema
if __name__ == "__main__":
    #Se define una lista de números reales
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Seleccione el agente para calcular la medida:")
    print("1. Agente A (Media aritmética o promedio)")
    print("2. Agente B (Media armónica)")
    print("3. Agente C (Mediana)")
    choice = input("Ingrese el número correspondiente al agente: ")

    #Actúa como el contexto para la selección dinámica del agente y el cálculo de la media.
    context = MediaContext(None)
    if choice == '1':
        context.set_strategy(AgenteA())
    elif choice == '2':
        context.set_strategy(AgenteB())
    elif choice == '3':
        context.set_strategy(AgenteC())
    else:
        
    #Dependiendo de la elección del usuario, se establece la estrategia correspondiente en el contexto.
    #Si se selecciona una opción no valida, muestra un error y sale.
        print("Opción no válida.")
        exit()

    #Se calcula la media utilizando la estrategia seleccionada y se muestra el resultado.
    print("La media es:", context.get_media(data))
