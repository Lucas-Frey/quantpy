from pipelines.base.BaseProcessor import BaseProcessor
from pipelines.yahoo.quote.YahooQuoteReader import YahooQuoteReader
from pipelines.yahoo.quote.YahooQuoteWriter import YahooQuote

import pandas as pd

from printers.SerialPrinter import SerialPrinter


class YahooQuoteProcessor(BaseProcessor):

    def __init__(self, symbol: str, response: object, reader: YahooQuoteReader,
                 include_events: bool = False, include_prepost: bool = False):

        self._yq = YahooQuote(symbol)
        self._serial_printer = SerialPrinter()

        super().__init__(symbol, response, reader)

    def process(self):
        response_json = self.response.json()
        yahoo_quote = YahooQuote(self.symbol)

        modules = response_json['chart']['result'][0]

        self._serial_printer.print_begin('Parsing quote objects...')
        self._yq.quote = self.parse_quote(modules)
        self._yq.dividends = self.parse_dividends(modules)
        self._yq.splits = self.parse_splits(modules)
        self._serial_printer.print_end('Complete.')

        return self._yq

    def parse_quote(self, modules):

        self._serial_printer.print_begin('Parsing quote from response...')

        if 'indicators' in modules and \
                'quote' in modules['indicators'] and \
                len(modules['indicators']['quote']) > 0 and \
                'timestamp' in modules and \
                'indicators' in modules and \
                'adjclose' in modules['indicators'] and \
                len(modules['indicators']['adjclose']) > 0:

            self._serial_printer.print_begin('Finding quote in response...')
            quotes = modules['indicators']['quote'][0]
            dates = modules['timestamp']
            adj_close = modules['indicators']['adjclose'][0]
            self._serial_printer.print_end('Complete.')

            self._serial_printer.print_begin('Creating dataframe...')
            # Combine the two dictionaries.
            dict = {**quotes, **adj_close}

            # Turn the dictionary into a dataframe.
            df = pd.DataFrame.from_dict(dict)
            self._serial_printer.print_end('Complete.')

            # Get the timestamp (datetime) for each quote entry in the pipelines and parse it.
            self._serial_printer.print_begin('Formatting columns...')
            df['date'] = dates
            df['date'] = pd.to_datetime(df['date'], unit='s')

            df['volume'] = pd.to_numeric(df['volume'])

            df = df.reindex(columns=['date', 'open', 'high', 'low',
                                     'close', 'adjclose', 'volume'])

            df = df.set_index('date').sort_index()
            self._serial_printer.print_end('Complete.')

        else:
            self._serial_printer.print_begin('Creating empty dataframe...')
            df = pd.DataFrame()
            self._serial_printer.print_end('Complete.')

        self._serial_printer.print_end('Complete.')

        return df

    def parse_dividends(self, modules):

        self._serial_printer.print_begin('Parsing dividends from response...')

        if 'events' in modules and \
            'dividends' in modules['events']:
            # Get the splits dictionary from the JSON API output.
            self._serial_printer.print_begin('Finding dividends in response...')
            dict = modules['events']['dividends']
            self._serial_printer.print_end('Complete.')

            # Convert the splits dictionary to a Dataframe.
            self._serial_printer.print_begin('Creating dataframe...')
            df = pd.DataFrame.from_dict(dict, orient='index')
            self._serial_printer.print_end('Complete.')

            self._serial_printer.print_begin('Formatting columns...')
            df['date'] = pd.to_datetime(df['date'], unit='s')
            df = df.set_index('date').sort_index()
            self._serial_printer.print_end('Complete.')

        else:
            self._serial_printer.print_begin('Creating empty dataframe...')
            df = pd.DataFrame()
            self._serial_printer.print_end('Complete.')

        self._serial_printer.print_end('Complete.')

        return df

    def parse_splits(self, modules):

        self._serial_printer.print_begin('Parsing splits from response...')

        if 'events' in modules and \
            'splits' in modules['events']:

            # Get the splits dictionary from the JSON API output.
            self._serial_printer.print_begin('Finding dividends in response...')
            dict = modules['events']['splits']
            self._serial_printer.print_end('Complete.')

            self._serial_printer.print_begin('Creating dataframe...')
            df = pd.DataFrame.from_dict(dict, orient='index')
            self._serial_printer.print_end('Complete.')

            self._serial_printer.print_begin('Formatting columns...')
            df['date'] = pd.to_datetime(df['date'], unit='s')
            df = df.set_index('date').sort_index()
            self._serial_printer.print_end('Complete.')

        else:
            self._serial_printer.print_begin('Creating empty dataframe...')
            df = pd.DataFrame()
            self._serial_printer.print_end('Complete.')

        self._serial_printer.print_end('Complete.')

        return df
