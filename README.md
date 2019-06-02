# hotel-booking

## usage
Python3 is required for running this application

It can be run by two ways: With a single string as argument, with the format `"<client_type>: <date_1>, <date_2> ..."` or passing a file using the `--file` argument. This file must have the same format as the string detailed above, and each entry of the file must be separated with a new line. An example of this file can be found on the inputs.txt file, presented in this repository.


```
# Example using a single costumer input
python3 app.py "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
# Example using a file, containing costumer inputs
python3 app.py --file input.txt
```

