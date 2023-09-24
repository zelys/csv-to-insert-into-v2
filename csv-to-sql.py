# funsion para definir los tipos de datos
def definir_datos(filas):
    for indice in enumerate(filas):
        for dato in enumerate(indice[1]):
            if (
                dato[1].replace(".", "").isdigit()
                or dato[1].lower() == "true"
                or dato[1].lower() == "false"
            ):
                filas[indice[0]][dato[0]] = dato[1]
            elif dato[1].find("-") == 2:
                filas[indice[0]][
                    dato[0]
                ] = f"'{dato[1][6:] + dato[1][2:6] + dato[1][0:2]}'"
            else:
                filas[indice[0]][dato[0]] = f"'{dato[1]}'"
    return filas


def procesar_archivo(nombre_archivo):
    # Abrir y leer archivo CSV
    with open(f"{nombre_archivo}.csv", "r") as archivo_csv:
        archivo = [linea.strip().split(";") for linea in archivo_csv]

    # concatenar lista e imprimir archivo SQL
    with open(f"{nombre_archivo}.sql", "w") as insert_into:
        insert_into.write(f"INSERT INTO ({', '.join(archivo.pop(0))})\nVALUE\n")
        definir_datos(archivo)
        for i in enumerate(archivo):
            if i[0] == len(archivo) - 1:
                insert_into.write(f"({', '.join(i[1])});")
            else:
                insert_into.write(f"({', '.join(i[1])}),\n")


analizar = input("Ingresa el nombre del archivo CSV: ")
procesar_archivo(analizar)
