#Se importa el módulo unittest para hacer las pruebas unitarias
import unittest

# Definición de la interfaz de estrategia.
class StaircaseStrategy:
    
    #es el método que se encarga de construir la escalera de acuerdo con la estrategia implementada por las subclases.
    def getStaircase(self, n):
        pass

# Agente A

# La clase StaircaseAgentA que implementa el método getStaircase(n) de la interfaz StaircaseStrategy, según el patrón específico.
class StaircaseAgentA(StaircaseStrategy):
    
    # Genera una cadena de texto que representa una escalera,
    # donde cada línea tiene un número creciente de caracteres #, empezando desde uno hasta n. 
    def getStaircase(self, n):
        staircase = ''
        for i in range(1, n + 1):
            staircase += ' ' * (n - i) + '#' * i + '\n'
        return staircase

# Agente B

#La clase StaircaseAgentB que implementa el método getStaircase(n) de la interfaz StaircaseStrategy, según el patrón específico.
class StaircaseAgentB(StaircaseStrategy):
    
    #El método getStaircase(n) genera una cadena de texto que representa una escalera,
    #donde cada línea tiene un número decreciente de caracteres #, empezando desde n y descendiendo hasta 1.
    def getStaircase(self, n):
        staircase = ''
        for i in range(n, 0, -1):
            staircase += ' ' * (n - i) + '#' * i + '\n'
        return staircase

# Agente C

#La clase StaircaseAgentC que implementa el método getStaircase(n) de la interfaz StaircaseStrategy, según el patrón específico.
class StaircaseAgentC(StaircaseStrategy):
    
#El método getStaircase(n) genera una cadena de texto que representa una escalera,
#donde la base y la cima son ambas iguales a n, con una distancia igual a n del centro.
    def getStaircase(self, n):
        staircase = ''
        for i in range(1, n // 2 + 1):
            staircase += ' ' * (n // 2 - i + 1) + '#' * (2 * i - 1) + '\n'
        staircase += '#' * n + '\n'
        for i in range(n // 2, 0, -1):
            staircase += ' ' * (n // 2 - i + 1) + '#' * (2 * i - 1) + '\n'
        return staircase

# Contexto

#La clase StaircaseContext actúa como un contexto que puede cambiar dinámicamente entre diferentes estrategias para construir la escalera,
#cada una representada por las clases StaircaseAgentA, StaircaseAgentB, y StaircaseAgentC.
class StaircaseContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def getStaircase(self, n):
        return self.strategy.getStaircase(n)
    
# Pruebas unitarias

#Una clase de prueba llamada TestStaircase que hereda de unittest.TestCase. 
class TestStaircase(unittest.TestCase):
    
#Crea una instancia de StaircaseContext con StaircaseAgentA como estrategia y llama al método getStaircase(4)
#para construir una escalera de tamaño 4 utilizando el Agente A.
    def test_staircase_agent_a(self):
        context = StaircaseContext(StaircaseAgentA())
        result = context.getStaircase(4)
        expected_output = '   #\n  ##\n ###\n####\n'
        self.assertEqual(result, expected_output)
        
#StaircaseAgentB como estrategia y verifica si la salida generada coincide con la salida esperada para el Agente B.
    def test_staircase_agent_b(self):
        context = StaircaseContext(StaircaseAgentB())
        result = context.getStaircase(4)
        expected_output = '####\n ###\n  ##\n   #\n'
        self.assertEqual(result, expected_output)

#StaircaseAgentC como estrategia y verifica si la salida generada coincide con la salida esperada para el Agente C.
    def test_staircase_agent_c(self):
        context = StaircaseContext(StaircaseAgentC())
        result = context.getStaircase(5)
        expected_output = '  #\n ###\n#####\n ###\n  #\n'
        self.assertEqual(result, expected_output)


#Verifica si el archivo se está ejecutando como un script principal
if __name__ == "__main__":
    
#Dependiendo de la opción seleccionada por el usuario, se instancia un objeto 
    print("Seleccione el agente para construir la escalera:")
    print("1. Agente A")
    print("2. Agente B")
    print("3. Agente C")
    choice = input("Ingrese el número correspondiente al agente: ")

    if choice == '1':
        context = StaircaseContext(StaircaseAgentA())
    elif choice == '2':
        context = StaircaseContext(StaircaseAgentB())
    elif choice == '3':
        context = StaircaseContext(StaircaseAgentC())
    else:
        
#Si el usuario ingresa una opción no válida, el programa imprime un mensaje de error y sale.
        print("Opción no válida.")
        exit()

 #Después de seleccionar el agente, el programa solicita al usuario que ingrese el tamaño de la escalera.
    n = int(input("Ingrese el tamaño de la escalera: "))
    
#Se llama al método getStaircase(n) del objeto context para construir la escalera del tamaño especificado por el usuario.
    print(context.getStaircase(n))
    
#Se ejecutan las pruebas unitarias definidas en el archivo utilizando unittest.main()
    unittest.main()

