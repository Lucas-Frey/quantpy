from data.Yahoo.YahooQuoteReader import YahooQuoteReader
from data.Yahoo.YahooQuoteProcessor import YahooQuoteProcessor

if __name__ == '__main__':
    data = YahooQuoteReader('AAPL').read()
    yahoo_quote = YahooQuoteProcessor('AAPL', data).process()