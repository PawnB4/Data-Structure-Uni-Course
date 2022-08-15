bandera = []
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


def carga_categoria(lista_cat):
    print("\n--- Carga de Vehículo --- \n")
    categoria_letra = input("Ingrese categoría: ")

    if categoria_letra != "F":
        while categoria_letra != "A" and categoria_letra != "B" and categoria_letra != "C" and categoria_letra != "D" and categoria_letra != "E":
            print("Parametro inválido. Ingrese nuevamente")
            categoria_letra = input("Ingrese categoría: ")
        else:
            lista_cat.append(categoria_letra)
    else:
        bandera.append("F")


def carga_registro(list_reg):
    numeroReg = input("Ingrese un numero de registro: ")
    boleano = True
    while boleano:
        if check_input(numeroReg):
            val = int(numeroReg)
            if 10000 <= val <= 99999 and not (val in list_reg):
                list_reg.append(val)
                boleano = False
            else:
                numeroReg = input(
                    ("Ingrese un nuevo numero de cinco cifras: "))
        else:
            numeroReg = input(("Ingrese un numero: "))


def carga_anio(lista_year):
    numeroAnio = input(
        "Ingrese el año de fabricación del vehículo (1975 a 1990): ")
    boleano = True
    while boleano:
        if check_input(numeroAnio):
            val = int(numeroAnio)
            if 1975 <= val <= 1990:
                lista_year.append(val)
                boleano = False
            else:
                numeroAnio = input(
                    ("Ingrese un año desde 1975 a 1990: "))
        else:
            numeroAnio = input(("Ingrese un año: "))


def ordenarBurbuja(categorias, registros, anios, pago):
    for i in range(0, len(categorias)-1):
        for j in range(i+1, len(categorias)):
            if categorias[i] > categorias[j]:
                aux = categorias[j]
                categorias[j] = categorias[i]
                categorias[i] = aux

                aux = registros[j]
                registros[j] = registros[i]
                registros[i] = aux

                aux = anios[j]
                anios[j] = anios[i]
                anios[i] = aux

                aux = pago[j]
                pago[j] = pago[i]
                pago[i] = aux
    return categorias, registros, anios, pago

# busca el registro que ingresaste por teclado y lo valida y carga los pagos


def busqueda(registros, categorias, anios, tributos):
    boleano = True
    while boleano:
        numero_registro = input("Ingrese el numero de registro a buscar: ")
        if check_input(numero_registro):
            val = int(numero_registro)
            if val in registros:
                indice = registros.index(val)
                print("Auto seleccionado: ",
                      categorias[indice], registros[indice], anios[indice])
                importe = input("Ingrese el monto correspondiente: ")
                flag = True
                while flag:

                    if check_input(importe):
                        pago = int(importe)
                        if categorias[indice] == "A":
                            if pago == 10000:
                                tributos[indice] = pago
                                flag = False
                            else:
                                importe = input("Ingrese un monto válido: ")
                        if categorias[indice] == "B":
                            if pago == 12000:
                                tributos[indice] = pago
                                flag = False
                            else:
                                importe = input("Ingrese un monto válido: ")
                        if categorias[indice] == "C":
                            if pago == 13000:
                                tributos[indice] = pago
                                flag = False
                            else:
                                importe = input("Ingrese un monto válido: ")
                        if categorias[indice] == "D":
                            if pago == 14000:
                                tributos[indice] = pago
                                flag = False
                            else:
                                importe = input("Ingrese un monto válido: ")
                        if categorias[indice] == "E":
                            if pago == 15000:
                                tributos[indice] = pago
                                flag = False
                            else:
                                importe = input("Ingrese un monto válido: ")
                    else:
                        importe = input(("Ingrese un importe valido: "))
            elif val == 0:
                boleano = False
            else:
                print("Por favor, ingrese un numero de registro válido.")
        else:
            print("Por favor, ingrese un numero de registro.")


def main():

    numero_interno = []
    categoria = []
    anio = []
    importes = []

    # Carga de datos

    while len(anio) < 900 and not ("F" in bandera):
        carga_categoria(categoria)
        if not ("F" in bandera):
            carga_registro(numero_interno)
            carga_anio(anio)

    print("\n---Finalización de carga de datos ---\n")

    for i in range(len(numero_interno)):
        importes.append(0)

    busqueda(numero_interno, categoria, anio, importes)

    # Ordenamiento de listas
    ordenarBurbuja(categoria, numero_interno, anio, importes)

    # crea la matriz
    print("CATEGORIA \t IMPORTE")
    for i in range(len(categoria)):
        print(categoria[i], "\t \t", importes[i])
    print("Total: \t \t$", sum(importes))

    print("\nEl año del vehículo más antiguo es: ", min(anio))


if __name__ == "__main__":
    main()
