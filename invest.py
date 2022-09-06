import investpy
from aiogram.utils.markdown import hlink
import emoji
emoji.emojize(':us:')

#crypto
#crypto = investpy.crypto.get_cryptos_overview(as_json=True, n_results=10)
#sym = hlink(crypto[0]['symbol'], 'https://ru.investing.com/crypto/bitcoin/chart')
#price = crypto[0]['price']
#perc = crypto[0]['change24h']
#perc7 = crypto[0]['change7d']
#btc = f"{sym}:  <b>{price}</b>   {perc}(D1)   {perc7}(7D)"

#sym = hlink(crypto[1]['symbol'], 'https://ru.investing.com/crypto/ethereum/chart')
#price = crypto[1]['price']
#perc = crypto[1]['change24h']
#perc7 = crypto[1]['change7d']
#eth = f"{sym}:  <b>{price}</b>   {perc}(D1)   {perc7}(7D)"

#sym = hlink(crypto[5]['symbol'], 'https://ru.investing.com/crypto/terra-luna/chart')
#price = crypto[5]['price']
#perc = crypto[5]['change24h']
#perc7 = crypto[5]['change7d']
#luna = f"{sym}:  <b>{price}</b>   {perc}(D1)   {perc7}(7D)"

#sym = hlink(crypto[6]['symbol'], 'https://ru.investing.com/crypto/solana/chart')
#price = crypto[6]['price']
#perc = crypto[6]['change24h']
#perc7 = crypto[6]['change7d']
#sol = f"{sym}:  <b>{price}</b>   {perc}(D1)   {perc7}(7D)"

#металлы
metals = investpy.commodities.get_commodities_overview(group='metals', as_json=True, n_results=10)
yearm = investpy.commodities.get_commodity_information(commodity='Gold', country=None, as_json=True)
sym = hlink(metals[0]['name'], 'https://ru.investing.com/commodities/gold-streaming-chart')
price = metals[0]['last']
perc = metals[0]['change_percentage']
yearchange = yearm['1-Year Change']
gold = f"{sym}:   <b>{price}</b>   {perc}   {yearchange} (за год)"

yearn = investpy.commodities.get_commodity_information(commodity='Nickel', country=None, as_json=True)
sym = hlink(metals[8]['name'], 'https://ru.investing.com/commodities/nickel-streaming-chart?cid=959208')
price = metals[8]['last']
perc = metals[8]['change_percentage']
yearchange = yearn['1-Year Change']
nik = f"{sym}:   <b>{price}</b>   {perc}   {yearchange} (за год)"

yearpa = investpy.commodities.get_commodity_information(commodity='Palladium', country=None, as_json=True)
sym = hlink(metals[3]['name'], 'https://ru.investing.com/commodities/palladium-streaming-chart')
price = metals[3]['last']
perc = metals[3]['change_percentage']
yearchange = yearpa['1-Year Change']
pal = f"{sym}:   <b>{price}</b>   {perc}   {yearchange} (за год)"

yearpl = investpy.commodities.get_commodity_information(commodity='Platinum', country=None, as_json=True)
sym = hlink(metals[4]['name'], 'https://ru.investing.com/commodities/platinum-streaming-chart')
price = metals[4]['last']
perc = metals[4]['change_percentage']
yearchange = yearpl['1-Year Change']
pl = f"{sym}:   <b>{price}</b>   {perc}   {yearchange} (за год)"

yearcoop = investpy.commodities.get_commodity_information(commodity='Copper', country='united states', as_json=True)
sym = hlink(metals[1]['name'], 'https://ru.investing.com/commodities/copper-streaming-chart')
price = metals[1]['last']
perc = metals[1]['change_percentage']
yearchange = yearcoop['1-Year Change']
cop = f"{sym}:   <b>{price}</b>   {perc}   {yearchange} (за год)"

#энергия
br = investpy.commodities.get_commodities_overview(group='energy', as_json=True, n_results=5)
yearb = investpy.commodities.get_commodity_information(commodity='Brent Oil', country=None, as_json=True)
sym = hlink(br[0]['name'], 'https://ru.investing.com/commodities/brent-oil-streaming-chart')
price = br[0]['last']
perc = br[0]['change_percentage']
yearchange = yearb['1-Year Change']
brent = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearg = investpy.commodities.get_commodity_information(commodity='Natural Gas', country=None, as_json=True)
sym = hlink(br[3]['name'], 'https://ru.investing.com/commodities/natural-gas-streaming-chart')
price = br[3]['last']
perc = br[3]['change_percentage']
yearchange = yearg['1-Year Change']
gas = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

#russia
indr = investpy.indices.get_indices_overview(country='russia', as_json=True, n_results=10)
yearmo = investpy.indices.get_index_information(index='MOEX', country='russia', as_json=True)
sym = hlink(indr[0]['name'], 'https://ru.investing.com/indices/mcx-chart')
price = indr[0]['last']
perc = indr[0]['change_percentage']
yearchange = yearmo['1-Year Change']
moex = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearrt = investpy.indices.get_index_information(index='RTSI', country='russia', as_json=True)
sym = hlink(indr[1]['name'], 'https://ru.investing.com/indices/rtsi-chart')
price = indr[1]['last']
perc = indr[1]['change_percentage']
yearchange = yearrt['1-Year Change']
rts = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

cur = investpy.currency_crosses.get_currency_crosses_overview('RUB', as_json=True, n_results=100)

sym = hlink(cur[2]['symbol'], 'https://ru.investing.com/currencies/usd-rub-chart')
price = cur[2]['bid']
perc = cur[2]['change_percentage']
rub = f"{sym}:  <b>{price}</b>   {perc}"

sym = hlink(cur[0]['symbol'], 'https://ru.investing.com/currencies/eur-rub-chart')
price = cur[0]['bid']
perc = cur[0]['change_percentage']
eurrub = f"{sym}:  <b>{price}</b>   {perc}"

sym = hlink(cur[8]['symbol'], 'https://ru.investing.com/currencies/cny-rub-chart')
price = cur[8]['bid']
perc = cur[8]['change_percentage']
yanrub = f"{sym}:  <b>{price}</b>   {perc}"

#usa
ind = investpy.indices.get_indices_overview(country='united states', as_json=True, n_results=10)
yearins = investpy.indices.get_index_information(index='Nasdaq', country='united states', as_json=True)
sym = hlink(ind[2]['name'], 'https://ru.investing.com/indices/nasdaq-composite-chart')
price = ind[2]['last']
perc = ind[2]['change_percentage']
yearchange = yearins['1-Year Change']
nsdq = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearisp5 = investpy.indices.get_index_information(index='S&P 500', country='united states', as_json=True)
sym = hlink(ind[3]['name'], 'https://ru.investing.com/indices/us-spx-500-chart')
price = ind[3]['last']
perc = ind[3]['change_percentage']
yearchange = yearisp5['1-Year Change']
sp500 = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

#index
inde = investpy.indices.get_indices_overview(country='germany', as_json=True, n_results=2)
yearid = investpy.indices.get_index_information(index='DAX', country='germany', as_json=True)
sym = hlink(inde[0]['name'], 'https://ru.investing.com/indices/germany-30-chart')
price = inde[0]['last']
perc = inde[0]['change_percentage']
yearchange = yearid['1-Year Change']
dax = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

indf = investpy.indices.get_indices_overview(country='france', as_json=True, n_results=2)
yearif = investpy.indices.get_index_information(index='CAC 40', country='france', as_json=True)
sym = hlink(indf[0]['name'], 'https://ru.investing.com/indices/france-40-chart')
price = indf[0]['last']
perc = indf[0]['change_percentage']
yearchange = yearif['1-Year Change']
cac40 = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

indc = investpy.indices.get_indices_overview(country='china', as_json=True, n_results=5)
yearic = investpy.indices.get_index_information(index='Shanghai', country='china', as_json=True)
sym = hlink(indc[1]['name'], 'https://ru.investing.com/indices/shanghai-composite-chart')
price = indc[1]['last']
perc = indc[1]['change_percentage']
yearchange = yearic['1-Year Change']
china = f"{sym}:  <b>{price}</b>  {perc}   {yearchange} (за год)"

indj = investpy.indices.get_indices_overview(country='japan', as_json=True, n_results=5)
yearij = investpy.indices.get_index_information(index='Nikkei 225', country='japan', as_json=True)
sym = hlink(indj[0]['name'], 'https://ru.investing.com/indices/japan-ni225-chart')
price = indj[0]['last']
yearchange = yearij['1-Year Change']
perc = indj[0]['change_percentage']
japan = f"{sym}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

#товары
prod = investpy.commodities.get_commodities_overview(group='grains', as_json=True, n_results=10)
years = investpy.commodities.get_commodity_information(commodity='US Soybeans', country=None, as_json=True)
price = prod[4]['last']
perc = prod[4]['change_percentage']
yearchange = years['1-Year Change']
soybeansusa = f"{hlink('Соевые бобы', 'https://ru.investing.com/commodities/us-soybeans-streaming-chart')}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearw = investpy.commodities.get_commodity_information(commodity='US Wheat', country=None, as_json=True)
price = prod[5]['last']
perc = prod[5]['change_percentage']
yearchange = yearw['1-Year Change']
pshenousa = f"{hlink('Пшеница', 'https://ru.investing.com/commodities/us-wheat-streaming-chart')}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearc = investpy.commodities.get_commodity_information(commodity='US Corn', country=None, as_json=True)
price = prod[6]['last']
perc = prod[6]['change_percentage']
yearchange = yearc['1-Year Change']
cornusa = f"{hlink('Кукуруза', 'https://ru.investing.com/commodities/us-corn-streaming-chart')}: <b>{price}</b>   {perc}   {yearchange} (за год)"

yearlw = investpy.commodities.get_commodity_information(commodity='London Wheat', country=None, as_json=True)
price = prod[0]['last']
perc = prod[0]['change_percentage']
yearchange = yearlw['1-Year Change']
pshenolon = f"{hlink('Пшеница', 'https://ru.investing.com/commodities/london-wheat-streaming-chart')}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearr = investpy.commodities.get_commodity_information(commodity='Rough Rice', country=None, as_json=True)
price = prod[1]['last']
perc = prod[1]['change_percentage']
yearchange = yearr['1-Year Change']
risusa = f"{hlink('Грубый рис', 'https://ru.investing.com/commodities/rough-rice-streaming-chart')}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

lum = investpy.commodities.get_commodities_overview(group='softs', as_json=True, n_results=10)
yearlm = investpy.commodities.get_commodity_information(commodity='Lumber', country=None, as_json=True)
price = lum[8]['last']
perc = lum[8]['change_percentage']
yearchange = yearlm['1-Year Change']
lumber = f"{hlink('Lumber', 'https://ru.investing.com/commodities/lumber-streaming-chart')}  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearls = investpy.commodities.get_commodity_information(commodity='London Sugar', country=None, as_json=True)
price = lum[7]['last']
perc = lum[7]['change_percentage']
yearchange = yearls['1-Year Change']
sugar = f"{hlink('Сахар', 'https://ru.investing.com/commodities/london-sugar-streaming-chart')}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

yearoj = investpy.commodities.get_commodity_information(commodity='Orange Juice', country=None, as_json=True)
price = lum[3]['last']
perc = lum[3]['change_percentage']
yearchange = yearoj['1-Year Change']
orange = f"{hlink('Апельсиновый сок', 'https://ru.investing.com/commodities/orange-juice-streaming-chart')}:  <b>{price}</b>   {perc}   {yearchange} (за год)"

index = ['🚀<b>Рубль:</b>', rub, eurrub, yanrub, ' ',
         '🔥<b>Энергоресурсы:</b>', brent, gas, ' ',
         '🔩<b>Металлы:</b>', gold, nik, pal, pl, cop, ' ',
         '🌳<b>Древесина:</b>', lumber, ' ',
         '🌻<b>C/x продукция, США:</b>', soybeansusa, pshenousa, cornusa, risusa, orange, ' ',
         '🌻<b>C/x продукция, Лондон:</b>', pshenolon, sugar, ' ',
         '🇷🇺<b>Россия:</b>',moex, rts, ' ',
         '🇺🇸<b>Америка:</b>', sp500, nsdq, ' ',
         '🇪🇺<b>Европа:</b>', dax, cac40, ' ',
         '🇨🇳<b>Азия:</b>', china, japan, ' '
         #'📊<b>Крипто:</b>', btc, eth, luna, sol
         ]
index = '\n'.join(index)












