from data.Yahoo.YahooQuoteReader import YahooQuoteReader

if __name__ == '__main__':
    a = YahooQuoteReader('AAPL')

    data = a.read()