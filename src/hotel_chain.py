import json
from pprint import pprint
from src.hotel import Hotel

class HotelChain:
    def __init__(self, hotels=[]):
        self.hotels = hotels

    def __str__(self):
        return str(self.hotels)
        
    @classmethod
    def load_from_file(cls, hotels_config_file = 'hotels.json'):
        hotel_chain = cls()
        with open(hotels_config_file) as f:
            hotels_config = json.load(f)
            for hotel in hotels_config:
                hotel_chain.hotels.append(
                    Hotel(**hotel)
                )
        return hotel_chain

    def find_best_offer(self, customer_request):
        best_offer = {'hotel': '', 'price': ''}
        for hotel in self.hotels:
            print(hotel.calculate_price(customer_request))
    