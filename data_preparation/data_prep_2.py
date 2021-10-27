import pandas as pd
import pickle
import random
import datetime

random.seed(39)

print(f"Opening stocks data post 2001 dictionary... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
with open('all_stocks_data_post_2001.pkl', 'rb') as file:
    all_stocks_data = pickle.load(file)

###############################################################################

def test():
    '''
    Function picks 5 random stocks and checks if the aggregation
    is happening as desired. 
    '''
    print("Running the test function ...")
    print(f"Testing begins...{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    num_list = random.choices(range(1, len(all_stocks_data.keys())), k=5)
    for i in num_list:
        check_stock = list(all_stocks_data.keys())[i]
        print(f"\nFor Stock code {check_stock}")
        # Accessing the data frame of check_code
        df = all_stocks_data[check_stock]
        df.reset_index(inplace=True)
        # Creating a new week day column where 0 is Monday and 6 is Sunday
        df['Week-day'] = df.Date.apply(lambda x: x.weekday())
        # Setting the index to Date
        df.set_index('Date', inplace=True)
        print("Original ")
        # Printing only the first 7 entries which would serve the purpose
        print(df.head(7))
        print("\nGrouped:")
        print(aggregate_week(check_stock).head(3))
    print(f"Testing done... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
###############################################################################

def aggregate_week(stock_code):
    '''
    Function to consolidate the stock data by week where a week starts
    on Monday and ends on Friday.
    '''
    df = all_stocks_data[stock_code]
    
    # Grouping by week and aggregating the remaining columns.
    df_grouped = df.groupby([pd.Grouper(freq='W')]).aggregate({'Open': 'first', 'High': 'max',
                                                               'Low': 'min', 'Close': 'last',
                                                               'Volume': 'sum',})
    df_grouped.reset_index(inplace=True)
    
    # By default the week ends on Sunday. Changing it to Friday as markets are closed on weekends
    df_grouped['Date'] = df_grouped.Date.apply(lambda x: x-datetime.timedelta(days=2))
    df_grouped.set_index('Date', inplace=True)
    return df_grouped
        
print("Consolidation on week begins...")
# Dictionary to store the new consolidated stock data    
count = 0
stocks_data_agg_week = dict()
for stock_code in all_stocks_data.keys():
    df = aggregate_week(stock_code)
    stocks_data_agg_week[stock_code] = df
    count += 1
    
    if count==len(all_stocks_data.keys())//4:
        print("\t25% consolidation complete..")
    elif count==len(all_stocks_data.keys())//2:
        print("\t50% consolidation complete..")
    elif count==count==(len(all_stocks_data.keys())*3)//4:
        print("\t75% consolidation complete..")
print("Consolidation on week complete...")    

print("Dumping begins...")
with open('all_stocks_data_post_2001_week.pkl', 'wb') as file:
    pickle.dump(stocks_data_agg_week, file)
  
print(f"Dumping Completed... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
###############################################################################       

# Opening stocks data post 2001 dictionary... 2021-10-27 12:54:42
# Consolidation on week begins...
# 	25% consolidation complete..
# 	50% consolidation complete..
# 	75% consolidation complete..
# Consolidation on week complete...
# Dumping begins...
# Dumping Completed... 2021-10-27 12:55:26

###############################################################################


# Running the test function ...
# Testing begins...2021-10-27 13:00:39

# For Stock code GENESYS.NS
# Original 
#                  Open       High        Low      Close  Volume  Week-day
# Date                                                                    
# 2003-01-23  30.893621  30.893621  27.259077  27.872406   13926         3
# 2003-01-24  29.076348  31.665959  26.236861  27.031918    8670         4
# 2003-01-27  29.076351  29.076351  24.192432  24.192432    1688         0
# 2003-01-28  26.259573  28.440298  26.259573  27.327221   55422         1
# 2003-01-29  28.394874  28.394874  26.395874  26.645750    7712         2
# 2003-01-30  27.259077  29.303508  27.259077  27.690680   18930         3
# 2003-01-31  27.259078  27.486237  26.123283  26.804760    1934         4

# Grouped:
#                  Open       High        Low      Close  Volume
# Date                                                          
# 2003-01-24  30.893621  31.665959  26.236861  27.031918   22596
# 2003-01-31  29.076351  29.303508  24.192432  26.804760   85686
# 2003-02-07  27.463518  28.826471  26.123277  26.759323   24656

# For Stock code TATAMTRDVR.NS
# Original 
#                  Open       High        Low      Close  Volume  Week-day
# Date                                                                    
# 2008-11-05  26.303506  47.092467  26.303506  41.682961   35770         2
# 2008-11-06  36.763635  41.989324  36.763635  38.391739     220         3
# 2008-11-07  40.089870  45.814495  31.520441  42.190651    1250         4
# 2008-11-10  48.142858  50.068573  36.851168  41.735481    2505         0
# 2008-11-11  46.742339  49.018182  39.485897  45.271793     450         1
# 2008-11-12  38.514283  48.843113  38.514283  48.738075     365         2
# 2008-11-14  48.738075  48.738075  48.738075  48.738075       0         4

# Grouped:
#                  Open       High        Low      Close  Volume
# Date                                                          
# 2008-11-07  26.303506  47.092467  26.303506  42.190651   37240
# 2008-11-14  48.142858  50.068573  36.851168  48.738075    3320
# 2008-11-21  47.092462  47.250021  26.959995  27.581476     835

# For Stock code ARVIND.NS
# Original 
#                 Open      High       Low     Close   Volume  Week-day
# Date                                                                 
# 2002-07-01  6.396942  6.677509  6.396942  6.453055  2280142         0
# 2002-07-02  6.677510  6.677510  6.340829  6.368886  2079430         1
# 2002-07-03  6.396943  6.565284  6.284716  6.396943  1539559         2
# 2002-07-04  6.705567  6.873907  6.340829  6.635426  5315564         3
# 2002-07-05  6.859878  7.000162  6.621397  6.930020  3911576         4
# 2002-07-08  7.042248  7.463100  7.028220  7.252674  6725053         0
# 2002-07-09  7.294759  7.645468  7.266702  7.392958  4342373         1

# Grouped:
#                 Open      High       Low     Close    Volume
# Date                                                        
# 2002-07-05  6.396942  7.000162  6.284716  6.930020  15126271
# 2002-07-12  7.042248  7.645468  6.901964  7.182531  18503755
# 2002-07-19  7.224617  7.547270  6.803766  6.986135  11710575

# For Stock code AARVI.NS
# Original 
#                  Open       High        Low      Close  Volume  Week-day
# Date                                                                    
# 2017-10-06  50.738618  51.933549  50.233071  51.565876  200000         4
# 2017-10-09  52.255258  52.255258  51.106286  51.795670  160000         0
# 2017-10-10  52.163343  56.805191  51.933549  55.748138  188000         1
# 2017-10-11  56.759230  61.584914  56.759230  59.195053  122000         2
# 2017-10-12  60.665739  63.974778  60.298067  63.469234   90000         3
# 2017-10-13  64.204577  67.559578  63.055604  67.145950  112000         4
# 2017-10-16  69.397930  80.565942  69.397930  79.968475  158000         0

# Grouped:
#                  Open       High        Low      Close  Volume
# Date                                                          
# 2017-10-06  50.738618  51.933549  50.233071  51.565876  200000
# 2017-10-13  52.255258  67.559578  51.106286  67.145950  672000
# 2017-10-20  69.397930  80.565942  69.030266  69.030266  312000

# For Stock code IRCON.NS
# Original 
#                  Open       High        Low      Close    Volume  Week-day
# Date                                                                      
# 2018-09-28  31.953702  36.064251  31.728785  32.209641  56754790         4
# 2018-10-01  32.426804  33.725892  31.534891  33.117065   6246240         0
# 2018-10-03  33.454440  33.958565  32.461704  32.682743   2797650         2
# 2018-10-04  32.496600  32.496600  31.333237  31.573664   2323640         3
# 2018-10-05  31.565913  31.728783  30.115588  31.007498   3735300         4
# 2018-10-08  30.867892  31.023008  29.471857  29.630852   1343180         0
# 2018-10-09  29.665754  29.956595  27.532922  28.203796   2516940         1

# Grouped:
#                  Open       High        Low      Close    Volume
# Date                                                            
# 2018-09-28  31.953702  36.064251  31.728785  32.209641  56754790
# 2018-10-05  32.426804  33.958565  30.115588  31.007498  15102830
# 2018-10-12  30.867892  31.023008  27.149015  28.541170  15194500
# Testing done... 2021-10-27 13:00:39