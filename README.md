# TD Ameritrade Trade History

Looks at TD Ameritrade trade history CSV and extracts the Account Trade History and stores the positions in a
dictionary with Symbol as the key and all the relevant orders, commission, p/l, and total p/l as the value

Writes the orders to a text file.

As of now, only works with the TD Ameritrade downloaded Account Statement csv

To run (python 3): ```$ python trade_history.py [CSV name]```