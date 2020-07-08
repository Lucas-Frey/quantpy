from pipelines.yahoo.summary.YahooSummary import YahooSummary
from printers.SerialPrinter import SerialPrinter

import pandas as pd
import os


class YahooSummaryWriter:

    def __init__(self, symbol: str):
        self._symbol = symbol.lower()

        self._serial_printer = SerialPrinter()

        self.directory = os.getcwd() + '\\data\\' + self._symbol + '\\summary\\'
        if not os.path.isdir(self.directory):
            os.makedirs(self.directory)

    def write(self, df, path, append=True, use_index=False, index_name='date'):
        if os.path.exists(path) and append:
            if use_index:
                temp_df = pd.read_csv(path, index_col=index_name)
            else:
                temp_df = pd.read_csv(path, index_col=None)
                
            temp_df = temp_df.append(df)
            temp_df.to_csv(path, index=False)
        else:
            if use_index:
                df.to_csv(path, index=index_name)
            else:
                df.to_csv(path, index=None)

    def write_all(self, ys: YahooSummary, append=False):
        self.write_profile(ys, append=append)
        self.write_company_officers(ys, append=append)
        self.write_income_statements(ys, append=append)
        self.write_income_statements_quarterly(ys, append=append)
        self.write_balance_sheets(ys, append=append)
        self.write_balance_sheets_quarterly(ys, append=append)
        self.write_cash_flow_statements(ys, append=append)
        self.write_cash_flow_statements_quarterly(ys, append=append)
        self.write_earnings_estimates(ys, append=append)
        self.write_earnings_estimates_quarterly(ys, append=append)
        self.write_financials_quarterly(ys, append=append)
        self.write_financials_yearly(ys, append=append)
        self.write_earnings_history(ys, append=append)
        self.write_financial_data(ys, append=append)
        self.write_default_key_statistics(ys, append=append)
        self.write_institution_ownership(ys, append=append)
        self.write_insider_holders(ys, append=append)
        self.write_insider_transactions(ys, append=append)
        self.write_fund_ownership(ys, append=append)
        self.write_major_direct_holders(ys, append=append)
        self.write_major_direct_holders_breakdown(ys, append=append)
        self.write_recommendation_trend(ys, append=append)
        self.write_earnings_trend(ys, append=append)
        self.write_industry_trend(ys, append=append)
        self.write_index_trend_info(ys, append=append)
        self.write_index_trend_estimate(ys, append=append)
        self.write_sector_trend(ys, append=append)
        self.write_calendar_events_earnings(ys, append=append)
        self.write_calendar_events_dividends(ys, append=append)
        self.write_sec_filings(ys, append=append)
        self.write_upgrade_downgrade_history(ys, append=append)
        self.write_net_share_purchase_activity(ys, append=append)

    def write_profile(self, ys: YahooSummary, append=False):
        """
        Method for writing the profile to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing profile')
        self.write(ys.profile,
                   ys.profile_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_company_officers(self, ys: YahooSummary, append=False):
        """
        Method for writing the company officers to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing company officers')
        self.write(ys.company_officers,
                   ys.company_officers_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_income_statements(self, ys: YahooSummary, append=False):
        """
        Method for writing the income statements to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing income statements')
        self.write(ys.income_statements,
                   ys.income_statements_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_income_statements_quarterly(self, ys: YahooSummary, append=False):
        """
        Method for writing the income statements quarterly to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing income statements quarterly')
        self.write(ys.income_statements_quarterly,
                   ys.income_statements_quarterly_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_balance_sheets(self, ys: YahooSummary, append=False):
        """
        Method for writing the balance sheets to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing balance sheets')
        self.write(ys.balance_sheets,
                   ys.balance_sheets_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_balance_sheets_quarterly(self, ys: YahooSummary, append=False):
        """
        Method for writing the balance sheets quarterly to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing balance sheets quarterly')
        self.write(ys.balance_sheets_quarterly,
                   ys.balance_sheets_quarterly_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_cash_flow_statements(self, ys: YahooSummary, append=False):
        """
        Method for writing the cash flow statements to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing cash flow statements')
        self.write(ys.cash_flow_statements,
                   ys.cash_flow_statements_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_cash_flow_statements_quarterly(self, ys: YahooSummary, append=False):
        """
        Method for writing the cash flow statements quarterly to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin(
            'Writing cash flow statements quarterly')
        self.write(ys.cash_flow_statements_quarterly,
                   ys.cash_flow_statements_quarterly_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_earnings_estimates(self, ys: YahooSummary, append=False):
        """
        Method for writing the earnings estimates to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing earnings estimates')
        self.write(ys.earnings_estimates,
                   ys.earnings_estimates_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_earnings_estimates_quarterly(self, ys: YahooSummary, append=False):
        """
        Method for writing the earnings estimates quarterly to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing earnings estimates quarterly')
        self.write(ys.earnings_estimates_quarterly,
                   ys.earnings_estimates_quarterly_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_financials_quarterly(self, ys: YahooSummary, append=False):
        """
        Method for writing the financials quarterly to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing financials quarterly')
        self.write(ys.financials_quarterly,
                   ys.financials_quarterly_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_financials_yearly(self, ys: YahooSummary, append=False):
        """
        Method for writing the financials yearly to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing financials yearly')
        self.write(ys.financials_yearly,
                   ys.financials_yearly_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_earnings_history(self, ys: YahooSummary, append=False):
        """
        Method for writing the earnings history to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing earnings history')
        self.write(ys.earnings_history,
                   ys.earnings_history_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_financial_data(self, ys: YahooSummary, append=False):
        """
        Method for writing the financial data to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing financial data')
        self.write(ys.financial_data,
                   ys.financial_data_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_default_key_statistics(self, ys: YahooSummary, append=False):
        """
        Method for writing the default key statistics to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing default key statistics')
        self.write(ys.default_key_statistics,
                   ys.default_key_statistics_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_institution_ownership(self, ys: YahooSummary, append=False):
        """
        Method for writing the institution ownership to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing institution ownership')
        self.write(ys.institution_ownership,
                   ys.institution_ownership_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_insider_holders(self, ys: YahooSummary, append=False):
        """
        Method for writing the insider holders to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing insider holders')
        self.write(ys.insider_holders,
                   ys.insider_holders_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_insider_transactions(self, ys: YahooSummary, append=False):
        """
        Method for writing the insider transactions to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing insider transactions')
        self.write(ys.insider_transactions,
                   ys.insider_transactions_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_fund_ownership(self, ys: YahooSummary, append=False):
        """
        Method for writing the fund ownership to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing fund ownership')
        self.write(ys.fund_ownership,
                   ys.fund_ownership_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_major_direct_holders(self, ys: YahooSummary, append=False):
        """
        Method for writing the major direct holders to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing major direct holders')
        self.write(ys.major_direct_holders,
                   ys.major_direct_holders_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_major_direct_holders_breakdown(self, ys: YahooSummary, append=False):
        """
        Method for writing the major direct holders breakdown to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin(
            'Writing major direct holders breakdown')
        self.write(ys.major_direct_holders_breakdown,
                   ys.major_direct_holders_breakdown_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_recommendation_trend(self, ys: YahooSummary, append=False):
        """
        Method for writing the recommendation trend to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing recommendation trend')
        self.write(ys.recommendation_trend,
                   ys.recommendation_trend_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_earnings_trend(self, ys: YahooSummary, append=False):
        """
        Method for writing the earnings trend to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing earnings trend')
        self.write(ys.earnings_trend,
                   ys.earnings_trend_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_industry_trend(self, ys: YahooSummary, append=False):
        """
        Method for writing the industry trend to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing industry trend')
        self.write(ys.industry_trend,
                   ys.industry_trend_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_index_trend_info(self, ys: YahooSummary, append=False):
        """
        Method for writing the index trend info to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing index trend info')
        self.write(ys.index_trend_info,
                   ys.index_trend_info_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_index_trend_estimate(self, ys: YahooSummary, append=False):
        """
        Method for writing the index trend estimate to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing index trend estimate')
        self.write(ys.index_trend_estimate,
                   ys.index_trend_estimate_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_sector_trend(self, ys: YahooSummary, append=False):
        """
        Method for writing the sector trend to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing sector trend')
        self.write(ys.sector_trend,
                   ys.sector_trend_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_calendar_events_earnings(self, ys: YahooSummary, append=False):
        """
        Method for writing the calendar events earnings to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing calendar events earnings')
        self.write(ys.calendar_events_earnings,
                   ys.calendar_events_earnings_path,
                   use_index=True, append=append)
        self._serial_printer.print_end('Complete!')

    def write_calendar_events_dividends(self, ys: YahooSummary, append=False):
        """
        Method for writing the calendar events dividends to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing calendar events dividends')
        self.write(ys.calendar_events_dividends,
                   ys.calendar_events_dividends_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_sec_filings(self, ys: YahooSummary, append=False):
        """
        Method for writing the sec filings to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing sec filings')
        self.write(ys.sec_filings,
                   ys.sec_filings_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_upgrade_downgrade_history(self, ys: YahooSummary, append=False):
        """
        Method for writing the upgrade downgrade history to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing upgrade downgrade history')
        self.write(ys.upgrade_downgrade_history,
                   ys.upgrade_downgrade_history_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

    def write_net_share_purchase_activity(self, ys: YahooSummary, append=False):
        """
        Method for writing the net share purchase activity to a file.
        :param append: Whether or not to append or overwrite existing file.
        """

        self._serial_printer.print_begin('Writing net share purchase activity')
        self.write(ys.net_share_purchase_activity,
                   ys.net_share_purchase_activity_path,
                   use_index=False, append=append)
        self._serial_printer.print_end('Complete!')

# print('def write_all(self, append=False)
# for value in YahooSummary('aapl').as_list():
#     print('\tself.write_{:}(append=append)'.format(value.title))

# for value in YahooSummary('aapl').as
# _list():
#     print('def write_{:}(self, append=False):'.format(value.title))
#     print('\t"""')
#     print('\tMethod for writing the {:} to a file.'.format(
#         value.title.replace('_', ' ')))
#     print(
#         '\t:param append: Whether or not to append or overwrite existing file.')
#     print('\t"""')
#     print('')
#     print('\tself._serial_printer.print_begin(\'Writing {:}\')'.format(
#         value.title.replace('_', ' ')))
#     print('\tself.write(ys.{:},'.format(value.title))
#     print('\t\t\t   ys.{:}_path,'.format(value.title))
#     print('\t\t\t   use_index={:}, append=append)'.format(value.uses_index))
#     print('\tself._serial_printer.print_end(\'Complete!\')')
#     print('')