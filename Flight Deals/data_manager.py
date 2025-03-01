import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0b86333efa3c9ea303f08fc31e475588/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        # Save your Sheety endpoints an environment variables
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._token = os.environ["BEARER_TOKEN"]
        self.sheet_header = {
            "Authorization": f"Bearer {self._token}"
        }
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # Using the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.sheet_header)
        data = response.json()

        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=self.sheet_header,
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        self.customer_data = data["users"]
        return self.customer_data
