import datetime as date
import pandas_datareader.data as web

date_time = lambda m, d, y: date.datetime(y, m, d)
get_data = lambda symbol, start, end: web.DataReader(symbol,
                                                     "google",
                                                     start,
                                                     end)

data = get_data("VRX", date_time(1, 1, 2016), date_time(12, 31, 2016))
# print(data)


first_jan_2016 = lambda: date.datetime(2016, 1, 1)
print(first_jan_2016)
print(first_jan_2016())

# The lambda expression above creates an immutable date object.
# To get the date value you need to say first_jan_2016()
# any attempt to modify that object needs to be done like first_jan_2016() = whateever,
# which will fail, saying you can't assign to a function call.
# Thus wrapping an object in a lambda call creates an immutable object.

# This will fail.
first_jan_2016() = date.date(2016, 2, 2)
