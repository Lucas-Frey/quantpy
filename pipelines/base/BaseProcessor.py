import abc
from pipelines.base.BaseReader import BaseReader


class BaseProcessor(object):

    def __init__(self, symbol):

        self.symbol = symbol.lower()