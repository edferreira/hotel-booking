import json
from pprint import pprint
from src.hotel import Hotel

class HotelChain:
    def __init__(self, hotels=[]):
        self.hotels = self.load_hotels(hotels)

    def __str__(self):
        return str(self.hotels)
        
    @classmethod
    def load_from_file(cls, hotels_config_file = 'hotels.json'):
        hotels = []
        with open(hotels_config_file) as f:
            hotels_config = json.load(f)
            for hotel in hotels_config:
                hotels.append(
                    Hotel(**hotel)
                )
        
        hotel_chain = cls()
        hotel_chain.hotels = hotels
        return hotel_chain

    @staticmethod
    def load_hotels(hotels):
        # we sort our hotels by rating, so it becomes 
        # easier to compare later because we will only need 
        # to get last one that has a price lower or equal 
        # to the current winning one
        hotels.sort(key=lambda hotel: hotel.rating)
        return hotels

    def find_best_offer(self, customer_request):
        best_offer = {'hotel': '', 'price': ''}
        for hotel in self.hotels:
            print(hotel.calculate_price(customer_request))
    