import csv


# función para definir los tipos de datos
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
                filas[indice[0]][dato[0]] = f'"{dato[1]}"'
    return filas


def procesar_archivo(nombre_archivo):
    # leer el archivo csv, convertir cada fila en una lista y guardar todo en una lista
    with open(f"{nombre_archivo}.csv", "r", errors="ignore") as archivo_csv:
        archivo = csv.reader(archivo_csv, delimiter=";")
        filas = [fila for fila in archivo]
    # crear la primera fila del script sql que identifica los atributos de la tabla
    # (se elimina el primer elemento de la lista)
    with open(f"{nombre_archivo}.sql", "w") as insert_into:
        insert_into.write(
            f"INSERT INTO {nombre_archivo} ({', '.join(filas.pop(0))})\nVALUE\n"
        )
        definir_datos(filas)
        for i in enumerate(filas):
            if i[0] == len(filas) - 1:
                insert_into.write(f"({', '.join(i[1])});")
            else:
                insert_into.write(f"({', '.join(i[1])}),\n")


analizar = input("Ingresa el nombre del archivo CSV: ")
procesar_archivo(analizar)

