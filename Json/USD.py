import requests

API_KEY = "ce3690063bb65266551b3f57f40e5543"

base_currency = "USD"
target_currency = "INR"

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

try:
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        if data["result"] == "success":

            rate = data["conversion_rates"][target_currency]

            print("Currency:", base_currency)
            print("Target:", target_currency)
            print("1", base_currency, "=", rate, target_currency)

        else:
            print("API Error:", data)

    else:
        print("HTTP Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Connection Error:", e)