import unittest
from src.hotel import Hotel
from src.customer_request import CustomerRequest

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.weekday_regular_price = 110
        self.weekday_reward_price = 80
        self.weekend_regular_price = 90
        self.weekend_reward_price = 80
        self.hotel = Hotel(
            "Lakewood",
            3, 
            {
                "weekday": {
                    "Regular": self.weekday_regular_price, 
                    "Reward": self.weekday_reward_price} ,
                "weekend": {
                    "Regular": self.weekend_regular_price, 
                    "Reward": self.weekend_reward_price} 
            }
        )
        pass

    def test_calculate_regular_empty(self):
        customer_request = CustomerRequest(
            'Regular', 
            []
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            0
        )

    def test_calculate_regular_1_weekday(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['16Mar2009(mon)']
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekday_regular_price
        )

    def test_calculate_regular_5_weekday(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['16Mar2009(mon)', '17Mar2009(tues)',
            '18Mar2009(wes)', '19Mar2009(thur)',
            '20Mar2009(fri)', ]
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekday_regular_price * 5
        )

    def test_calculate_reward_1_weekday(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['16Mar2009(mon)']
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekday_reward_price
        )

    def test_calculate_reward_5_weekday(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['16Mar2009(mon)', '17Mar2009(tues)',
            '18Mar2009(wes)', '19Mar2009(thur)',
            '20Mar2009(fri)', ]
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekday_reward_price * 5
        )

    def test_calculate_regular_1_weekend(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['15Mar2009(sun)']
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekend_regular_price
        )

    def test_calculate_regular_2_weekend(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['14Mar2009(sat)', '15Mar2009(sun)' ]
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekend_regular_price * 2
        )

    def test_calculate_reward_1_weekend(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['14Mar2009(sat)']
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekend_reward_price
        )

    def test_calculate_reward_2_weekend(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['14Mar2009(sat)', '15Mar2009(sun)' ]
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekend_reward_price * 2
        )

    def test_calculate_regular_2_weekday_2_weekend(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['14Mar2009(sat)', '15Mar2009(sun)',
            '16Mar2009(mon)', '17Mar2009(tues)',]
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekend_regular_price * 2 + self.weekday_regular_price * 2
        )

    def test_calculate_reward_2_weekday_2_weekend(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['14Mar2009(sat)', '15Mar2009(sun)',
            '16Mar2009(mon)', '17Mar2009(tues)',]
        )
        self.assertEqual(
            self.hotel.calculate_price(customer_request),
            self.weekend_reward_price * 2 + self.weekday_reward_price * 2
        )

    def test_get_offer(self):
        customer_request = CustomerRequest(
            'Reward', 
            ['14Mar2009(sat)', '15Mar2009(sun)',
            '16Mar2009(mon)', '17Mar2009(tues)']
        )

        self.assertDictEqual(
            self.hotel.get_offer(customer_request), 
            {
                'hotel': self.hotel, 
                'price': self.weekend_reward_price * 2 + self.weekday_reward_price * 2
            }
        )


if __name__ == '__main__':
    unittest.main()
