import abc
from data.base.BaseReader import BaseReader


class BaseProcessor(object):

    def __init__(self, symbol, response: object, reader: BaseReader):

        self.symbol = symbol
        self.response = response
        self.reader = reader

    def process(self):
        # Raise this since this is an abstract property.
        raise NotImplementedError('Subclass has not implemented method.')