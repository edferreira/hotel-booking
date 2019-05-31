import json
from pprint import pprint
from src.hotel import Hotel

class HotelChain:
    def __init__(self, hotels=[]):
        self._hotels = hotels

    def __str__(self):
        return str(self._hotels)
        
    @classmethod
    def load_from_file(cls, hotels_config_file = 'hotels.json'):
        """Instance a hotel chain from a configuration file path
        """
        hotels = []
        with open(hotels_config_file) as f:
            hotels_config = json.load(f)
            for hotel in hotels_config:
                hotels.append(
                    Hotel(**hotel)
                )
        
        hotel_chain = cls()
        hotel_chain._hotels = hotels
        return hotel_chain

    def find_best_offer(self, customer_request):
        cheapest_offer = None
        for hotel in self._hotels:
            cheapest_offer = self.get_lowest_offer(
                cheapest_offer, 
                hotel.get_offer(customer_request)
            )

        if cheapest_offer: 
            print (cheapest_offer)
            print (cheapest_offer["price"])
            print (cheapest_offer["hotel"])
            return cheapest_offer['hotel'].name
        return None

    @staticmethod
    def get_lowest_offer(current_cheapest_offer, contender_offer):
        """Compares two offers prices, based on price first 
        and hotel raiting second"""
        if(not current_cheapest_offer): return contender_offer

    @staticmethod
    def create_offer(hotel, customer_request):
        return {
            'hotel': hotel, 
            'price': hotel.calculate_price(customer_request)
        }
    