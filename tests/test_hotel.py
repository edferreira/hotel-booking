import unittest
from src.hotel import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculate_price(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['15Mar2009(sun)', '16Mar2009(mon)', '17Mar2009(tues)', '18Mar2009(wed)']
        )
        hotel = Hotel(

        )
        # self.assertEqual(hotel_chain.hotels[0].name, 'Lakewood')
        # self.assertEqual(hotel_chain.hotels[1].name, 'Bridgewood')
        # self.assertEqual(hotel_chain.hotels[1].name, 'Ridgewood')

if __name__ == '__main__':
    unittest.main()
