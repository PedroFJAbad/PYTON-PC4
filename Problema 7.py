import requests

def obtener_tipo_cambio_anio(year):
    url = f'https://api.apis.net.pe/v2/sunat/tipo-cambio?year={year}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f"Error al obtener los datos del API para el año {year}.")
        return None

def mostrar_datos(datos):
    for item in datos:
        print(f"Fecha: {item['fecha']}, Compra: {item['compra']}, Venta: {item['venta']}")

def main():
    year = 2023
    datos = obtener_tipo_cambio_anio(year)
    if datos:
        mostrar_datos(datos)

if __name__ == "__main__":
    main()