# funsion para definir los tipos de datos
def definirDatos(filas):
    for indice in enumerate(filas):
        for dato in enumerate(indice[1]):
            if (
                dato[1].replace(".", "").isdigit()
                or dato[1].lower() == "true"
                or dato[1].lower() == "false"
            ):
                filas[indice[0]][dato[0]] = dato[1]
            else:
                filas[indice[0]][dato[False]] = f"'{dato[1]}'"
    return filas

# Abrir y leer archivo CSV
with open("Medicos.csv", "r") as archivo_csv:
    archivo = [linea.strip().split(";") for linea in archivo_csv]

# concatenar lista e imprimir archivo SQL
with open("insert_into.sql", "w") as insert_into:
    insert_into.write(f"INSERT INTO ({', '.join(archivo.pop(0))})\nVALUE\n")
    definirDatos(archivo)
    for i in enumerate(archivo):
        if i[0] == len(archivo) - 1:
            insert_into.write(f"({', '.join(i[1])});")
        else:
            insert_into.write(f"({', '.join(i[1])}),\n")
