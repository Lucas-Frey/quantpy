import pandas as pd
import os
from printers.SerialPrinter import SerialPrinter


class YahooQuote:

    def __init__(self, symbol: str):
        """
        Constructor method to create the class. It will set all of the
        class instance variables to none.
        :param symbol: The string symbol for the company.
        """

        self._serial_printer = SerialPrinter()

        self._serial_printer.print_begin('Creating a YahooSummary object...')

        # Save the company's symbol as an instance variable.
        self._serial_printer.print_begin('Creating Yahoo quote instance variables...')
        self._symbol = symbol.lower()
        self._directory = os.getcwd() + '\\data\\' + self._symbol + '\\quote\\'
        self._serial_printer.print_end('Complete!')

        self._serial_printer.print_begin('Creating quote datum objects...')
        self._quote = self.Datum(None, 'quote', self._directory + '_quote.csv')
        self._dividends = self.Datum(None, 'dividends', self._directory + '_dividends.csv')
        self._splits = self.Datum(None, 'splits', self._directory + '_splits.csv')
        self._serial_printer.print_end('Complete.')

    def as_list(self):
        return [self._quote,
                self._dividends,
                self._splits]

    @property
    def quote_path(self):
        """
        A getter method to get the path to the company's quote data.
        """

        return self._quote.path

    @property
    def quote(self):
        """
        A getter method to get a company's quote data.
        """

        return self._quote.value

    @quote.setter
    def quote(self, value):
        """
        A setter method to set a company's quote data.
        :param value: The value to be set.
        """

        self._quote.value = value

    @property
    def dividends_path(self):
        """
        A getter method to get the path to the company's dividends data.
        """

        return self._dividends.path

    @property
    def dividends(self):
        """
        A getter method to get a company's dividends data.
        """

        return self._dividends.value

    @dividends.setter
    def dividends(self, value):
        """
        A setter method to set a company's dividends data.
        :param value: The value to be set.
        """

        self._dividends.value = value

    @property
    def splits_path(self):
        """
        A getter method to get the path to the company's splits data.
        """

        return self._splits.path

    @property
    def splits(self):
        """
        A getter method to get a company's splits data.
        """

        return self._splits.value

    @splits.setter
    def splits(self, value):
        """
        A setter method to set a company's splits data.
        :param value: The value to be set.
        """

        self._splits.value = value

    class Datum:
        def __init__(self, value, title, path):
            self._value = value
            self._title = title
            self._path = path

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        @property
        def title(self):
            return self._title

        @property
        def path(self):
            return self._path

# for value in YahooQuote('aapl').as_list():
#     print('@property')
#     print('def {:}_path(self):'.format(value.title))
#     print('\t"""')
#     print('\tA getter method to get the path to the company\'s {:} data.'.format(value.title.replace('_', ' ')))
#     print('\t"""')
#
#     print('')
#     print('\treturn self._{:}.path'.format(value.title))
#     print('')
#
#     print('@property')
#     print('def {:}(self):'.format(value.title))
#     print('\t"""')
#     print('\tA getter method to get a company\'s {:} data.'.format(value.title.replace('_', ' ')))
#     print('\t"""')
#
#     print('')
#     print('\treturn self._{:}.value'.format(value.title))
#     print('')
#
#     print('@{:}.setter'.format(value.title))
#     print('def {:}(self, value):'.format(value.title))
#     print('\t"""')
#     print('\tA setter method to set a company\'s {:} data.'.format(value.title.replace('_', ' ')))
#     print('\t:param value: The value to be set.')
#     print('\t"""')
#
#     print('')
#     print('\tself._{:}.value = value'.format(value.title))
#     print('')

