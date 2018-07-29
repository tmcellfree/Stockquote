# Get Stock Price Data

### This script will collect instant (delayed 15 mins) stock price information from Yahoo Finanicals and print it at the command line. 

### To Use 

`git clone https://github.com/tmcellfree/Stockquote.git`

`pip install YahooFinancials`

This is a great tool developed by Connor Sanders @JECSand REPO `https://github.com/JECSand/yahoofinancials` 

To run type:

`cd stockquote`

`python fast_quote.py`

This will list the stock inforation of a mix of different stocks from all over the world.

The output looks like:

`Todays Date`

`Time in 24hr Format`

`Woodford Patient WPCT.L ^^^ UP 0.13 ^^^ GBp 79.2`

`City of London CTY.L *** DOWN 0.47 *** GBp 431`


### Personalise your stocks

Next setup your personal list of holdings or stocks you want information on:

`nano holdings.txt` 

There are a number of stocks already listed.

Format should be `stock name, ticker symbol *` with each stock occupying one line of the file.

For Example:

`Deutsche Bank,DBK.DE*`

` Woodford Patient Capital,WPCT.L*`

` Tesla,TSLA*`

If you are not familiar with Ticker symbols all you have to know if that every stock has a symbol that refers to it. Non-US based stocks also need to have their exchange (the trading venue e.g., `.L` is for the London Stock Exchange, London and `.DE` is for Deutsche Borse, Frankfurt) specified. So a US stock that trades on the New York Stock Exchange (NYSE), for instance Tesla, has a stock ticker `TSLA`. A stock that trades on the London Stock Exchange (LSE), like Barclays, has a ticker symbol `BARC.L`. I find this pretty cool since companies can pick their own stock tickers when the first list on a stock exchange. On of the coolest tickers (in my opinion) is from AT&T (listed on the NYSE), it is simply `T`! 

Please contribute!
   
