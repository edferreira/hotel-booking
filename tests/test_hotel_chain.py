import unittest
from src.hotel_chain import HotelChain

class TestHotelChain(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_from_file(self):
        hotel_chain = HotelChain.load_from_file()
        # self.assertEqual(hotel_chain.hotels[0].name, 'Lakewood')
        # self.assertEqual(hotel_chain.hotels[1].name, 'Bridgewood')
        # self.assertEqual(hotel_chain.hotels[1].name, 'Ridgewood')

if __name__ == '__main__':
    unittest.main()
