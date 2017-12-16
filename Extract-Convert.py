import pytrends
import csv
from pytrends.request import TrendReq
#gmail username and password not necessary
gmail_username = ""
gmail_password = ""
pytrend = TrendReq(gmail_username, gmail_password, custom_useragent=None)
#topic name specified with kw_list & timeframe specifies the time duartion to be considered
pytrend.build_payload(kw_list=['pizza'], timeframe = 'today 12-m')
interest_over_time_df = pytrend.interest_over_time()
#name of the csv file to be stored is "topic.csv"
interest_over_time_df.to_csv("topic.csv", encoding='utf-8')
