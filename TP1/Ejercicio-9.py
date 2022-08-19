import random
# listas

cantidad = []
naranjas = []
jugo = []
listaCajones = []
listaCamiones = []
sumatoria = []
listaCamionesCompletos = []
listaSobrante = []


# chequea que el ingreso hecho por teclado sea un entero

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


# envia las naranjas dentro del peso precisado a una lista, y las que estan fuera de rango a otra

def contarNaranja():
    for i in cantidad:
        aux = i
        if 200 <= aux <= 300:
            naranjas.append(aux)
        else:
            jugo.append(aux)
    return naranjas, jugo


# se calcula la cantidad de cajones que se pueden meter lo mas optimo en un camion de 500kg

def calcularCamiones():
    while sum(listaCajones) != 0:
        suma = 0
        for cajon in listaCajones:
            for caja in matriz:
                for naranja in caja:
                    sum naranja + narnja #Idea abstracta
                    
            if 500000-cajon >= suma:
                suma = suma + cajon

                listaCajones[listaCajones.index(cajon)] = 0
        listaCamiones.append(suma)

    return listaCamiones

# introduce 100 naranjas por cajon y suma los pesos

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

# recorre la lista de camiones y agrega a segun que lista dependiendo si cuenta con mas del 80% del peso o no

def extraerResto():
    for camion in listaCamiones:
        if camion >= 400000:
            listaCamionesCompletos.append(camion/1000)
        else:
            listaSobrante.append(camion/1000)
            
    return listaCamionesCompletos, listaSobrante

def rellenarCamiones():
    for camion in listaCamionesCompletos:
        if camion<498:
            pass

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
