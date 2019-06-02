import unittest
from src.customer_request import CustomerRequest

class TestCustomerRequest(unittest.TestCase):
    def setUp(self):
        pass

    def test_weekdays_null(self):
        customer_request = CustomerRequest(
            'Regular', 
            [ ]
        )
        self.assertEqual(customer_request.weekdays_count, 0)
        self.assertEqual(customer_request.weekends_count, 0)

    def test_weekdays_1_weekend(self):
        customer_request = CustomerRequest(
            'Regular', 
            [
                '14Mar2009(sat)', 
            ]
        )
        self.assertEqual(customer_request.weekdays_count, 0)
        self.assertEqual(customer_request.weekends_count, 1)

    def test_weekdays_1_weekday(self):
        customer_request = CustomerRequest(
            'Regular', 
            [
                '16Mar2009(mon)', 
            ]
        )
        self.assertEqual(customer_request.weekdays_count, 1)
        self.assertEqual(customer_request.weekends_count, 0)

    def test_set_weekdays(self):
        customer_request = CustomerRequest(
            'Regular', 
            [
                '14Mar2009(sat)', 
                '15Mar2009(sun)', 
                '16Mar2009(mon)', 
                '17Mar2009(tues)', 
                '18Mar2009(wed)'
            ]
        )
        self.assertEqual(customer_request.weekdays_count, 3)
        self.assertEqual(customer_request.weekends_count, 2)

if __name__ == '__main__':
    unittest.main()
