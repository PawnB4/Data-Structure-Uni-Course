# Bautista Novarese, Tomás Bond, Franco Pascual, Ivan Faifer, Julian Contreras -- UADE // Agoritmos & Estructura de Datos - Viernes / Mañana

import random

#Variables
cantidad = []
naranjas = []
jugo = []
listaCajones = []
listaCamiones = []
sumatoria = []
listaCamionesCompletos = []
listaSobrante = []


# Funcion encargada de verificar el que el tipo de dato sea int.
def check_input(entrada):
    try:
        int(entrada)
        return True
    except ValueError:
        try:
            float(entrada)
            return False
        except ValueError:
            return False

def ingresarCantidad():
    bandera = True
    while bandera:
        n = input("Ingrese la cantidad de naranjas: ")
        if check_input(n):
            val = int(n)
            for i in range(0, val):
                cantidad.append(random.randint(150, 350))
                bandera = False
        else:
            print("Por favor, ingrese un valor válido.")
    return cantidad


def contarNaranja():
    for i in cantidad:
        aux = i
        if 200 <= aux <= 300:
            naranjas.append(aux)
        else:
            jugo.append(aux)
    return naranjas, jugo


# Funcion encargada de calcular la cantidad de cajones. Retorna una lista con los pesos de cada cajon.
def calcularCajones():
    naranjas.sort(reverse=True)
    n = 100
    matrizCajones = [naranjas[i:i + n] for i in range(0, len(naranjas), n)]
    for cajon in matrizCajones:  # Acceso a cada cajon
        suma = 0
        for naranja in cajon:  # Acceso las naranjas de cada cajon
            suma = (suma + naranja)
        listaCajones.append(suma)
        
    return listaCajones


# Funcion encargada de introducir cajones a los camiones. Se intenta llegar lo mas cerca a 500kg.
def calcularCamiones():
    while sum(listaCajones) != 0:
        suma = 0
        for cajon in listaCajones:
            if 500000-cajon >= suma:
                suma = suma + cajon
                listaCajones[listaCajones.index(cajon)] = 0 # ==> Por cajon agregado se "borra" de la lista de cajones. 
        listaCamiones.append(suma)

    return listaCamiones


# Funcion encargada de verificar que los camiones sean superiores a 400kg (80% capacidad).
def extraerResto():
    for camion in listaCamiones:
        if camion >= 400000:
            listaCamionesCompletos.append(camion/1000)
        else:
            listaSobrante.append(camion/1000)
            
    return listaCamionesCompletos, listaSobrante


def main():
    ingresarCantidad()
    contarNaranja()
    cajones = len(calcularCajones())
    calcularCamiones()
    extraerResto()
    listaCamionesCompletos.sort(reverse=True)

    print(
        f'Naranjas para jugo: {len(jugo)}\nNarajas para exportar: {len(naranjas)}\nPeso total de naranjas a exportar: {sum(naranjas)/1000}kg')
    print(
        f'Cantidad total de cajones: {cajones}\nCantidad de camiones: {len(listaCamionesCompletos)}\nPesos de cada camión: {listaCamionesCompletos}\nSobrante para la próxima cosecha: {listaSobrante}')


if __name__ == "__main__":
    main()
