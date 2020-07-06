from data.base.BaseProcessor import BaseProcessor
from data.Yahoo.YahooSummaryReader import YahooSummaryReader
from data.Yahoo.YahooSummary import YahooSummary
from utils.utils import flatten

import pandas as pd


class YahooSummaryProcessor(BaseProcessor):

    def __init__(self, symbol: str, response: object, reader: YahooSummaryReader):

        # Assign all financial information to the value requested.
        self.include_asset_profile = reader.include_asset_profile
        self.include_income_statement_history = reader.include_income_statement_history
        self.include_income_statement_history_quarterly = reader.include_income_statement_history_quarterly
        self.include_balance_sheet_history = reader.include_balance_sheet_history
        self.include_balance_sheet_history_quarterly = reader.include_balance_sheet_history_quarterly
        self.include_cash_flow_statement_history = reader.include_cash_flow_statement_history
        self.include_cash_flow_statement_history_quarterly = reader.include_cash_flow_statement_history_quarterly
        self.include_earnings = reader.include_earnings
        self.include_earnings_history = reader.include_earnings_history
        self.include_financial_data = reader.include_financial_data
        self.include_default_key_statistics = reader.include_default_key_statistics

        # Assign all holders information to the value requested.
        self.include_institution_ownership = reader.include_institution_ownership
        self.include_insider_holders = reader.include_insider_holders
        self.include_insider_transactions = reader.include_insider_transactions
        self.include_fund_ownership = reader.include_fund_ownership
        self.include_major_direct_holders = reader.include_major_direct_holders
        self.include_major_direct_holders_breakdown = reader.include_major_direct_holders_breakdown

        # Assign all trends information to the value requested.
        self.include_recommendation_trend = reader.include_recommendation_trend
        self.include_earnings_trend = reader.include_earnings_trend
        self.include_industry_trend = reader.include_industry_trend
        self.include_index_trend = reader.include_index_trend
        self.include_sector_trend = reader.include_sector_trend

        # Assign all non-financial information to the value requested.
        self.include_calendar_events = reader.include_calendar_events
        self.include_sec_filings = reader.include_sec_filings
        self.include_upgrade_downgrade_history = reader.include_upgrade_downgrade_history
        self.include_net_share_purchase_activity = reader.include_net_share_purchase_activity

        self.include_all = reader.include_all

        super().__init__(symbol, response, reader)

    def process(self):
        response_json = self._response.json()
        yahoo_summary = YahooSummary(self._symbol)

        modules_dict = response_json['quoteSummary']['result'][0]

        if self.include_asset_profile:
            yahoo_summary.profile = self.parse_module_asset_profile_profile(modules_dict, 'assetProfile')
            yahoo_summary.company_officers = self.parse_module_asset_profile_company_officers(modules_dict, 'assetProfile')

        if self.include_income_statement_history:
            yahoo_summary.income_statement_history = self.parse_module(modules_dict, 'incomeStatementHistory',
                                                             'incomeStatementHistory')

        if self.include_income_statement_history_quarterly:
            yahoo_summary.income_statement_history_quarterly = self.parse_module(modules_dict, 'incomeStatementHistoryQuarterly',
                                                                       'incomeStatementHistory')

        if self.include_balance_sheet_history:
            yahoo_summary.balance_sheet_history = self.parse_module(modules_dict, 'balanceSheetHistory', 'balanceSheetStatements')

        if self.include_balance_sheet_history_quarterly:
            yahoo_summary.balance_sheet_history_quarterly = self.parse_module(modules_dict, 'balanceSheetHistoryQuarterly',
                                                                    'balanceSheetStatements')

        if self.include_cash_flow_statement_history:
            yahoo_summary.cash_flow_statement_history = self.parse_module(modules_dict, 'cashflowStatementHistory',
                                                                'cashflowStatements')

        if self.include_cash_flow_statement_history_quarterly:
            yahoo_summary.cash_flow_statement_history_quarterly = self.parse_module(modules_dict, 'cashflowStatementHistoryQuarterly',
                                                                          'cashflowStatements')

        if self.include_earnings:
            yahoo_summary.earnings_estimates = self.parse_module_earnings_estimates(modules_dict, 'earnings')
            yahoo_summary.earnings_estimates_quarterly = self.parse_module_earnings_estimates_quarterly(modules_dict, 'earnings')
            yahoo_summary.financials_yearly = self.parse_module_earnings_finance_yearly(modules_dict, 'earnings')
            yahoo_summary.financials_quarterly = self.parse_module_earnings_finance_quarterly(modules_dict, 'earnings')

        if self.include_earnings_history:
            yahoo_summary.earnings_history = self.parse_module(modules_dict, 'earningsHistory', 'history')

        if self.include_financial_data:
            yahoo_summary.financial_data = self.parse_module(modules_dict, 'financialData')

        if self.include_default_key_statistics:
            yahoo_summary.default_key_statistics = self.parse_module(modules_dict, 'defaultKeyStatistics')

        if self.include_institution_ownership:
            yahoo_summary.institution_ownership = self.parse_module(modules_dict, 'institutionOwnership', 'ownershipList')

        if self.include_insider_holders:
            yahoo_summary.insider_holders = self.parse_module(modules_dict, 'insiderHolders', 'holders')

        if self.include_insider_transactions:
            yahoo_summary.insider_transactions = self.parse_module(modules_dict, 'insiderTransactions', 'transactions')

        if self.include_fund_ownership:
            yahoo_summary.fund_ownership = self.parse_module(modules_dict, 'fundOwnership', 'ownershipList')

        if self.include_major_direct_holders:
            yahoo_summary.major_direct_holders = self.parse_module(modules_dict, 'majorDirectHolders', 'holders')

        if self.include_major_direct_holders_breakdown:
            yahoo_summary.major_direct_holders_breakdown = self.parse_module(modules_dict, 'majorHoldersBreakdown')

        if self.include_recommendation_trend:
            yahoo_summary.recommendation_trend = self.parse_module(modules_dict, 'recommendationTrend', 'trend')

        if self.include_earnings_trend:
            yahoo_summary.earnings_trend = self.parse_module(modules_dict, 'earningsTrend', 'trend')

        if self.include_industry_trend:
            yahoo_summary.industry_trend = self.parse_module(modules_dict, 'industryTrend')

        if self.include_index_trend:
            yahoo_summary.index_trend_info = self.parse_module_index_trend_info(modules_dict, 'indexTrend')
            yahoo_summary.index_trend_estimate = self.parse_module_index_trend_estimates(modules_dict, 'indexTrend')

        if self.include_sector_trend:
            yahoo_summary.sector_trend = self.parse_module(modules_dict, 'sectorTrend')

        if self.include_calendar_events:
            yahoo_summary.calendar_events_earnings = self.parse_module_calendar_events_earnings(modules_dict, 'calendarEvents')
            yahoo_summary.calendar_events_dividends = self.parse_module_calendar_events_dividends(modules_dict, 'calendarEvents')

        if self.include_sec_filings:
            yahoo_summary.sec_filings = self.parse_module(modules_dict, 'secFilings', 'filings')

        if self.include_upgrade_downgrade_history:
            yahoo_summary.upgrade_downgrade_history = self.parse_module(modules_dict, 'upgradeDowngradeHistory', 'history')

        if self.include_net_share_purchase_activity:
            yahoo_summary.net_share_purchase_activity = self.parse_module(modules_dict, 'netSharePurchaseActivity')

        return yahoo_summary

    def parse_module(self, modules_dict, module_name, submodule_name=None):
        """
        Method to parse an individual requested module returned from the Yahoo Finance API call.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :param submodule_name: The name of the submodule to be parsed. Some modules are wrapped in another dictionary.
        :type submodule_name: str
        :return: A tuple containing a dataframe containing the information and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the module to be parsed. If the module is not found, then it will return None and a
        # YahooModuleNotFoundError.
        try:
            # Checks to see if there is a submodule.
            if not submodule_name:
                module = modules_dict[module_name]
            else:
                module = modules_dict[module_name][submodule_name]

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            module_dataframe = self._format_dataframe(module)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the module information and
        # None since there was no error.
        return module_dataframe, None

    def parse_module_asset_profile_profile(self, modules_dict, module_name):
        """
        Method to parse the assetProfile module returned from the Yahoo Finance API call. The assetProfile module is
        uniquely parsed because it contains two separate pieces of data: The company profile and the company officers.
        This method will parse the profile portion of the assetProfile.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the assetProfile module. If the module is not found, then it will return None and a
        # YahooModuleNotFoundError.
        try:
            profile_dict = modules_dict[module_name]

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            # We are going to remove the company officer's submodule to be parsed later.
            del profile_dict['companyOfficers']
            profile = self._format_dataframe(profile_dict)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the profile
        # information and None since there was no error.
        return profile, None

    def parse_module_asset_profile_company_officers(self, modules_dict, module_name):
        """
        Method to parse the assetProfile module returned from the Yahoo Finance API call. The assetProfile module is
        uniquely parsed because it contains two separate pieces of data: The company profile and the company officers.
        This method will parse the company officers portion of the assetProfile.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the assetProfile and the company_officers submodule. If the module is not found, then it will
        # return None and a YahooModuleNotFoundError.
        try:
            profile_dict = modules_dict[module_name]
            company_officers_dict = profile_dict['companyOfficers']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            company_officers = self._format_dataframe(company_officers_dict)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return company_officers, None

    def parse_module_earnings_estimates(self, modules_dict, module_name):
        """
        Method to parse the earnings module returned from the Yahoo Finance API call. The earnings module is uniquely
        parsed because it contains four separate pieces of data: The company earnings estimates, the company quarterly
        earnings estimates, the company's yearly financials, and the company's quarterly financials.
        This method will parse the company's earnings estimates.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the earnings and the earningsChart submodule. If the module is not found, then it will
        # return None and a YahooModuleNotFoundError.
        try:
            earnings_estimates_dict = modules_dict[module_name]['earningsChart']
            del earnings_estimates_dict['quarterly']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            # Sometimes the earnings data portion is returned as a list instead of a date.
            if isinstance(earnings_estimates_dict['earningsDate'], list):
                earnings_estimates_dict['earningsDate'] = earnings_estimates_dict['earningsDate'][0]

            earnings_estimates = self._format_dataframe(earnings_estimates_dict)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return earnings_estimates, None

    def parse_module_earnings_estimates_quarterly(self, modules_dict, module_name):
        """
        Method to parse the earnings module returned from the Yahoo Finance API call. The earnings module is uniquely
        parsed because it contains four separate pieces of data: The company earnings estimates, the company quarterly
        earnings estimates, the company's yearly financials, and the company's quarterly financials.
        This method will parse the company's quarterly earnings estimates.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the earnings, earningsChart, and quarterly submodule. If the module is not found, then it will
        # return None and a YahooModuleNotFoundError.
        try:
            module = modules_dict[module_name]
            quarterly_earnings_estimates = module['earningsChart']['quarterly']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            earnings_quarterly = self._format_dataframe(quarterly_earnings_estimates)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return earnings_quarterly, None

    def parse_module_earnings_finance_yearly(self, modules_dict, module_name):
        """
        Method to parse the earnings module returned from the Yahoo Finance API call. The earnings module is uniquely
        parsed because it contains four separate pieces of data: The company earnings estimates, the company quarterly
        earnings estimates, the company's yearly financials, and the company's quarterly financials.
        This method will parse the company's yearly financials.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the earnings, financialsChart, and yearly submodule. If the module is not found, then it will
        # return None and a YahooModuleNotFoundError.
        try:
            module = modules_dict[module_name]
            financial_yearly = module['financialsChart']['yearly']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            financial_yearly = self._format_dataframe(financial_yearly)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return financial_yearly, None

    def parse_module_earnings_finance_quarterly(self, modules_dict, module_name):
        """
        Method to parse the earnings module returned from the Yahoo Finance API call. The earnings module is uniquely
        parsed because it contains four separate pieces of data: The company earnings estimates, the company quarterly
        earnings estimates, the company's yearly financials, and the company's quarterly financials.
        This method will parse the company's quarterly financials.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the earnings, financialsChart, and quarterly submodule. If the module is not found, then it
        # will return None and a YahooModuleNotFoundError.
        try:
            module = modules_dict[module_name]
            financial_quarterly = module['financialsChart']['quarterly']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            financial_quarterly = self._format_dataframe(financial_quarterly)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return financial_quarterly, None

    def parse_module_index_trend_info(self, modules_dict, module_name):
        """
        Method to parse the indexTrend module returned from the Yahoo Finance API call. The indexTrend module is
        uniquely parsed because it contains two separate pieces of data: The index trend's information and the index
        trend's estimates. This method will parse the index trend's information portion of the indexTrend.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the indexTrend module. If the module is not found, then it will return None and a
        # YahooModuleNotFoundError.
        try:
            index_trend_info = modules_dict[module_name]

            # Removes the estimates submodule.
            del index_trend_info['estimates']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            index_trend_info = self._format_dataframe(index_trend_info)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return index_trend_info, None

    def parse_module_index_trend_estimates(self, modules_dict, module_name):
        """
        Method to parse the indexTrend module returned from the Yahoo Finance API call. The indexTrend module is
        uniquely parsed because it contains two separate pieces of data: The index trend's information and the index
        trend's estimates. This method will parse the index trend's estimates portion of the indexTrend.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the indexTrend module and the estimates submodule. If the module is not found, then it will
        # return None and a YahooModuleNotFoundError.
        try:
            index_trend_info = modules_dict[module_name]
            index_trend_estimates = index_trend_info['estimates']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            index_trend_estimates = self._format_dataframe(index_trend_estimates)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return index_trend_estimates, None

    def parse_module_calendar_events_earnings(self, modules_dict, module_name):
        """
        Method to parse the calendarEvents module returned from the Yahoo Finance API call. The calendarEvents module is
        uniquely parsed because it contains two separate pieces of data: The company's earnings events and the company's
        dividends dates. This method will parse the company's earnings dates portion of the calendarEvents.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the calendarEvents module and the earnings submodule. If the module is not found, then it will
        # return None and a YahooModuleNotFoundError.
        try:
            calender_events_earnings = modules_dict[module_name]['earnings']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            if isinstance(calender_events_earnings['earningsDate'], list):
                calender_events_earnings['earningsDate'] = calender_events_earnings['earningsDate'][0]

            calender_events_earnings = self._format_dataframe(calender_events_earnings)
        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return calender_events_earnings, None

    def parse_module_calendar_events_dividends(self, modules_dict, module_name):
        """
        Method to parse the calendarEvents module returned from the Yahoo Finance API call. The calendarEvents module is
        uniquely parsed because it contains two separate pieces of data: The company's earnings events and the company's
        dividends dates. This method will parse the company's dividends dates portion of the calendarEvents.
        :param modules_dict: A dictionary containing all the modules.
        :type modules_dict: dict
        :param module_name: The name of the module to be parsed.
        :type module_name: str
        :return: A tuple containing a dataframe containing the company profile and None, or None and an error.
        :rtype: tuple
        """

        # Attempt to find the calendarEvents module and the dividends submodule. If the module is not found, then it
        # will return None and a YahooModuleNotFoundError.
        try:
            dividends = modules_dict[module_name]

            # Removes the earnings submodule.
            del dividends['earnings']

        except Exception as e:
            return None, YahooExceptions.YahooModuleNotFoundError(e)

        # Attempt to get a formatted dataframe from the module. If there was an error formatting the dataframe, then it
        # will return None and a YahooModuleFormatError.
        try:
            calendar_events_dividends = self._format_dataframe(dividends)

        except Exception as e:
            return None, YahooExceptions.YahooModuleFormatError(e)

        # If the module was found and formatted, then it will return a dataframe containing the company officers
        # information and None since there was no error.
        return calendar_events_dividends, None

    def format_dataframe(self, data_dictionary):
        """
        Method to format the response dictionary from a requested module.
        :param data_dictionary: The dictionary data from the requested module.
        :type data_dictionary: dict
        :return: A formatted dataframe containing the data.
        :rtype pd.Dataframe
        """

        # Checks to see if there are any dictionaries or lists within the data that need to be flattened.
        if isinstance(data_dictionary, list):
            module = [flatten(data) for data in data_dictionary]
            module = pd.DataFrame(module)
        else:
            module = flatten(data_dictionary)
            module = pd.DataFrame([module])

        # Due to the way Yahoo Finance API returns numeric types, the raw integer value is preferred. Therefore, any
        # values with the suffix longfmt (long format) or fmt (format) are removed.
        module_columns = [column for column in module.columns
                          if not ('.fmt' in column or '.longFmt' in column)]

        # Get a new dataframe.
        module = module[module_columns]

        # Format the headers of the column to match PEP8 standards.
        new_columns_dict = {col: self.reader.pep_pattern.sub('_', col.split('.')[0]).lower() for col in
                            module.columns}
        module.rename(columns=new_columns_dict, inplace=True)

        return module
