from pipelines.yahoo.quote.YahooQuote import YahooQuote
from printers.SerialPrinter import SerialPrinter

import pandas as pd


class YahooQuoteReader():

    def __init__(self, symbol: str):
        self._symbol = symbol
        self._yq = YahooQuote(self._symbol)

        self._serial_printer = SerialPrinter()

    def format(self, df):
        return df

    def read_quote(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading quote')
        df = pd.read_csv(self._yq.quote.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self._yq.quote = df
        return self._yq

    def read_dividends(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading dividends')
        df = pd.read_csv(self._yq.dividends.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self._yq.dividends = df
        return self._yq

    def read_splits(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading splits')
        df = pd.read_csv(self._yq.splits.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self._yq.splits = df
        return self._yq

# for value in YahooQuote('aapl').as_list():
#     print('def read_{:}(self, format_value=False):'.format(value.title))
#     print('\t"""')
#     print('\tMethod for reading the data from the file.')
#     print('\t:param format_value: Whether or not to format the data.')
#     print('\t"""')
#     print('')
#     print('\tself._serial_printer.print_begin(\'Reading {:}\')'.format(value.title))
#     print('\tdf = pd.read_csv(self._yq.{:}.path)'.format(value.title))
#     print('\tself._serial_printer.print_end(\'Complete.\')')
#     print('')
#     print('\tif format_value:')
#     print('\t\tdf = self.format(df)')
#     print('')
#     print('\tself._yq.{:} = df'.format(value.title))
#     print('\treturn self._yq')
#     print('')