import unittest
from src.hotel_chain import HotelChain

class TestHotelChain(unittest.TestCase):
    def setUp(self):
        pass

    def test_loader(self):
        me = HotelChain.load_from_file()
        self.assertEqual(me, '../hotels.json')


if __name__ == '__main__':
    unittest.main()
