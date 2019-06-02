from src.hotel_chain import  HotelChain
from src.customer_request import CustomerRequest
import sys

def process_input_line(line):
    client_type, dates = line.split(':')
    dates = list(map(lambda x: x.strip(), dates.split(',')))
    customer_request = CustomerRequest(client_type, dates)
    print(hotel_chain.find_best_offer(customer_request))

if len(sys.argv) < 2:
    print("usage: %s [options] <input>" % sys.argv[1])
    print("options: --file for inputing a file")
    sys.exit()

user_input = None
input_file = None

print(sys.argv)

if sys.argv[1] == "--file":
    input_file = sys.argv[2]
else:
    user_input = sys.argv[1]

hotel_chain = HotelChain.load_from_file()

'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'

if input_file:
    with open(input_file, 'r') as f:
        line = f.readline()
        while line:
            process_input_line(line)
            line = f.readline()
elif user_input:
    process_input_line(user_input)
else:
    print("invalid input")