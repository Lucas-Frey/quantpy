from pipelines.yahoo.summary.YahooSummary import YahooSummary
from printers.SerialPrinter import SerialPrinter

import pandas as pd

class YahooSummaryReader:

    def __init__(self, symbol: str):
        self._symbol = symbol
        self.ys = YahooSummary(self._symbol)
        self._serial_printer = SerialPrinter()

    def format(self, df):
        return df

    def read_all(self, format_value=False):
        self.ys.profile = self.read_profile(format_value=format_value)
        self.ys.company_officers = self.read_company_officers(format_value=format_value)
        self.ys.income_statements = self.read_income_statements(format_value=format_value)
        self.ys.income_statements_quarterly = self.read_income_statements_quarterly(format_value=format_value)
        self.ys.balance_sheets = self.read_balance_sheets(format_value=format_value)
        self.ys.balance_sheets_quarterly = self.read_balance_sheets_quarterly(format_value=format_value)
        self.ys.cash_flow_statements = self.read_cash_flow_statements(format_value=format_value)
        self.ys.cash_flow_statements_quarterly = self.read_cash_flow_statements_quarterly(format_value=format_value)
        self.ys.earnings_estimates = self.read_earnings_estimates(format_value=format_value)
        self.ys.earnings_estimates_quarterly = self.read_earnings_estimates_quarterly(format_value=format_value)
        self.ys.financials_quarterly = self.read_financials_quarterly(format_value=format_value)
        self.ys.financials_yearly = self.read_financials_yearly(format_value=format_value)
        self.ys.earnings_history = self.read_earnings_history(format_value=format_value)
        self.ys.financial_data = self.read_financial_data(format_value=format_value)
        self.ys.default_key_statistics = self.read_default_key_statistics(format_value=format_value)
        self.ys.institution_ownership = self.read_institution_ownership(format_value=format_value)
        self.ys.insider_holders = self.read_insider_holders(format_value=format_value)
        self.ys.insider_transactions = self.read_insider_transactions(format_value=format_value)
        self.ys.fund_ownership = self.read_fund_ownership(format_value=format_value)
        self.ys.major_direct_holders = self.read_major_direct_holders(format_value=format_value)
        self.ys.major_direct_holders_breakdown = self.read_major_direct_holders_breakdown(format_value=format_value)
        self.ys.recommendation_trend = self.read_recommendation_trend(format_value=format_value)
        self.ys.earnings_trend = self.read_earnings_trend(format_value=format_value)
        self.ys.industry_trend = self.read_industry_trend(format_value=format_value)
        self.ys.index_trend_info = self.read_index_trend_info(format_value=format_value)
        self.ys.index_trend_estimate = self.read_index_trend_estimate(format_value=format_value)
        self.ys.sector_trend = self.read_sector_trend(format_value=format_value)
        self.ys.calendar_events_earnings = self.read_calendar_events_earnings(format_value=format_value)
        self.ys.calendar_events_dividends = self.read_calendar_events_dividends(format_value=format_value)
        self.ys.sec_filings = self.read_sec_filings(format_value=format_value)
        self.ys.upgrade_downgrade_history = self.read_upgrade_downgrade_history(format_value=format_value)
        self.ys.net_share_purchase_activity = self.read_net_share_purchase_activity(format_value=format_value)

        return self.ys

    def read_profile(self, ys: YahooSummary=None, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading profile')
        df = pd.read_csv(self.ys.profile.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.profile = df
        return self.ys

    def read_company_officers(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading company_officers')
        df = pd.read_csv(self.ys.company_officers.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.company_officers = df
        return self.ys

    def read_income_statements(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading income_statements')
        self._serial_printer.print_begin('REading')
        df = pd.read_csv(self.ys.income_statements.path)

        if format_value:
            df = self.format(df)

        self.ys.income_statements = df
        return self.ys

    def read_income_statements_quarterly(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading income_statements_quarterly')
        df = pd.read_csv(self.ys.income_statements_quarterly.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.income_statements_quarterly = df
        return self.ys

    def read_balance_sheets(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading balance_sheets')
        df = pd.read_csv(self.ys.balance_sheets.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.balance_sheets = df
        return self.ys

    def read_balance_sheets_quarterly(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading balance_sheets_quarterly')
        df = pd.read_csv(self.ys.balance_sheets_quarterly.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.balance_sheets_quarterly = df
        return self.ys

    def read_cash_flow_statements(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading cash_flow_statements')
        df = pd.read_csv(self.ys.cash_flow_statements.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.cash_flow_statements = df
        return self.ys

    def read_cash_flow_statements_quarterly(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin(
            'Reading cash_flow_statements_quarterly')
        df = pd.read_csv(self.ys.cash_flow_statements_quarterly.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.cash_flow_statements_quarterly = df
        return self.ys

    def read_earnings_estimates(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading earnings_estimates')
        df = pd.read_csv(self.ys.earnings_estimates.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.earnings_estimates = df
        return self.ys

    def read_earnings_estimates_quarterly(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading earnings_estimates_quarterly')
        df = pd.read_csv(self.ys.earnings_estimates_quarterly.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.earnings_estimates_quarterly = df
        return self.ys

    def read_financials_quarterly(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading financials_quarterly')
        df = pd.read_csv(self.ys.financials_quarterly.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.financials_quarterly = df
        return self.ys

    def read_financials_yearly(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading financials_yearly')
        df = pd.read_csv(self.ys.financials_yearly.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.financials_yearly = df
        return self.ys

    def read_earnings_history(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading earnings_history')
        df = pd.read_csv(self.ys.earnings_history.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.earnings_history = df
        return self.ys

    def read_financial_data(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading financial_data')
        df = pd.read_csv(self.ys.financial_data.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.financial_data = df
        return self.ys

    def read_default_key_statistics(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading default_key_statistics')
        df = pd.read_csv(self.ys.default_key_statistics.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.default_key_statistics = df
        return self.ys

    def read_institution_ownership(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading institution_ownership')
        df = pd.read_csv(self.ys.institution_ownership.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.institution_ownership = df
        return self.ys

    def read_insider_holders(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading insider_holders')
        df = pd.read_csv(self.ys.insider_holders.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.insider_holders = df
        return self.ys

    def read_insider_transactions(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading insider_transactions')
        df = pd.read_csv(self.ys.insider_transactions.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.insider_transactions = df
        return self.ys

    def read_fund_ownership(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading fund_ownership')
        df = pd.read_csv(self.ys.fund_ownership.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.fund_ownership = df
        return self.ys

    def read_major_direct_holders(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading major_direct_holders')
        df = pd.read_csv(self.ys.major_direct_holders.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.major_direct_holders = df
        return self.ys

    def read_major_direct_holders_breakdown(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin(
            'Reading major_direct_holders_breakdown')
        df = pd.read_csv(self.ys.major_direct_holders_breakdown.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.major_direct_holders_breakdown = df
        return self.ys

    def read_recommendation_trend(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading recommendation_trend')
        df = pd.read_csv(self.ys.recommendation_trend.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.recommendation_trend = df
        return self.ys

    def read_earnings_trend(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading earnings_trend')
        df = pd.read_csv(self.ys.earnings_trend.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.earnings_trend = df
        return self.ys

    def read_industry_trend(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading industry_trend')
        df = pd.read_csv(self.ys.industry_trend.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.industry_trend = df
        return self.ys

    def read_index_trend_info(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading index_trend_info')
        df = pd.read_csv(self.ys.index_trend_info.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.index_trend_info = df
        return self.ys

    def read_index_trend_estimate(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading index_trend_estimate')
        df = pd.read_csv(self.ys.index_trend_estimate.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.index_trend_estimate = df
        return self.ys

    def read_sector_trend(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading sector_trend')
        df = pd.read_csv(self.ys.sector_trend.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.sector_trend = df
        return self.ys

    def read_calendar_events_earnings(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading calendar_events_earnings')
        df = pd.read_csv(self.ys.calendar_events_earnings.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.calendar_events_earnings = df
        return self.ys

    def read_calendar_events_dividends(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading calendar_events_dividends')
        df = pd.read_csv(self.ys.calendar_events_dividends.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.calendar_events_dividends = df
        return self.ys

    def read_sec_filings(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading sec_filings')
        df = pd.read_csv(self.ys.sec_filings.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.sec_filings = df
        return self.ys

    def read_upgrade_downgrade_history(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading upgrade_downgrade_history')
        df = pd.read_csv(self.ys.upgrade_downgrade_history.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.upgrade_downgrade_history = df
        return self.ys

    def read_net_share_purchase_activity(self, format_value=False):
        """
        Method for reading the data from the file.
        :param format_value: Whether or not to format the data.
        """

        self._serial_printer.print_begin('Reading net_share_purchase_activity')
        df = pd.read_csv(self.ys.net_share_purchase_activity.path)
        self._serial_printer.print_end('Complete.')

        if format_value:
            df = self.format(df)

        self.ys.net_share_purchase_activity = df
        return self.ys

# print('self.ys.{:} = self.read_{:}(format=format)'.format(value.title, value.title))

# if __name__ == '__main__':
#     for value in YahooSummary('aapl').as_list():
#         print('def read_{:}(self, format_value=False):'.format(value.title))
#         print('\t"""')
#         print('\tMethod for reading the data from the file.')
#         print('\t:param format_value: Whether or not to format the data.')
#         print('\t"""')
#         print('')
#         print('\tself._serial_printer.print_begin(\'Reading self.ys.{:}.path\')'.format(value))
#         print('\tdf = pd.read_csv(self.ys.{:}.path)'.format(value.title))
#         print('\tself._serial_printer.print_end(\'Complete.\')')
#         print('')
#         print('\tif format_value:')
#         print('\t\tdf = self.format(df)')
#         print('')
#         print('\tself.ys.{:} = df'.format(value.title))
#         print('\treturn self.ys')
#         print('')