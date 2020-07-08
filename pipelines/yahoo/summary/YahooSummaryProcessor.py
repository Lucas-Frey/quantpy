from pipelines.base.BaseProcessor import BaseProcessor
from pipelines.yahoo.summary.YahooSummaryWriter import YahooSummary
from printers.SerialPrinter import SerialPrinter

from utils.utils import flatten
import numpy as np
import re

import pandas as pd


class YahooSummaryProcessor(BaseProcessor):
    """
    Class for processing, parsing, and formatting data recieved from the
    YahooSummaryReader API call.
    """

    def __init__(self, symbol: str):
        """
        Constructor method for the YahooSummarProcess class.
        :param symbol: the company's symbol.
        :param response: The A.P.I. response.
        """

        self._serial_printer = SerialPrinter()

        self._pep_pattern = re.compile(r'(?<!^)(?=[A-Z])')
        self._serial_printer.print_begin('Creating a YahooSummaryProcessor object...')

        super().__init__(symbol)

        self._serial_printer.print_end('Complete')

    def process_all(self, response: object) -> YahooSummary:
        """
        Primary driver method for processing the response.
        :return: A yahoo summary containing the formatted response.
        """

        response_json = response.json()
        ys = YahooSummary(self.symbol)

        modules = response_json['quoteSummary']['result'][0]

        self._serial_printer.print_begin('Parsing financial statement summary datum objects...')
        ys.profile = self.parse_profile(modules, ys.profile_location, ys.profile_removables)
        ys.company_officers = self.parse_company_officers(modules, ys.company_officers_location, ys.company_officers_removables)
        ys.income_statements = self.parse_income_statements(modules, ys.income_statements_location, ys.income_statements_removables)
        ys.income_statements_quarterly = self.parse_income_statements_quarterly(modules, ys.income_statements_quarterly_location, ys.income_statements_quarterly_removables)
        ys.balance_sheets = self.parse_balance_sheets(modules, ys.balance_sheets_location, ys.balance_sheets_removables)
        ys.balance_sheets_quarterly = self.parse_balance_sheets_quarterly(modules, ys.balance_sheets_quarterly_location, ys.balance_sheets_quarterly_removables)
        ys.cash_flow_statements = self.parse_cash_flow_statements(modules, ys.cash_flow_statements_location, ys.cash_flow_statements_removables)
        ys.cash_flow_statements_quarterly = self.parse_cash_flow_statements_quarterly(modules, ys.cash_flow_statements_quarterly_location, ys.cash_flow_statements_quarterly_removables)
        ys.earnings_estimates = self.parse_earnings_estimates(modules, ys.earnings_estimates_location, ys.earnings_estimates_removables)
        ys.earnings_estimates_quarterly = self.parse_earnings_estimates_quarterly(modules, ys.earnings_estimates_quarterly_location, ys.earnings_estimates_quarterly_removables)
        ys.financials_quarterly = self.parse_financials_quarterly(modules, ys.financials_quarterly_location, ys.financials_quarterly_removables)
        ys.financials_yearly = self.parse_financials_yearly(modules, ys.financials_yearly_location, ys.financials_yearly_removables)
        ys.earnings_history = self.parse_earnings_history(modules, ys.earnings_history_location, ys.earnings_history_removables)
        ys.financial_data = self.parse_financial_data(modules, ys.financial_data_location, ys.financial_data_removables)
        ys.default_key_statistics = self.parse_default_key_statistics(modules, ys.default_key_statistics_location, ys.default_key_statistics_removables)
        self._serial_printer.print_end('Complete!')

        self._serial_printer.print_begin('Parsing holder summary datum objects...')
        ys.institution_ownership = self.parse_institution_ownership(modules, ys.institution_ownership_location, ys.institution_ownership_removables)
        ys.insider_holders = self.parse_insider_holders(modules, ys.insider_holders_location, ys.insider_holders_removables)
        ys.insider_transactions = self.parse_insider_transactions(modules, ys.insider_transactions_location, ys.insider_transactions_removables)
        ys.fund_ownership = self.parse_fund_ownership(modules, ys.fund_ownership_location, ys.fund_ownership_removables)
        ys.major_direct_holders = self.parse_major_direct_holders(modules, ys.major_direct_holders_location, ys.major_direct_holders_removables)
        ys.major_direct_holders_breakdown = self.parse_major_direct_holders_breakdown(modules, ys.major_direct_holders_breakdown_location, ys.major_direct_holders_breakdown_removables)
        self._serial_printer.print_end('Complete!')

        self._serial_printer.print_begin('Parsing trend summary datum objects...')
        ys.recommendation_trend = self.parse_recommendation_trend(modules, ys.recommendation_trend_location, ys.recommendation_trend_removables)
        ys.earnings_trend = self.parse_earnings_trend(modules, ys.earnings_trend_location, ys.earnings_trend_removables)
        ys.industry_trend = self.parse_industry_trend(modules, ys.industry_trend_location, ys.industry_trend_removables)
        ys.index_trend_info = self.parse_index_trend_info(modules, ys.index_trend_info_location, ys.index_trend_info_removables)
        ys.index_trend_estimate = self.parse_index_trend_estimate(modules, ys.index_trend_estimate_location, ys.index_trend_estimate_removables)
        ys.sector_trend = self.parse_sector_trend(modules, ys.sector_trend_location, ys.sector_trend_removables)
        self._serial_printer.print_end('Complete!')

        self._serial_printer.print_begin('Parsing non financial statement summary datum objects...')
        ys.calendar_events_earnings = self.parse_calendar_events_earnings(modules, ys.calendar_events_earnings_location, ys.calendar_events_earnings_removables)
        ys.calendar_events_dividends = self.parse_calendar_events_dividends(modules, ys.calendar_events_dividends_location, ys.calendar_events_dividends_removables)
        ys.sec_filings = self.parse_sec_filings(modules, ys.sec_filings_location, ys.sec_filings_removables)
        ys.upgrade_downgrade_history = self.parse_upgrade_downgrade_history(modules, ys.upgrade_downgrade_history_location, ys.upgrade_downgrade_history_removables)
        ys.net_share_purchase_activity = self.parse_net_share_purchase_activity(modules, ys.net_share_purchase_activity_location, ys.net_share_purchase_activity_removables)
        self._serial_printer.print_end('Complete!')

        return ys

    def format_dataframe(self, data_dictionary) -> pd.DataFrame:
        """
        Method to format the response dictionary from a module.
        :param data_dictionary: The dictionary from the module.
        :type data_dictionary: dict
        :return: A formatted dataframe containing the pipelines.
        :rtype pd.DataFrame
        """

        # Checks to see if there are any dictionaries or lists within
        # pipelines that need to be flattened.
        if isinstance(data_dictionary, list):
            module = [flatten(data) for data in data_dictionary]
            module = pd.DataFrame(module)
        else:
            module = flatten(data_dictionary)
            module = pd.DataFrame([module])

        # Due to the way yahoo Finance API returns numeric types, the
        # raw integer value is preferred. Therefore, any values with the
        # suffix longfmt (long format) or fmt (format) are removed.
        module_columns = [column for column in module.columns
                          if not ('.fmt' in column or '.longFmt' in column)]

        if 'maxAge' in module_columns:
            module_columns.remove('maxAge')

        # Get a new dataframe.
        module = module[module_columns]

        # Format the headers of the column to match PEP8 standards.
        new_columns_dict = {col: self._pep_pattern.sub('_', col.split('.')[0]).lower() for col in
                            module.columns}
        new_columns_dict['endDate.raw'] = 'date'
        new_columns_dict['earnings_date.raw'] = 'date'
        new_columns_dict['report_date.raw'] = 'date'
        new_columns_dict['epoch_grade_date.raw'] = 'date'

        module.rename(columns=new_columns_dict, inplace=True)

        if 'date' in module.columns:
            try:
                module['date'] = pd.to_datetime(module['date'], unit='s')
                module = module.set_index('date', drop=True).sort_index()
            except Exception as e:
                pass

        module = module.fillna(np.nan)

        return module

    # ------------------------------------------------------------------
    # Methods for parsing financial summary information.
    # ------------------------------------------------------------------

    def parse_profile(self, modules, location, removables=[]) -> pd.DataFrame:
        """
        Method to parse the profile potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the profile within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_company_officers(self, modules, location,
                               removables=[]) -> pd.DataFrame:
        """
        Method to parse the company officers potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the company officers within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_income_statements(self, modules, location,
                                removables=[]) -> pd.DataFrame:
        """
        Method to parse the income statements potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the income statements within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_income_statements_quarterly(self, modules, location,
                                          removables=[]) -> pd.DataFrame:
        """
        Method to parse the income statements quarterly potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the income statements quarterly within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_balance_sheets(self, modules, location,
                             removables=[]) -> pd.DataFrame:
        """
        Method to parse the balance sheets potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the balance sheets within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_balance_sheets_quarterly(self, modules, location,
                                       removables=[]) -> pd.DataFrame:
        """
        Method to parse the balance sheets quarterly potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the balance sheets quarterly within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_cash_flow_statements(self, modules, location,
                                   removables=[]) -> pd.DataFrame:
        """
        Method to parse the cash flow statements potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the cash flow statements within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_cash_flow_statements_quarterly(self, modules, location,
                                             removables=[]) -> pd.DataFrame:
        """
        Method to parse the cash flow statements quarterly potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the cash flow statements quarterly within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_earnings_estimates(self, modules, location,
                                 removables=[]) -> pd.DataFrame:
        """
        Method to parse the earnings estimates potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the earnings estimates within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

        if isinstance(dict['earningsDate'], list):
            dict['earningsDate'] = dict['earningsDate'][0]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_earnings_estimates_quarterly(self, modules, location,
                                           removables=[]) -> pd.DataFrame:
        """
        Method to parse the earnings estimates quarterly potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the earnings estimates quarterly within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_financials_quarterly(self, modules, location,
                                   removables=[]) -> pd.DataFrame:
        """
        Method to parse the financials quarterly potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the financials quarterly within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_financials_yearly(self, modules, location,
                                removables=[]) -> pd.DataFrame:
        """
        Method to parse the financials yearly potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the financials yearly within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_earnings_history(self, modules, location,
                               removables=[]) -> pd.DataFrame:
        """
        Method to parse the earnings history potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the earnings history within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_financial_data(self, modules, location,
                             removables=[]) -> pd.DataFrame:
        """
        Method to parse the financial data potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the financial data within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_default_key_statistics(self, modules, location,
                                     removables=[]) -> pd.DataFrame:
        """
        Method to parse the default key statistics potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the default key statistics within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_institution_ownership(self, modules, location,
                                    removables=[]) -> pd.DataFrame:
        """
        Method to parse the institution ownership potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the institution ownership within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_insider_holders(self, modules, location,
                              removables=[]) -> pd.DataFrame:
        """
        Method to parse the insider holders potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the insider holders within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_insider_transactions(self, modules, location,
                                   removables=[]) -> pd.DataFrame:
        """
        Method to parse the insider transactions potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the insider transactions within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_fund_ownership(self, modules, location,
                             removables=[]) -> pd.DataFrame:
        """
        Method to parse the fund ownership potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the fund ownership within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_major_direct_holders(self, modules, location,
                                   removables=[]) -> pd.DataFrame:
        """
        Method to parse the major direct holders potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the major direct holders within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_major_direct_holders_breakdown(self, modules, location,
                                             removables=[]) -> pd.DataFrame:
        """
        Method to parse the major direct holders breakdown potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the major direct holders breakdown within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_recommendation_trend(self, modules, location,
                                   removables=[]) -> pd.DataFrame:
        """
        Method to parse the recommendation trend potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the recommendation trend within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_earnings_trend(self, modules, location,
                             removables=[]) -> pd.DataFrame:
        """
        Method to parse the earnings trend potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the earnings trend within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_industry_trend(self, modules, location,
                             removables=[]) -> pd.DataFrame:
        """
        Method to parse the industry trend potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the industry trend within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_index_trend_info(self, modules, location,
                               removables=[]) -> pd.DataFrame:
        """
        Method to parse the index trend info potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the index trend info within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_index_trend_estimate(self, modules, location,
                                   removables=[]) -> pd.DataFrame:
        """
        Method to parse the index trend estimate potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the index trend estimate within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_sector_trend(self, modules, location,
                           removables=[]) -> pd.DataFrame:
        """
        Method to parse the sector trend potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the sector trend within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_calendar_events_earnings(self, modules, location,
                                       removables=[]) -> pd.DataFrame:
        """
        Method to parse the calendar events earnings potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the calendar events earnings within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

        if isinstance(dict['earningsDate'], list):
            dict['earningsDate'] = dict['earningsDate'][0]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_calendar_events_dividends(self, modules, location,
                                        removables=[]) -> pd.DataFrame:
        """
        Method to parse the calendar events dividends potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the calendar events dividends within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df

    def parse_sec_filings(self, modules, location,
                          removables=[]) -> pd.DataFrame:
        """
        Method to parse the sec filings potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the sec filings within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
            df['epoch_date'] = pd.to_datetime(df['epoch_date'])

        else:
            df = pd.DataFrame()


        self._serial_printer.print_begin('Complete.')

        return df


    def parse_upgrade_downgrade_history(self, modules, location,
                                        removables=[]) -> pd.DataFrame:
        """
        Method to parse the upgrade downgrade history potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the upgrade downgrade history within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df


    def parse_net_share_purchase_activity(self, modules, location,
                                          removables=[]) -> pd.DataFrame:
        """
        Method to parse the net share purchase activity potion of the response.
        :param modules: The JSON dictionary response.
        :param location: The keys that lead to the data..
        :param removables: The keys that need to be removed from data.
        """

        is_present = True
        dict = modules

        # Trying to see if the data is within the response.
        self._serial_printer.print_begin(
            'Searching for the net share purchase activity within the response...')
        for value in location:
            if is_present and value in dict:
                dict = dict[value]
            else:
                is_present = False
        self._serial_printer.print_begin('Complete.')

        # If data is present, it will format it into a dataframe.
        self._serial_printer.print_begin('Creating a dataframe for the data.')
        if is_present:
            if len(removables) > 0:
                for value in removables:
                    del dict[value]

            df = self.format_dataframe(dict)
        else:
            df = pd.DataFrame()
        self._serial_printer.print_begin('Complete.')

        return df


# for value in YahooSummary('aapl').as_list():
#     print(
#         'def parse_{:}(self, modules, location, removables=[]) -> pd.DataFrame:'.format(
#             value.title))
#     print('\t"""')
#     print('\tMethod to parse the {:} potion of the response.'.format(
#         value.title.replace('_', ' ')))
#     print('\t:param modules: The JSON dictionary response.')
#     print('\t:param location: The keys that lead to the data..')
#     print('\t:param removables: The keys that need to be removed from data.')
#     print('\t"""')
#     print('')
#
#     print('\tis_present = True')
#     print('\tdict = modules')
#     print('')
#
#     print('\t# Trying to see if the data is within the response.')
#
#     print(
#         '\tself._serial_printer.print_begin(\'Searching for the {:} within the response...\')'.format(
#             value.title.replace('_', ' ')))
#     print('\tfor value in location:')
#     print('\t\tif is_present and value in dict:')
#     print('\t\t\tdict = dict[value]')
#     print('\t\telse:')
#     print('\t\t\tis_present = False')
#     print('\tself._serial_printer.print_begin(\'Complete.\')')
#     print('')
#
#     print('\t# If data is present, it will format it into a dataframe.')
#     print(
#         '\tself._serial_printer.print_begin(\'Creating a dataframe for the data.\')')
#     print('\tif is_present:')
#     print('\t\tif len(removables) > 0:')
#     print('\t\t\tfor value in removables:')
#     print('\t\t\t\tdel dict[value]')
#     print('')
#     print('\t\tdf = self.format_dataframe(dict)')
#     print('\telse:')
#     print('\t\tdf = pd.DataFrame()')
#     print('\tself._serial_printer.print_begin(\'Complete.\')')
#     print('')
#
#     print('\treturn df')
#     print('')