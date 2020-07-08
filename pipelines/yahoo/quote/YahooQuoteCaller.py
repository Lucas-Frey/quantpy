from pipelines.base.BaseReader import BaseReader


class YahooQuoteReader(BaseReader):
    def __init__(self, symbol: str,
                 period_start: int = 0,
                 period_end: int = 9999999999,
                 interval: str = '1d',
                 include_events: bool = False,
                 include_prepost: bool = False):

        self.period_start = period_start
        self.period_end = period_end
        self.interval = interval
        self.include_events = include_events
        self.include_prepost = include_prepost

        # Call the super class' constructor.
        super().__init__(symbol)

    @property
    def url(self):
        return 'https://query1.finance.yahoo.com/v8/finance/chart/{}'

    @property
    def params(self):
        if self.include_events:
            events_param = 'div,splits'
        else:
            events_param = ''

        return {'period1': self.period_start, 'period2': self.period_end,
                'interval': self.interval,
                'includePrePost': self.include_prepost, 'events': events_param}