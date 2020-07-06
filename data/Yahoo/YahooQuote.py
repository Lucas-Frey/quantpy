import pandas as pd


class YahooQuote:

    def __init__(self, symbol: str):
        self._symbol = symbol

        self.quote_df = pd.DataFrame(columns=['date', 'open', 'high', 'low',
                                              'close', 'adjclose', 'volume'])
        self.dividends_df = pd.DataFrame()
        self.splits_df = pd.DataFrame()
