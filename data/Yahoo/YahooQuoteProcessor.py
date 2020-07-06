from data.base.BaseProcessor import BaseProcessor
from data.Yahoo.YahooQuoteReader import YahooQuoteReader
from data.Yahoo.YahooQuote import YahooQuote

import pandas as pd


class YahooQuoteProcessor(BaseProcessor):

    def __init__(self, symbol: str, response: object, reader: YahooQuoteReader,
                 include_events: bool = False, include_prepost: bool = False):

        self._include_prepost = reader.include_prepost
        self._include_events = reader.include_events

        super().__init__(symbol, response, reader)

    def process(self):
        response_json = self.response.json()
        yahoo_quote = YahooQuote(self.symbol)

        quote_dict = self.parse_response(response_json)

        quote_df = self.parse_quote(quote_dict)
        yahoo_quote.quote_df = quote_df

        if self._include_events:
            dividends_df = self.parse_dividends(quote_dict)
            yahoo_quote.dividends_df = dividends_df

            splits_df = self.parse_splits(quote_dict)
            yahoo_quote.splits_df = splits_df

        return yahoo_quote

    def parse_response(self, response_json):
        quote_dict = response_json['chart']['result'][0]
        return quote_dict

    def parse_quote(self, quote_dict):
        quotes = quote_dict['indicators']['quote'][0]
        dates = quote_dict['timestamp']
        adj_close = quote_dict['indicators']['adjclose'][0]

        # Combine the two dictionaries.
        quote_dictionary = {**quotes, **adj_close}

        # Turn the dictionary into a dataframe.
        quote_df = pd.DataFrame.from_dict(quote_dictionary)

        # Get the timestamp (datetime) for each quote entry in the data and parse it.
        quote_df['date'] = dates

        quote_df = quote_df.reindex(columns=['date', 'open', 'high', 'low',
                                             'close', 'adjclose', 'volume'])

        return quote_df

    def parse_dividends(self, quote_dict):
        # Get the splits dictionary from the JSON API output.
        dividends_dict = quote_dict['chart']['result'][0]['events']['dividends']

        # Convert the splits dictionary to a Dataframe.
        dividends_df = pd.DataFrame.from_dict(dividends_dict, orient='index')
        dividends_df.index = pd.Index(range(0, dividends_df.shape[0]))

        return dividends_df

    def parse_splits(self, quote_dict):
        # Get the splits dictionary from the JSON API output.
        splits_dict = quote_dict['chart']['result'][0]['events']['splits']

        splits_df = pd.DataFrame.from_dict(splits_dict, orient='index')
        splits_df.index = pd.Index(range(0, splits_df.shape[0]))

        return splits_df
