import abc
import requests

class BaseReader(object):

    def __init__(self, symbol: str, timeout: float = 10.0):
        self.symbol = symbol
        self.timeout = timeout

    @property
    @abc.abstractmethod
    def url(self):
        raise NotImplementedError('Subclass has not implemented property.')

    @property
    @abc.abstractmethod
    def params(self):
        raise NotImplementedError('Subclass has not implemented property.')

    def read(self):
        data = requests.get(url=self.url.format(self.symbol),
                            params=self.params, timeout=self.timeout)
        return data
