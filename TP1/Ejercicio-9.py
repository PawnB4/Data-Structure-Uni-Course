# Resolver el siguiente problema diseñando y utilizando funciones:

# La empresa cuenta con N camiones, y
# cada  uno  puede  transportar  hasta  media  tonelada  (500  kilogramos).
# En  un  cajón caben 100 naranjas con un peso entre 200 y 300 gramos cada una.
# Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo.
# Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden llenar,
# cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto.
# Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.Además,
# se  desea  saber  cuántos  camiones  se  necesitan  para  transportar  la  cosecha,  considerando
# que  la  ocupación  del  camión  no  debe  ser  inferior  al  80%;  en caso contrario el camión no serán despachado por su alto costo.

# _______________________________________________________________________________________________________________________________________________
# cada camion: minimo 400kg max 500kg
# cajon: maximo 100 naranjas.
# naranjas: peso entre 200 y 300 / Peso fuera de rango => naranja para jugo
# _______________________________________________________________________________________________________________________________________________

import random

cantidad = []
naranjas = []
jugo = []
cajones = []


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
        # print(cantidad.index(i))
        aux = i
        if 200 <= aux <= 300:
            naranjas.append(aux)
        else:
            jugo.append(aux)
    return naranjas, jugo


def cajonesNaranja():
    naranjas.sort(reverse=True)
    # print(naranjas)
    # print(split(range(len(naranjas)), 100))
    n = 100
    output = [naranjas[i:i + n] for i in range(0, len(naranjas), n)]
    print(output)

    # for i in range(len(naranjas)):


    sumatoria = 0
    while True:
        for i in range(len(naranjas)):
            sumatoria += naranjas[i]
            
        cajones.append(sumatoria/1000)
        print()

    # return cajones


def main():
    ingresarCantidad()
    contarNaranja()
    print("Naranjas para jugo: ", len(jugo))
    print("Naranjas para exportar: ", len(naranjas))
    print("Peso total kg narnjas exportar: ", sum(naranjas)/1000)
    cajonesNaranja()
    print(cajones)
    print(sum(cajones))


if __name__ == "__main__":
    main()


