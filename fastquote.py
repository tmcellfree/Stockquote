# README
# To use this file unmodified:
# 1 add a .txt file to your directory listing your holdings (call it holdings.txt).
# 2 format should be "stock name, ticker symbol *" with each holding occupying one line of the file.
# Example: 
# Deutsche Bank, DBK.DE *
# Woodford Patient Capital, WPCT.L *
# Tesla, TSLA *

# SEE Repo https://github.com/JECSand/yahoofinancials

from yahoofinancials import YahooFinancials
import pandas as pd
import time
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))
## 12 hour format ##
print (time.strftime("%I:%M:%S"))
holdings = open("holdings.txt") #create a file called "holdings" and add your stock list to it

for line in holdings:
    Name_of_stock = line.split(',')[0]
    Ticker_symbol = line.split(',')[1].split('*')[0]
    #print (Name_of_stock,Ticker_symbol)
    stockInfo=YahooFinancials(Ticker_symbol) #import the stock details from yahoo finance
    stockpricechange = format(100*float(stockInfo.get_current_change())/(float(stockInfo.get_current_price())-float(stockInfo.get_current_change())), '.2f')
    #For ease of viewing this allows you to see if the stock has risen or fallen
    if float(stockpricechange) > 0.00:
        print Name_of_stock, Ticker_symbol,"^^^" , "UP", stockpricechange, "^^^", stockInfo.get_currency() ,stockInfo.get_current_price();
    elif float(stockpricechange) <= 0.00:
        print Name_of_stock, Ticker_symbol,"***" , "DOWN", stockpricechange, "***", stockInfo.get_currency() , stockInfo.get_current_price();
    # Written by Tom Meany please add suff you think is useful!
