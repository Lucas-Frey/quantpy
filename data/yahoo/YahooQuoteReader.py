import datetime
import time
import pandas as pd
from data.base.BaseReader import BaseReader


class YahooQuoteReader(BaseReader):
    def __init__(self, symbol: str,
                 period_start: int = 0,
                 period_end: int = 9999999999,
                 interval: str = '1d',
                 include_events: bool = False,
                 include_prepost: bool = False):

        self._period_start = period_start
        self._period_end = period_end
        self._interval = interval
        self._include_events = include_events
        self._include_prepost = include_prepost

        # Call the super class' constructor.
        super().__init__(symbol)

    @property
    def url(self):
        return 'https://query1.finance.yahoo.com/v8/finance/chart/{}'

    @property
    def params(self):
        if self._include_events:
            events_param = 'div,splits'
        else:
            events_param = ''

        return {'period1': self._period_start, 'period2': self._period_end,
                'interval': self._interval,
                'includePrePost': self._include_prepost, 'events': events_param}