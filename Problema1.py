import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        bitcoin_price_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        return bitcoin_price_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    bitcoin_price_usd = get_bitcoin_price()
    if bitcoin_price_usd is None:
        return

    total_cost_usd = n * bitcoin_price_usd
    print(f"El costo actual de {n} bitcoins es: ${total_cost_usd:,.4f}")

if __name__ == "__main__":
    main()