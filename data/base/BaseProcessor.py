import abc


class BaseProcessor(object):

    def __init__(self, symbol, response: object):

        self._symbol = symbol
        self._response = response


    def process(self):

        # Raise this since this is an abstract property.
        raise NotImplementedError('Subclass has not implemented method.')