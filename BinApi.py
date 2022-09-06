import requests
import operator
from collections import OrderedDict

url = 'https://api.binance.com/api/v3/ticker/24hr'

r = requests.get(url)
data = r.json()
print(data)
l = []
w = []

for crypto in data:
    sym = crypto['symbol']
    perc = format(float(crypto['priceChangePercent']), '.2f')
    if (str(sym).find("UP") != -1) or (str(sym).find("DOWN") != -1):
        continue
    elif str(sym).find("USDT") != -1:
        if float(perc) >= 10:
            i = f"{sym}:  {perc}"+" %"
            l.append(i)
            l.append('\n')
        elif float(perc) <= -10:
            m = f"{sym}:  {perc}" + " %"
            w.append(m)
            w.append('\n')

topplus = l
topplus = ' '.join(topplus)

topminus = w
topminus = ' '.join(topminus)



