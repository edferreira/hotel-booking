import json
from pprint import pprint
from src.hotel import Hotel

class HotelChain:
    def __init__(self, hotels=[]):
        self.hotels = hotels
        
    @classmethod
    def load_from_file(cls, hotels_config_file = 'hotels.json'):
        hotels = cls()
        with open(hotels_config_file) as f:
            hotels_config = json.load(f)
            for hotel in hotels_config:
                print(hotel)
                hotels.add_hotel(
                    Hotel(**hotel)
                )
        return 

    def add_hotel(self, hotel):
        print(hotel)
        self.hotels.append(hotel)
