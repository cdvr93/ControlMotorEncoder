"""Control de motor paso a paso.

Boceto de un posible proceso para control de paso a paso A VELOCIDAD CONSTANTE.
En este ejemplo no se tiene encuenta la aceleracion y el codigo está diseñado
para mover el motor a una velocidad constante.

Para futuras referencias, al agregar aceleracion, se puede utilizar
la siguiente referencia. Una libreria en C++ para arduino que tiene control de
velocidad y aceleracion:
https://www.airspayce.com/mikem/arduino/AccelStepper/
https://forum.arduino.cc/index.php?topic=489323.0

"""
# Importacion de librerias

import time
import matplotlib.pyplot as plt


# Datos de entrada
PPV = 3200  # pasos por vuelta completa del motor
VEL_INI = 1  # velocidad inicial (rpm)
duty = 0.5  # porcentaje del duty de 0 a 1 (tiempo on/off)

# Aclaraciones sobre el duty: El duty es el porcentaje de tiempo encendido
# y tiempo apagado. Un duty de 0.5 (50%) indica que el pulso en alto ocupa
# la mitad del tiempo total de la onda, por tanto, el tiempo de apagado dura
# lo mismo que el tiempo de encendido.

# Inicializacion de algunas variables
t_ant_p = 0
salida_act = 0


def trans_vel(vel_entrada):
    """Funcion para transformar velocidad.

    Toma una velocidad de entrada y la transforma en el intervalo
    de tiempo entre pasos para que el motor pueda recorrer la distancia
    en esa velocidad. 

    Parameters
    ----------
    vel_entrada: float
        Velocidad de entrada en revoluciones por minuto.

    Returns
    -------
    itep: float
        Intervalo de Tiempo entre Pasos (en milisegundos).

    """
    # 1rpm = 1 vuelta del motor / 1min
    # 1rpm = 1 vuelta / 60 ms
    # entonces:
    itep = (60/vel_entrada)/PPV  # el tiempo entre pasos (en segundos)
    return itep


def dar_paso(estado_act, t_entre_pasos, t_ant=0, t_act_p=0):
    """Funcion para dar los pasos del motor.

    Aqui se programa la ejecucion del paso, si se usa raspberry se programaria
    la escritura de los puertos seriales. En este caso se reemplazara por
    "salida" a modo de ejemplo.

    Parameters
    ----------
    estado_act: Bool
        Estado actual de la salida GPIO en el momento. Inicializado en 0.
    t_entre_pasos: Float
        Tiempo entre pasos.
    t_ant: Float
        Ultimo tiempo en el que se hizo un cambio alto en el estado.
        Inicializado en 0.

    Returns
    -------
    salida: Bool
        Estado final del puerto GPIO.
    t_ant: Float
        Devuelve el tiempo actualizado en el que se cambio el estado.

    """
    salida = estado_act
    dift = t_act_p - t_ant  # Calcula diferencia de tiempos
    # Si la diferencia supera el periodo, es momento de cambiar el pulso
    if estado_act == 1 and dift >= t_entre_pasos*(1-duty):
        t_ant = t_act_p
        salida = 0  # Aqui se desactivaria la GPIO
    if estado_act == 0 and dift >= t_entre_pasos*(duty):
        t_ant = t_act_p
        salida = 1  # Aqui se activaria la GPIO
    return salida, t_ant


if __name__ == "__main__":
    """Funcion principal.

    Para efectos de este ejemplo, se graficaran las salidas en 10 intervalos de
    tiempo, a dos velocidades diferentes para apreciar el cambio de frecuencia.
    """
    # ---------------------------PRIMERA MARCHA-----------------------------
    # Definiendo velocidades entrada en rpm:
    VEL1 = 0.5
    # Iniciando rutina para velocidad 1:
    # Creando algunas listas para almacenar datos y graficarlos:
    tiempos = [0]
    estados = [0]
    periodo = trans_vel(VEL1)  # Calcula el periodo con la funcion de arriba
    while len(estados) < 10:
        t_act = time.perf_counter()  # Toma el tiempo actual y procede
        salida_act, t_ant_p = dar_paso(salida_act, periodo, t_ant_p, t_act)

        # Esto es OPCIONAL: se llenan los vectores para graficar
        if estados[-1] != salida_act:
            estados.append(salida_act)
            tiempos.append(t_ant_p)

    # ---------------------------SEGUNDA MARCHA-----------------------------
    # Definiendo velocidades entrada en rpm:
    VEL2 = 2
    # Iniciando rutina para velocidad 2:
    # Creando algunas listas para almacenar datos y graficarlos:
    tiempos2 = [0]
    estados2 = [0]
    periodo = trans_vel(VEL2)  # Calcula el periodo
    t_ant_p = 0
    while len(estados2) < 15:
        t_act = time.perf_counter()
        salida_act, t_ant_p = dar_paso(salida_act, periodo, t_ant_p, t_act)

        # Esto es OPCIONAL: se llenan los vectores para graficar:
        if estados2[-1] != salida_act:
            estados2.append(salida_act)
            tiempos2.append(t_ant_p)

    # ---------------------------------GRAFICAMOS (OPCIONAL)------------------
    # Se grafica para visualizacion
    plt.plot(tiempos[2:], estados[2:], 'b',
             drawstyle='steps-pre', label=f'{VEL1}rpm')
    plt.plot(tiempos2[2:], estados2[2:], 'r',
             drawstyle='steps-pre', label=f'{VEL2}rpm')
    plt.legend()
    plt.show()
