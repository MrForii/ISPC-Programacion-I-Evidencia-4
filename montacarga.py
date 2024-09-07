import time
import sys

class Montacarga:
    def __init__(self, pasillo, carga_maxima):
        self.__pasillo = pasillo              # Aqui vamos a indicar la cantidad de pasillos que posee el edificio donde trabaja
        self.__pasillo_actual = 0             # Aqui se indicara el pasillo en el que esta situado el montacarga
        self.__carga_actual = 0               # Aqui indicaremos la carga que posee la montacarga
        self.__carga_maxima = carga_maxima    # Aqui indicaremos la capacidad maxima de la montacarga
        self.__encendido = False              # Aqui indicaremos si la montacarga se encuentra encendida

    # Metodos accesores (getters y setters)
    def get_pasillo(self):
        return self.__pasillo

    def get_pasillo_actual(self):
        return self.__pasillo_actual

    def set_pasillo_actual(self, pasillo_actual):
        self.__pasillo_actual = pasillo_actual

    def get_carga_actual(self):
        return self.__carga_actual

    def set_carga_actual(self, carga_actual):
        self.__carga_actual = carga_actual

    def get_carga_maxima(self):
        return self.__carga_maxima

    def get_encendido(self):
        return self.__encendido

    def set_encendido(self, encendido):
        self.__encendido = encendido

    # Metodos a definir:
    # Encender -- Se encarga de encender el motor de la montacarga
    # Apagar -- Se encarga de apagar el motor de la montacarga
    # Mover -- Se encarga de mover la montacarga a un pasillo de destino
    # Cargar -- Se encarga de agregar carga al montacarga
    # Descargar -- Se encarga de descargar la carga del montacarga
    # Ver_estado -- Se encarga de mostrar la informacion de la montacarga

    def encender(self):
        imprimir_lentamente("🚨 Encendiendo Montacarga...    ✅ Montacarga Encendido!\n", retraso=0.05)
        self.set_encendido(True)

    def apagar(self):
        imprimir_lentamente("🚨 Apagando Montacarga...    ✅ Montacarga Apagado!\n", retraso=0.05)
        self.set_encendido(False)


    def mover(self, destino):
        if not self.get_encendido():
            print("❌ Montacarga apagado. Por favor encienda el montacarga para poder moverlo.\n")
         
        # Vamos a comprobar que el usuario no ingrese un numero que sea negativo o mayor al numero total de pasillos
        elif destino < 0: 
            print(f"❌ El destino esta fuera de rango. No se puede mover.\n")

        elif destino >= self.get_pasillo():
            print(f"❌ El destino esta fuera de rango. No se puede mover.\n")

        # Vamos a comprobar que el usuario no quiera mover el montacarga al mismo pasillo en el que esta situado
        elif destino == self.get_pasillo_actual():
            print(f"❌ El montacarga ya se encuentra en el pasillo {destino}.\n")

        else:
            # Si no se cumple lo anterior, entonces el usuario puede mover la montacarga
            self.set_pasillo_actual(destino)
            imprimir_lentamente("🚨 Moviendo montacarga...\n", retraso=0.05)
            print(f"✅ El montacarga se ha movido al pasillo {destino}.\n")


    def cargar_montacarga(self, carga):
        if not self.get_encendido():
            print("❌ Montacarga apagado. Por favor encienda el montacarga para poder cargarlo.\n")
        
        else:
            # Vamos a comprobar que el usuario no ingrese un numero que sea negativo
            if carga < 0:
                print("❌ El valor de la carga no puede ser negativo. Por favor intente de nuevo.\n")

            # Vamos a comprobar que el usuario no quiera cargar mas de la capacidad maxima de la montacarga
            else:
                carga_provisoria = self.get_carga_actual() + carga
                if carga_provisoria > self.get_carga_maxima():
                    print(f"❌ El montacarga no puede cargar {carga} kg. Carga maxima: {self.get_carga_maxima()} kg.\n")
                
                else:
                    # Si no se cumple lo anterior, entonces el usuario puede cargar la montacarga
                    self.set_carga_actual(carga_provisoria)
                    imprimir_lentamente("🚨 Cargando Montacarga...\n", retraso=0.05)
                    print(f"✅ Se han cargado {carga} kg al montacarga. Carga actual: {self.get_carga_actual()} kg.\n")


    def descargar_montacarga(self, carga):
        if not self.get_encendido():
            print("❌ Montacarga apagado. Por favor encienda el montacarga para poder descargarlo.\n")
        else:
            # Vamos a comprobar que el usuario no ingrese un numero que sea negativo
            if carga < 0:
                print("❌ El valor de la carga no puede ser negativo. Por favor intente de nuevo.\n")
            else:
                # Vamos a comprobar que el usuario no quiera descargar mas de la carga que tiene la montacarga
                if carga > self.get_carga_actual():
                    print(f"❌ No hay suficiente carga para descargar {carga} kg. Carga actual: {self.get_carga_actual()} kg.\n")
                else:
                    # Si no se cumple lo anterior, entonces el usuario puede descargar la montacarga
                    self.set_carga_actual(self.get_carga_actual() - carga)
                    imprimir_lentamente("🚨 Descargando Montacarga...\n", retraso=0.05)
                    print(f"✅ Se han descargado {carga} kg del montacarga. Carga actual: {self.get_carga_actual()} kg.\n")

    def __str__(self):
        if not self.get_encendido():
            print("🚨 Montacarga apagado. Por favor encienda el montacarga para poder moverlo.")
        else:
            print(f"✅ El montacarga se encuentra encendido.")
        print(f"🚧 El montacarga se encuentra en el pasillo {self.get_pasillo_actual()}.")
        print(f"🚧 El montacarga tiene {self.get_carga_actual()} kg de carga.\n")


""" FUNCIONES PARA ESTILOS DE PYTHON """

def imprimir_lentamente(texto, retraso=0.05, retraso_inicio=1):
    """
    Imprime el texto en la consola caracter por caracter con un retraso.
    
    :param texto: El texto que se quiere imprimir.
    :param retraso: Tiempo en segundos entre la impresión de cada carácter.
    """
    time.sleep(retraso_inicio)
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()  # Asegura que el texto se imprime inmediatamente
        time.sleep(retraso)
    time.sleep(retraso_inicio)
    print()  # Imprime una nueva línea al final
