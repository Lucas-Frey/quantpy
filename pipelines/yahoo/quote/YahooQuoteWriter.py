import pandas as pd
import os

from pipelines.yahoo.quote.YahooQuote import YahooQuote
from printers.SerialPrinter import SerialPrinter


class YahooQuoteWriter:

    def __init__(self, symbol: str):
        self._symbol = symbol.lower()

        self._quote = None
        self._dividends = None
        self._splits = None

        self._yq = YahooQuote(self._symbol)
        self._serial_printer = SerialPrinter()

    def write(self, df, path, append=True):
        """
        Method to write the data to a file.
        :param df: The data in dataframe form.
        :param path: The path to where the data needs to be written.
        :param append: Whether or not to append the data.
        """

        if os.path.exists(path) and append:
            temp_df = pd.read_csv(path, index_col='date')

            temp_df = temp_df.append(df)
            temp_df.to_csv(path, index=False)
        else:
            df.to_csv(path, index='date')

    def write_quote(self, append=False):
        """
        Method for writing the quote to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing quote')
        self.write(self._yq.quote,
                   self._yq.quote.path,
                   append=append)
        self._serial_printer.print_end('Complete!')

    def write_dividends(self, append=False):
        """
        Method for writing the dividends to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing dividends')
        self.write(self._yq.dividends,
                   self._yq.dividends.path,
                   append=append)
        self._serial_printer.print_end('Complete!')

    def write_splits(self, append=False):
        """
        Method for writing the splits to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing splits')
        self.write(self._yq.splits,
                   self._yq.splits.path,
                   append=append)
        self._serial_printer.print_end('Complete!')


# for value in YahooQuote('aapl').as_list():
#     print('def write_{:}(self, append=False):'.format(value.title))
#     print('\t"""')
#     print('\tMethod for writing the {:} to a file.'.format(value.title.replace('_', ' ')))
#     print('\t:param append: Whether or not to append or overwrite existing file.')
#     print('\t"""')
#     print('')
#     print('\tself._serial_printer.print_begin(\'Writing {:}\')'.format(value.title.replace('_', ' ')))
#     print('\tself.write(self._summary.{:},'.format(value.title))
#     print('\t\t\t   self._summary.{:}.path,'.format(value.title))
#     print('\t\t\t   use_index={:}, append=append)'.format(value.uses_index))
#     print('\tself._serial_printer.print_end(\'Complete!\')')
#     print('')