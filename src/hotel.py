class HotelPrices:
    def __init__(self, prices):
        self.prices = prices

class Hotel:
    def __init__(self, name, rating, prices):
        print(name, rating, prices)
        self.name = name
        self.rating = rating
        self.prices = HotelPrices(prices)

    def __str__(self):
        return "%s %s"% (self.name, self.rating)

