import pickle
import pandas as pd
import datetime

print(f"Opening stocks dictionary... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
with open('all_stocks_max_period.pickle', 'rb') as stock_file:
    all_stocks_data = pickle.load(stock_file)

# Computing the minimum dates of all stocks    
stock_codes = all_stocks_data.keys()
min_date_all_stocks = dict() 
for stock_code in stock_codes:
    min_date_all_stocks[stock_code] = all_stocks_data[stock_code].index.min()

# Cretaing a dataframe of stock codes and their minimum dates    
min_time_stamps = pd.to_datetime(pd.Series(min_date_all_stocks.values()))
df_min_dates = pd.concat([pd.Series(stock_codes), min_time_stamps], axis=1)
df_min_dates.columns = ['Stock Code', 'Min Date']
df_min_dates.sort_values(ascending=True, by='Min Date', inplace=True)

# Filtering stocks only for dates post 01-01-2001 
all_stocks_data_post_2001 = dict()
for stock_code in all_stocks_data.keys():
    df = all_stocks_data[stock_code]
    df.drop(columns=['Stock Splits', 'Dividends'], inplace=True)
    df = df[df.index>datetime.datetime(2001, 1, 1)]
    # Removing columns with no data
    all_stocks_data_post_2001[stock_code] = df

# Checking the updated dates for the 20 oldest stocks
count = 1
for stock, date in zip(df_min_dates['Stock Code'], df_min_dates['Min Date']):
    print(f"For stock: {stock}")
    print(f"\tOld date: {date}", end=" ")
    print(f"\tNew date: {all_stocks_data_post_2001[stock].index.min()}\n")
    if count==20:
        break
    count += 1
    
# Creating a pickle file for the updated dictionary
print("Dumping the filtered data to a pickle file...")
with open('all_stocks_data_post_2001.pkl', 'wb') as file:
    pickle.dump(all_stocks_data_post_2001, file)

print(f"Dumping Completed... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


###############################################################################


# Opening stocks dictionary... 2021-10-27 10:52:34
# For stock: TATAMOTORS.NS
# 	Old date: 1995-12-25 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: MFSL.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: ANDHRAPAP.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: RELINFRA.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: RIIL.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: GHCL.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: SAIL.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: SBIN.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: FEDERALBNK.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: ESCORTS.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: EIHOTEL.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: EICHERMOT.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: DRREDDY.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: DEEPAKFERT.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: SUNPHARMA.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: CIPLA.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: CENTURYTEX.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: TATACHEM.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: TATACONSUM.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# For stock: TATAINVEST.NS
# 	Old date: 1996-01-01 00:00:00 	New date: 2001-01-02 00:00:00

# Dumping the filtered data to a pickle file...
# Dumping Completed... 2021-10-27 10:53:02