import unittest
from src.customer_request import CustomerRequest

class TestCustomerRequest(unittest.TestCase):
    def setUp(self):
        pass

    def test_set_weekdays(self):
        customer_request = CustomerRequest(
            'Regular', 
            ['15Mar2009(sun)', '16Mar2009(mon)', '17Mar2009(tues)', '18Mar2009(wed)']
        )
        self.assertEqual(customer_request.weekdays_count, 3)
        self.assertEqual(customer_request.weekends_count, 1)

if __name__ == '__main__':
    unittest.main()
