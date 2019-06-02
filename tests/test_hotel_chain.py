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

    def test_get_lowest_offer_empty_current_offer(self):
        customer_request = CustomerRequest(
            'Regular', 
            []
        )

        self.assertEqual(
            HotelChain.get_lowest_offer(
                None, 
                self.hotel_a.get_offer(customer_request)
            ), 
            self.hotel_a.get_offer(customer_request)
        )

    def test_get_lowest_offer_empty_contender_offer(self):
        customer_request = CustomerRequest(
            'Regular', 
            []
        )

        self.assertEqual(
            HotelChain.get_lowest_offer(
                self.hotel_a.get_offer(customer_request),
                None
            ),
            self.hotel_a.get_offer(customer_request)
        )

    def test_get_lowest_offer_contender_offer_lower_price(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['16Mar2009(mon)']
        )

        self.assertEqual(
            HotelChain.get_lowest_offer(
                self.hotel_b.get_offer(customer_request),
                self.hotel_a.get_offer(customer_request),
            ),
            self.hotel_a.get_offer(customer_request)
        )

    def test_get_lowest_offer_current_offer_lower_price(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['16Mar2009(mon)']
        )

        self.assertEqual(
            HotelChain.get_lowest_offer(
                self.hotel_a.get_offer(customer_request),
                self.hotel_b.get_offer(customer_request),
            ),
            self.hotel_a.get_offer(customer_request)
        )

    def test_get_lowest_offer_same_price_contender_higher_ranking(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['15Mar2009(sun)', '16Mar2009(mon)']
        )
        self.assertEqual(
            HotelChain.get_lowest_offer(
                self.hotel_a.get_offer(customer_request),
                self.hotel_b.get_offer(customer_request),
            ),
            self.hotel_b.get_offer(customer_request)
        )

    def test_get_lowest_offer_same_price_contender_lower_ranking(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['15Mar2009(sun)', '16Mar2009(mon)']
        )
        self.assertEqual(
            HotelChain.get_lowest_offer(
                self.hotel_b.get_offer(customer_request),
                self.hotel_a.get_offer(customer_request),
            ),
            self.hotel_b.get_offer(customer_request)
        )

    # testing find best offer
    def test_find_best_offer_empty_dates(self):
        customer_request = CustomerRequest(
            'Regular', 
            []
        )

        self.assertEqual(
            self.hotel_chain.find_best_offer(customer_request), 
            self.hotel_c.name
        )

    def test_find_best_offer_testcase_1(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['16Mar2009(mon)', 
            '17Mar2009(tues)', 
            '18Mar2009(wed)']
        )
        self.assertEqual(
            self.hotel_chain.find_best_offer(customer_request), 
            self.hotel_a.name
        )

    def test_find_best_offer_testcase_2(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['20Mar2009(fri)', 
            '21Mar2009(sat)', 
            '22Mar2009(sun)']
        )
        self.assertEqual(
            self.hotel_chain.find_best_offer(customer_request), 
            self.hotel_b.name
        )

    def test_find_best_offer_testcase_3(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['26Mar2009(thur)', 
            '27Mar2009(fri)', 
            '28Mar2009(sat)']
        )

        self.assertEqual(
            self.hotel_chain.find_best_offer(customer_request), 
            self.hotel_c.name
        )

if __name__ == '__main__':
    unittest.main()
