import abc
import requests

class BaseReader(object):

    def __init__(self, symbol: str, timeout: float = 10.0):
        self._symbol = symbol
        self._timeout = timeout

    @property
    @abc.abstractmethod
    def url(self):
        raise NotImplementedError('Subclass has not implemented property.')

    @property
    @abc.abstractmethod
    def params(self):
        raise NotImplementedError('Subclass has not implemented property.')

    @abc.abstractmethod
    def read(self):
        data = requests.get(url=self.url.format(self._symbol),
                            params=self.params, timeout=self._timeout)
        return data
