def contar_lineas_codigo(archivo):
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            lineas_sin_comentarios = [linea.strip() for linea in lineas if not linea.strip().startswith("#") and linea.strip() != ""]
            return len(lineas_sin_comentarios)
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    if not ruta_archivo.endswith(".py"):
        print("El archivo no es un archivo .py válido.")
        return

    num_lineas = contar_lineas_codigo(ruta_archivo)
    if num_lineas is not None:
        print(f"El número de líneas de código en {ruta_archivo} es: {num_lineas}")

if __name__ == "__main__":
    main()