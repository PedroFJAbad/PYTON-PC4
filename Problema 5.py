class TablaMultiplicar:
    def __init__(self):
        pass

    def guardar_tabla(self, n):
        if n < 1 or n > 10:
            print("El número debe estar entre 1 y 10.")
            return

        with open(f"tabla-{n}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{n} x {i} = {n*i}\n")
        print(f"Tabla de multiplicar de {n} guardada en tabla-{n}.txt.")

    def mostrar_tabla(self, n):
        try:
            with open(f"tabla-{n}.txt", "r") as file:
                tabla = file.read()
                print(tabla)
        except FileNotFoundError:
            print("El fichero no existe.")

    def mostrar_linea(self, n, m):
        try:
            with open(f"tabla-{n}.txt", "r") as file:
                lineas = file.readlines()
                if m < 1 or m > 10:
                    print("El número de línea debe estar entre 1 y 10.")
                    return
                print(lineas[m-1])
        except FileNotFoundError:
            print("El fichero no existe.")

def menu():
    tabla = TablaMultiplicar()
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar.")
        print("2. Mostrar tabla de multiplicar.")
        print("3. Mostrar línea de la tabla de multiplicar.")
        print("4. Salir.")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            n = int(input("Ingrese un número entre 1 y 10: "))
            tabla.guardar_tabla(n)
        elif opcion == "2":
            n = int(input("Ingrese un número entre 1 y 10: "))
            tabla.mostrar_tabla(n)
        elif opcion == "3":
            n = int(input("Ingrese un número entre 1 y 10: "))
            m = int(input("Ingrese un número entre 1 y 10 para seleccionar la línea: "))
            tabla.mostrar_linea(n, m)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu()