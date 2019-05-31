from src.hotel_chain import  HotelChain
from src.customer_request import CustomerRequest

hotel_chain = HotelChain.load_from_file()

customer_request = CustomerRequest(
    'Regular', 
    ['15Mar2009(sun)', '16Mar2009(mon)', '17Mar2009(tues)', '18Mar2009(wed)']
)

hotel_chain.find_best_offer(customer_request)