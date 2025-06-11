import requests

def get_card_price(card_name):
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    data = response.json()
    price = data.get("prices", {}).get("usd")

    if price is None:
        return(f"No USD price found for '{card_name}'.")
    else:
        return(f"The USD price of '{data['name']}' is ${price}")
