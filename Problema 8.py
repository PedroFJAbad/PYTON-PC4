import requests
import sqlite3

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        bitcoin_price_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        bitcoin_price_gbp = float(data['bpi']['GBP']['rate'].replace(',', ''))
        bitcoin_price_eur = float(data['bpi']['EUR']['rate'].replace(',', ''))
        return bitcoin_price_usd, bitcoin_price_gbp, bitcoin_price_eur
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None, None, None

def obtener_tipo_cambio_pen():
    try:
        response = requests.get('https://api.apis.net.pe/v2/sunat/tipo-cambio')
        response.raise_for_status()
        data = response.json()
        tipo_cambio_pen = float(data['dolar']['venta'])
        return tipo_cambio_pen
    except requests.RequestException as e:
        print(f"Error al obtener el tipo de cambio de PEN: {e}")
        return None

def crear_tabla_bitcoin(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS bitcoin (fecha TEXT, precio_usd REAL, precio_gbp REAL, precio_eur REAL, precio_pen REAL)")

def insertar_datos_bitcoin(cursor, fecha, precio_usd, precio_gbp, precio_eur, precio_pen):
    cursor.execute("INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)", (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))

def obtener_precio_compra_10_bitcoins(cursor):
    cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    row = cursor.fetchone()
    precio_pen = row[0]
    precio_eur = row[1]
    precio_compra_pen = 10 * precio_pen
    precio_compra_eur = 10 * precio_eur
    return precio_compra_pen, precio_compra_eur

def mostrar_precio_compra_10_bitcoins(cursor):
    precio_compra_pen, precio_compra_eur = obtener_precio_compra_10_bitcoins(cursor)
    print(f"El precio de compra de 10 bitcoins en PEN es: {precio_compra_pen}")
    print(f"El precio de compra de 10 bitcoins en EUR es: {precio_compra_eur}")

def main():
    # Obtener precios de Bitcoin
    precio_usd, precio_gbp, precio_eur = obtener_precio_bitcoin()
    if precio_usd is None or precio_gbp is None or precio_eur is None:
        return

    # Obtener tipo de cambio de PEN
    tipo_cambio_pen = obtener_tipo_cambio_pen()
    if tipo_cambio_pen is None:
        return

    # Calcular precio de Bitcoin en PEN
    precio_pen = precio_usd * tipo_cambio_pen

    # Conectar a la base de datos
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Crear tabla si no existe
    crear_tabla_bitcoin(cursor)

    # Insertar datos en la tabla
    fecha = datetime.now().strftime("%Y-%m-%d")
    insertar_datos_bitcoin(cursor, fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
    conn.commit()

    # Consultar y mostrar el precio de compra de 10 bitcoins en PEN y EUR
    mostrar_precio_compra_10_bitcoins(cursor)

    # Cerrar la conexión
    conn.close()

if __name__ == "__main__":
    main()