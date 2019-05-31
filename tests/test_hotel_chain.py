import unittest
from src.hotel_chain import HotelChain
from src.hotel import Hotel
from src.customer_request import CustomerRequest

class TestHotelChain(unittest.TestCase):
    def setUp(self):
        self.hotel_a = Hotel(
            "Lakewood",
            3, 
            {
                "weekday": {
                    "Regular": 110, 
                    "Reward": 80,
                },
                "weekend": {
                    "Regular": 90, 
                    "Reward": 80
                }
            }
        )

        self.hotel_b = Hotel(
            "Bridgewood",
            4, 
            {
                "weekday": {
                    "Regular": 160, 
                    "Reward": 110,
                },
                "weekend": {
                    "Regular": 60, 
                    "Reward": 50 
                }
            }
        )
        self.hotel_c = Hotel(
            "Ridgewood",
            5, 
            {
                "weekday": {
                    "Regular": 220, 
                    "Reward": 100,
                },
                "weekend": {
                    "Regular": 150, 
                    "Reward": 40 
                }
            }
        )

        self.hotel_chain = HotelChain(
            [self.hotel_a, self.hotel_b, self.hotel_c]
        )

    def test_load_from_file(self):
        hotel_chain = HotelChain.load_from_file()
        self.assertEqual(hotel_chain.hotels[0].name, 'Lakewood')
        self.assertEqual(hotel_chain.hotels[1].name, 'Bridgewood')
        self.assertEqual(hotel_chain.hotels[2].name, 'Ridgewood')

    def test_calculate_regular_empty(self):
        customer_request = CustomerRequest(
            'Regular', 
            []
        )
        self.assertEqual(
            self.hotel_chain.find_best_offer(customer_request), 
            self.hotel_c.name
        )


if __name__ == '__main__':
    unittest.main()
