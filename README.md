# hotel-booking

## Usage
Python3 is required for running this application

It can be run in two ways: With a single string as argument, formatted as `"<client_type>: <date_1>, <date_2> ..."` or passing a file using the `--file` argument. This file must have the same format as the string detailed above, and each entry of the file must be separated with a new line. An example of this file can be found on the [inputs.txt file](input.txt), presented in this repository.

```
# Example using a single costumer input
python3 app.py "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
# Example using a file, containing costumer inputs
python3 app.py --file input.txt
```

## Testing
All the test files can be find at the tests folder. For running the test files, use the following command

```python3 -m unittest discover tests```


## Application Description

This application aims to find the cheapest hotel, with the heigher ranking, for a costumer who wants to book an hotel for a given set of dates.

## Design

Created two classes for representing the hotel chain structure (as shown bellow), which can be configured throw the [hotels.json file](hotels.json). This file will load the hotel chain instances and can be easliy configured for adding a new hotel or changing its values. For now it can only represent one hotel chain. 

```
+-----------------+         +--------+
|    HotelChain   |         | Hotel  |
|-----------------|         |--------|
| _hotels         |         | name   |
+-----------------+         | rating |
                            | prices |
                            +--------+
```
Those two models will be the representation of the hotel chain and the hotels belonging to this hotel chain. Each hotel will be responsible of processing the user request and give it's price, and the hotel chain will be responsible of getting all it's hotels price and compare each other to find out which one has the best offer for the user.

The customer request also has a class for it's one (as shown bellow). This class will store the customer type and dates, and will process the request to retrieve the numbers of weekdays and weekends, which will help us calcualte the offers lates.
```
+---------------------------+
|      CustomerRequest      |
|---------------------------|
| customer_type             |
| request_dates             |
| weekdays_count            |
| weekends_count            |
+---------------------------+
```

## Assumptions
For this exercise, it was made an assumption that every input will be a valid one. Which means that it doesn't expect the costumer to input a day that isn't a weekday, like 20Mar2009(lala). If it happens it will be counted as a weekday.


