from abc import ABC, abstractmethod
import statistics
import unittest


class MediaStrategy(ABC):
    @abstractmethod
    #Define un método abstracto get_media(data), que debe ser implementado por todas las clases que hereden de ella.
    def get_media(self, data):
        pass
    
# Agente A: implementa concreta de la clase MediaStrategy.
# Sobrescribe el método get_media(data) para calcular la media aritmética o promedio
class AgenteA(MediaStrategy):
    def get_media(self, data):
        return sum(data) / len(data)

# Agente B: implementa la interfaz MediaStrategy para calcular la media armónica de una lista de números proporcionada.
class AgenteB(MediaStrategy):
    def get_media(self, data):
        if 0 in data:
            return 0
        return len(data) / sum(1 / x for x in data)

# Agente C: implementa el método get_media(self, data). Esta clase forma parte de una jerarquía de clases en un programa
# que calcula la media de una lista de números utilizando diferentes estrategias.
class AgenteC(MediaStrategy):
    def get_media(self, data):
        return statistics.median(data)
    
# MediaContext actúa como un contexto para calcular la media de una lista de números utilizando diferentes estrategias
# implementadas por los agentes A, B y C.
class MediaContext:
    
#El método constructor recibe una estrategia como parámetro y la asigna al atributo strategy.
    def __init__(self, strategy):
        self.strategy = strategy

#Este método permite cambiar dinámicamente la estrategia utilizada para calcular la media.
    def set_strategy(self, strategy):
        self.strategy = strategy

# Este método utiliza la estrategia actual (almacenada en self.strategy) para calcular y devolver la media de la lista de números.
    def get_media(self, data):
        return self.strategy.get_media(data)


class TestMedia(unittest.TestCase):
    
#Prueba la funcionalidad del agente A (media aritmética o promedio) calculando la media de una lista de números
    def test_media_agente_a(self):
        context = MediaContext(AgenteA())
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(context.get_media(data), 3.0)

#Prueba la funcionalidad del agente B (media armónica) calculando la media de la misma lista de números
    def test_media_agente_b(self):
        context = MediaContext(AgenteB())
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(context.get_media(data), 2.18978102189781)

#Prueba la funcionalidad del agente C (mediana) calculando la media de la misma lista de números
    def test_media_agente_c(self):
        context = MediaContext(AgenteC())
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(context.get_media(data), 3)
        
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

# Seleccionar el agente
    print("Seleccione el agente para calcular la medida:")
    print("1. Agente A (Media aritmética o promedio)")
    print("2. Agente B (Media armónica)")
    print("3. Agente C (Mediana)")
    choice = input("Ingrese el número correspondiente al agente: ")

    context = MediaContext(None)
    if choice == '1':
        context.set_strategy(AgenteA())
    elif choice == '2':
        context.set_strategy(AgenteB())
    elif choice == '3':
        context.set_strategy(AgenteC())
    else:
        
#Si elige una opción inválida mostrará un error y sale.
        print("Opción no válida.")
        exit()

#Muestra el resultado de calcular la media utilizando el contexto y la estrategia seleccionada previamente.
    print("La media es:", context.get_media(data))

#Se utiliza para ejecutar todas las pruebas unitarias definidas en el script
    unittest.main()
