import yfinance as yf
from nsetools import Nse
import pickle
import datetime

nse = Nse()

# Getting the stock code of all companies listed on NSE
print(f"Getting the codes of all companies... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
all_stock_codes = nse.get_stock_codes().keys()

# Since finance API requires .NS at the end of every stock code
print("Converting the codes into Yahoo Finance compatible format...")
all_stock_codes_yf = [x+'.NS' for x in all_stock_codes]

# Dictionary to store the everyday price of all stocks
all_stock_price_daily = dict()

percentage_done = 0
print(f"Storing the historical prices of {len(all_stock_codes_yf)} stocks...")
print(f"The first item {all_stock_codes_yf[0]} is not a stock...")
print(f"Storing the historical prices of {len(all_stock_codes_yf)-1} stocks...")

for stock_code in all_stock_codes_yf[1:]:
    stock_ticker = yf.Ticker(stock_code)
    check = stock_ticker.history('max')
    if check.empty:
        print(f"Removing stock code {stock_code} with no data...")
        continue
    
    all_stock_price_daily[stock_code] = check
    
    if percentage_done==len(all_stock_codes_yf)//4:  
        print("25% done...")
    elif percentage_done==len(all_stock_codes_yf)//2:
        print("50% done...")
    elif percentage_done==(len(all_stock_codes_yf)*3)//4:
        print("75% done...")
    
    percentage_done += 1
    
print("100% done...")
print("Creating a pickle file for the dictionary...")

with open('all_stocks_max_period.pickle','wb') as file:
    pickle.dump(all_stock_price_daily, file)
    
print(f"Completed... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


###############################################################################


# Getting the codes of all companies... 2021-10-26 07:22:17
# Converting the codes into Yahoo Finance compatible format...
# Storing the historical prices of 1738 stocks...
# The first item SYMBOL.NS is not a stock...
# Storing the historical prices of 1737 stocks...
# 25% done...
# - EMAMIPAP.NS: None
# Removing stock code EMAMIPAP.NS with no data...
# - KALYANI.NS: No data found, symbol may be delisted
# Removing stock code KALYANI.NS with no data...
# 50% done...
# - MEDICAMEQ.NS: No data found, symbol may be delisted
# Removing stock code MEDICAMEQ.NS with no data...
# 75% done...
# - SELMC.NS: No data found, symbol may be delisted
# Removing stock code SELMC.NS with no data...
# 100% done...
# Creating a pickle file for the dictionary...
# Completed... 2021-10-26 07:43:16

