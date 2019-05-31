class HotelPrices:
    def __init__(self, prices):
        self.prices = prices

class Hotel:
    def __init__(self, name, rating, prices):
        self.name = name
        self.rating = rating
        self.prices = self.load_hotel_prices(prices)

    def __str__(self):
        return "%s %s %s"% (self.name, self.rating, self.prices)
        
    def __repr__(self):
        return "%s %s %s"% (self.name, self.rating, self.prices)

    @staticmethod
    def load_hotel_prices(prices):
        formated_prices = {
            'Regular': {
                'weekend': prices['weekend']['Regular'],
                'weekday': prices['weekday']['Regular']
            },
            'Reward': {
                'weekend': prices['weekend']['Reward'],
                'weekday': prices['weekday']['Reward']
            }
        }
        return formated_prices

    def calculate_price(self, customer_request):
        user_type_prices = self.prices[customer_request.customer_type]

        weekday_price = self.weekday_price(customer_request.weekdays_count, user_type_prices)
        weekend_price = self.weekend_price(customer_request.weekends_count, user_type_prices)
        return weekday_price + weekend_price

    @classmethod
    def weekday_price(cls, days_count, prices):
        return days_count * prices['weekday']

    @classmethod
    def weekend_price(cls, days_count, prices):
        return days_count * prices['weekend']