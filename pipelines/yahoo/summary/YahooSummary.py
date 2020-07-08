from printers.SerialPrinter import SerialPrinter

import os


class YahooSummary:
    """
    A quasi data class used to store mutable values obtained from the
    yahoo! Finance A.P.I..
    """

    def __init__(self, symbol: str):
        """
        Constructor method to create the class. It will set all of the
        class instance variables to none.
        :param symbol: The string symbol for the company.
        """

        self._serial_printer = SerialPrinter()

        self._serial_printer.print_begin('Creating a YahooSummary object...')

        # Save the company's symbol as an instance variable.
        self._serial_printer.print_begin('Creating Yahoo summary instance variables...')
        self._symbol = symbol.lower()
        self._directory = os.getcwd() + '\\data\\' + self._symbol + '\\summary\\'
        self._serial_printer.print_end('Complete!')

        # Set all financial summary data to a default state.
        self._serial_printer.print_begin('Creating financial statement summary datum objects...')
        self._profile = self.Datum(None, 'profile', self._directory + '_profile.csv', ['assetProfile'], ['companyOfficers'], uses_index=False)
        self._company_officers = self.Datum(None, 'company_officers', self._directory + '_company_officers.csv', ['assetProfile', 'companyOfficers'], [], uses_index=False)
        self._income_statements = self.Datum(None, 'income_statements', self._directory + '_income_statements.csv', ['incomeStatementHistory', 'incomeStatementHistory'], [], uses_index=True)
        self._income_statements_quarterly = self.Datum(None, 'income_statements_quarterly', self._directory + '_income_statements_quarterly.csv', ['incomeStatementHistoryQuarterly', 'incomeStatementHistory'], [], uses_index=True)
        self._balance_sheets = self.Datum(None, 'balance_sheets', self._directory + '_balance_sheets.csv', ['balanceSheetHistory', 'balanceSheetStatements'], [], uses_index=True)
        self._balance_sheets_quarterly = self.Datum(None, 'balance_sheets_quarterly', self._directory + '_balance_sheets_quarterly.csv', ['balanceSheetHistoryQuarterly', 'balanceSheetStatements'], [], uses_index=True)
        self._cash_flow_statements = self.Datum(None, 'cash_flow_statements', self._directory + '_cash_flow_statements.csv', ['cashflowStatementHistory', 'cashflowStatements'], [], uses_index=True)
        self._cash_flow_statements_quarterly = self.Datum(None, 'cash_flow_statements_quarterly', self._directory + '_cash_flow_statements_quarterly.csv', ['cashflowStatementHistoryQuarterly', 'cashflowStatements'], [], uses_index=True)
        self._earnings_estimates = self.Datum(None, 'earnings_estimates', self._directory + '_earnings_estimates.csv', ['earnings', 'earningsChart'], ['quarterly'], uses_index=True)
        self._earnings_estimates_quarterly = self.Datum(None, 'earnings_estimates_quarterly', self._directory + '_earnings_estimates_quarterly.csv', ['earnings', 'earningsChart', 'quarterly'], [], uses_index=False)
        self._financials_quarterly = self.Datum(None, 'financials_quarterly', self._directory + '_financials_quarterly.csv', ['earnings', 'financialsChart', 'yearly'], [], uses_index=False)
        self._financials_yearly = self.Datum(None, 'financials_yearly', self._directory + '_financials_yearly.csv',  ['earnings', 'financialsChart', 'quarterly'], [], uses_index=True)
        self._earnings_history = self.Datum(None, 'earnings_history', self._directory + '_earnings_history.csv', ['earningsHistory', 'history'], [], uses_index=False)
        self._financial_data = self.Datum(None, 'financial_data', self._directory + '_financial_data.csv', ['financialData'], [], uses_index=False)
        self._default_key_statistics = self.Datum(None, 'default_key_statistics', self._directory + '_default_key_statistics.csv', ['defaultKeyStatistics'], [], uses_index=False)
        self._serial_printer.print_end('Complete!')

        # Set all holder summary data to a default state.
        self._serial_printer.print_begin('Creating holder summary datum objects...')
        self._institution_ownership = self.Datum(None, 'institution_ownership', self._directory + '_institution_ownership.csv', ['institutionOwnership', 'ownershipList'], [], uses_index=True)
        self._insider_holders = self.Datum(None, 'insider_holders', self._directory + '_insider_holders.csv', ['insiderHolders', 'holders'], [], uses_index=False)
        self._insider_transactions = self.Datum(None, 'insider_transactions', self._directory + '_insider_transactions.csv', ['insiderTransactions', 'transactions'], [],  uses_index=False)
        self._fund_ownership = self.Datum(None, 'fund_ownership', self._directory + '_fund_ownership.csv', ['fundOwnership', 'ownershipList'], [], uses_index=True)
        self._major_direct_holders = self.Datum(None, 'major_direct_holders', self._directory + '_major_direct_holders.csv', ['majorDirectHolders', 'holders'], [], uses_index=False)
        self._major_direct_holders_breakdown = self.Datum(None, 'major_direct_holders_breakdown', self._directory + '_major_direct_holders_breakdown.csv', ['majorHoldersBreakdown'], [], uses_index=False)
        self._serial_printer.print_end('Complete!')

        # Set all trend summary data to a default state.
        self._serial_printer.print_begin('Creating trend summary datum objects...')
        self._recommendation_trend = self.Datum(None, 'recommendation_trend', self._directory + '_recommendation_trend.csv', ['recommendationTrend', 'trend'], [], uses_index=False)
        self._earnings_trend = self.Datum(None, 'earnings_trend', self._directory + '_earnings_trend.csv', ['earningsTrend', 'trend'], [], uses_index=False)
        self._industry_trend = self.Datum(None, 'industry_trend', self._directory + '_industry_trend.csv', ['industryTrend'], ['estimates'], uses_index=False)
        self._index_trend_info = self.Datum(None, 'index_trend_info', self._directory + '_index_trend_info.csv', ['indexTrend'], [], uses_index=False)
        self._index_trend_estimate = self.Datum(None, 'index_trend_estimate', self._directory + '_index_trend_estimate.csv', ['indexTrend', 'estimates'], [], uses_index=False)
        self._sector_trend = self.Datum(None, 'sector_trend', self._directory + '_sector_trend.csv', ['sectorTrend'], [], uses_index=False)
        self._serial_printer.print_end('Complete!')

        # Set all non-financial summary data to a default state.
        self._serial_printer.print_begin('Creating non financial statement summary datum objects...')
        self._calendar_events_earnings = self.Datum(None, 'calendar_events_earnings', self._directory + '_calendar_events_earnings.csv', ['calendarEvents', 'earnings'], [], uses_index=True)
        self._calendar_events_dividends = self.Datum(None, 'calendar_events_dividends', self._directory + '_calendar_events_dividends.csv', ['calendarEvents'], ['earnings'], uses_index=False)
        self._sec_filings = self.Datum(None, 'sec_filings', self._directory + '_sec_filings.csv', ['secFilings', 'filings'], [], uses_index=False)
        self._upgrade_downgrade_history = self.Datum(None, 'upgrade_downgrade_history', self._directory + '_upgrade_downgrade_history.csv', ['upgradeDowngradeHistory', 'history'], [], uses_index=False)
        self._net_share_purchase_activity = self.Datum(None, 'net_share_purchase_activity', self._directory + '_net_share_purchase_activity.csv', ['netSharePurchaseActivity'], [], uses_index=False)
        self._serial_printer.print_end('Complete!')

        self._serial_printer.print_end('Complete!')

    def as_list(self):
        return [self._profile,
                self._company_officers,
                self._income_statements,
                self._income_statements_quarterly,
                self._balance_sheets,
                self._balance_sheets_quarterly,
                self._cash_flow_statements,
                self._cash_flow_statements_quarterly,
                self._earnings_estimates,
                self._earnings_estimates_quarterly,
                self._financials_quarterly,
                self._financials_yearly,
                self._earnings_history,
                self._financial_data,
                self._default_key_statistics,
                self._institution_ownership,
                self._insider_holders,
                self._insider_transactions,
                self._fund_ownership,
                self._major_direct_holders,
                self._major_direct_holders_breakdown,
                self._recommendation_trend,
                self._earnings_trend,
                self._industry_trend,
                self._index_trend_info,
                self._index_trend_estimate,
                self._sector_trend,
                self._calendar_events_earnings,
                self._calendar_events_dividends,
                self._sec_filings,
                self._upgrade_downgrade_history,
                self._net_share_purchase_activity]

    @property
    def profile_path(self):
        """
        A getter method to get the path to the company's profile data.
        """

        return self._profile.path

    @property
    def profile_uses_index(self):
        """
        A getter method to a company's profile data uses an index.
        """

        return self._profile.uses_index

    @property
    def profile_location(self):
        """
        A getter method to get a company's profile location in the data.
        """

        return self._profile.response_location

    @property
    def profile_removables(self):
        """
        A getter method to get a company's profile removable data.
        """

        return self._profile.response_removables

    @property
    def profile(self):
        """
        A getter method to get a company's profile data.
        """

        return self._profile.value

    @profile.setter
    def profile(self, value):
        """
        A setter method to set a company's profile data.
        :param value: The value to be set.
        """

        self._profile.value = value

    @property
    def company_officers_path(self):
        """
        A getter method to get the path to the company's company officers data.
        """

        return self._company_officers.path

    @property
    def company_officers_uses_index(self):
        """
        A getter method to a company's company officers data uses an index.
        """

        return self._company_officers.uses_index

    @property
    def company_officers_location(self):
        """
        A getter method to get a company's company officers location in the data.
        """

        return self._company_officers.response_location

    @property
    def company_officers_removables(self):
        """
        A getter method to get a company's company officers removable data.
        """

        return self._company_officers.response_removables

    @property
    def company_officers(self):
        """
        A getter method to get a company's company officers data.
        """

        return self._company_officers.value

    @company_officers.setter
    def company_officers(self, value):
        """
        A setter method to set a company's company officers data.
        :param value: The value to be set.
        """

        self._company_officers.value = value

    @property
    def income_statements_path(self):
        """
        A getter method to get the path to the company's income statements data.
        """

        return self._income_statements.path

    @property
    def income_statements_uses_index(self):
        """
        A getter method to a company's income statements data uses an index.
        """

        return self._income_statements.uses_index

    @property
    def income_statements_location(self):
        """
        A getter method to get a company's income statements location in the data.
        """

        return self._income_statements.response_location

    @property
    def income_statements_removables(self):
        """
        A getter method to get a company's income statements removable data.
        """

        return self._income_statements.response_removables

    @property
    def income_statements(self):
        """
        A getter method to get a company's income statements data.
        """

        return self._income_statements.value

    @income_statements.setter
    def income_statements(self, value):
        """
        A setter method to set a company's income statements data.
        :param value: The value to be set.
        """

        self._income_statements.value = value

    @property
    def income_statements_quarterly_path(self):
        """
        A getter method to get the path to the company's income statements quarterly data.
        """

        return self._income_statements_quarterly.path

    @property
    def income_statements_quarterly_uses_index(self):
        """
        A getter method to a company's income statements quarterly data uses an index.
        """

        return self._income_statements_quarterly.uses_index

    @property
    def income_statements_quarterly_location(self):
        """
        A getter method to get a company's income statements quarterly location in the data.
        """

        return self._income_statements_quarterly.response_location

    @property
    def income_statements_quarterly_removables(self):
        """
        A getter method to get a company's income statements quarterly removable data.
        """

        return self._income_statements_quarterly.response_removables

    @property
    def income_statements_quarterly(self):
        """
        A getter method to get a company's income statements quarterly data.
        """

        return self._income_statements_quarterly.value

    @income_statements_quarterly.setter
    def income_statements_quarterly(self, value):
        """
        A setter method to set a company's income statements quarterly data.
        :param value: The value to be set.
        """

        self._income_statements_quarterly.value = value

    @property
    def balance_sheets_path(self):
        """
        A getter method to get the path to the company's balance sheets data.
        """

        return self._balance_sheets.path

    @property
    def balance_sheets_uses_index(self):
        """
        A getter method to a company's balance sheets data uses an index.
        """

        return self._balance_sheets.uses_index

    @property
    def balance_sheets_location(self):
        """
        A getter method to get a company's balance sheets location in the data.
        """

        return self._balance_sheets.response_location

    @property
    def balance_sheets_removables(self):
        """
        A getter method to get a company's balance sheets removable data.
        """

        return self._balance_sheets.response_removables

    @property
    def balance_sheets(self):
        """
        A getter method to get a company's balance sheets data.
        """

        return self._balance_sheets.value

    @balance_sheets.setter
    def balance_sheets(self, value):
        """
        A setter method to set a company's balance sheets data.
        :param value: The value to be set.
        """

        self._balance_sheets.value = value

    @property
    def balance_sheets_quarterly_path(self):
        """
        A getter method to get the path to the company's balance sheets quarterly data.
        """

        return self._balance_sheets_quarterly.path

    @property
    def balance_sheets_quarterly_uses_index(self):
        """
        A getter method to a company's balance sheets quarterly data uses an index.
        """

        return self._balance_sheets_quarterly.uses_index

    @property
    def balance_sheets_quarterly_location(self):
        """
        A getter method to get a company's balance sheets quarterly location in the data.
        """

        return self._balance_sheets_quarterly.response_location

    @property
    def balance_sheets_quarterly_removables(self):
        """
        A getter method to get a company's balance sheets quarterly removable data.
        """

        return self._balance_sheets_quarterly.response_removables

    @property
    def balance_sheets_quarterly(self):
        """
        A getter method to get a company's balance sheets quarterly data.
        """

        return self._balance_sheets_quarterly.value

    @balance_sheets_quarterly.setter
    def balance_sheets_quarterly(self, value):
        """
        A setter method to set a company's balance sheets quarterly data.
        :param value: The value to be set.
        """

        self._balance_sheets_quarterly.value = value

    @property
    def cash_flow_statements_path(self):
        """
        A getter method to get the path to the company's cash flow statements data.
        """

        return self._cash_flow_statements.path

    @property
    def cash_flow_statements_uses_index(self):
        """
        A getter method to a company's cash flow statements data uses an index.
        """

        return self._cash_flow_statements.uses_index

    @property
    def cash_flow_statements_location(self):
        """
        A getter method to get a company's cash flow statements location in the data.
        """

        return self._cash_flow_statements.response_location

    @property
    def cash_flow_statements_removables(self):
        """
        A getter method to get a company's cash flow statements removable data.
        """

        return self._cash_flow_statements.response_removables

    @property
    def cash_flow_statements(self):
        """
        A getter method to get a company's cash flow statements data.
        """

        return self._cash_flow_statements.value

    @cash_flow_statements.setter
    def cash_flow_statements(self, value):
        """
        A setter method to set a company's cash flow statements data.
        :param value: The value to be set.
        """

        self._cash_flow_statements.value = value

    @property
    def cash_flow_statements_quarterly_path(self):
        """
        A getter method to get the path to the company's cash flow statements quarterly data.
        """

        return self._cash_flow_statements_quarterly.path

    @property
    def cash_flow_statements_quarterly_uses_index(self):
        """
        A getter method to a company's cash flow statements quarterly data uses an index.
        """

        return self._cash_flow_statements_quarterly.uses_index

    @property
    def cash_flow_statements_quarterly_location(self):
        """
        A getter method to get a company's cash flow statements quarterly location in the data.
        """

        return self._cash_flow_statements_quarterly.response_location

    @property
    def cash_flow_statements_quarterly_removables(self):
        """
        A getter method to get a company's cash flow statements quarterly removable data.
        """

        return self._cash_flow_statements_quarterly.response_removables

    @property
    def cash_flow_statements_quarterly(self):
        """
        A getter method to get a company's cash flow statements quarterly data.
        """

        return self._cash_flow_statements_quarterly.value

    @cash_flow_statements_quarterly.setter
    def cash_flow_statements_quarterly(self, value):
        """
        A setter method to set a company's cash flow statements quarterly data.
        :param value: The value to be set.
        """

        self._cash_flow_statements_quarterly.value = value

    @property
    def earnings_estimates_path(self):
        """
        A getter method to get the path to the company's earnings estimates data.
        """

        return self._earnings_estimates.path

    @property
    def earnings_estimates_uses_index(self):
        """
        A getter method to a company's earnings estimates data uses an index.
        """

        return self._earnings_estimates.uses_index

    @property
    def earnings_estimates_location(self):
        """
        A getter method to get a company's earnings estimates location in the data.
        """

        return self._earnings_estimates.response_location

    @property
    def earnings_estimates_removables(self):
        """
        A getter method to get a company's earnings estimates removable data.
        """

        return self._earnings_estimates.response_removables

    @property
    def earnings_estimates(self):
        """
        A getter method to get a company's earnings estimates data.
        """

        return self._earnings_estimates.value

    @earnings_estimates.setter
    def earnings_estimates(self, value):
        """
        A setter method to set a company's earnings estimates data.
        :param value: The value to be set.
        """

        self._earnings_estimates.value = value

    @property
    def earnings_estimates_quarterly_path(self):
        """
        A getter method to get the path to the company's earnings estimates quarterly data.
        """

        return self._earnings_estimates_quarterly.path

    @property
    def earnings_estimates_quarterly_uses_index(self):
        """
        A getter method to a company's earnings estimates quarterly data uses an index.
        """

        return self._earnings_estimates_quarterly.uses_index

    @property
    def earnings_estimates_quarterly_location(self):
        """
        A getter method to get a company's earnings estimates quarterly location in the data.
        """

        return self._earnings_estimates_quarterly.response_location

    @property
    def earnings_estimates_quarterly_removables(self):
        """
        A getter method to get a company's earnings estimates quarterly removable data.
        """

        return self._earnings_estimates_quarterly.response_removables

    @property
    def earnings_estimates_quarterly(self):
        """
        A getter method to get a company's earnings estimates quarterly data.
        """

        return self._earnings_estimates_quarterly.value

    @earnings_estimates_quarterly.setter
    def earnings_estimates_quarterly(self, value):
        """
        A setter method to set a company's earnings estimates quarterly data.
        :param value: The value to be set.
        """

        self._earnings_estimates_quarterly.value = value

    @property
    def financials_quarterly_path(self):
        """
        A getter method to get the path to the company's financials quarterly data.
        """

        return self._financials_quarterly.path

    @property
    def financials_quarterly_uses_index(self):
        """
        A getter method to a company's financials quarterly data uses an index.
        """

        return self._financials_quarterly.uses_index

    @property
    def financials_quarterly_location(self):
        """
        A getter method to get a company's financials quarterly location in the data.
        """

        return self._financials_quarterly.response_location

    @property
    def financials_quarterly_removables(self):
        """
        A getter method to get a company's financials quarterly removable data.
        """

        return self._financials_quarterly.response_removables

    @property
    def financials_quarterly(self):
        """
        A getter method to get a company's financials quarterly data.
        """

        return self._financials_quarterly.value

    @financials_quarterly.setter
    def financials_quarterly(self, value):
        """
        A setter method to set a company's financials quarterly data.
        :param value: The value to be set.
        """

        self._financials_quarterly.value = value

    @property
    def financials_yearly_path(self):
        """
        A getter method to get the path to the company's financials yearly data.
        """

        return self._financials_yearly.path

    @property
    def financials_yearly_uses_index(self):
        """
        A getter method to a company's financials yearly data uses an index.
        """

        return self._financials_yearly.uses_index

    @property
    def financials_yearly_location(self):
        """
        A getter method to get a company's financials yearly location in the data.
        """

        return self._financials_yearly.response_location

    @property
    def financials_yearly_removables(self):
        """
        A getter method to get a company's financials yearly removable data.
        """

        return self._financials_yearly.response_removables

    @property
    def financials_yearly(self):
        """
        A getter method to get a company's financials yearly data.
        """

        return self._financials_yearly.value

    @financials_yearly.setter
    def financials_yearly(self, value):
        """
        A setter method to set a company's financials yearly data.
        :param value: The value to be set.
        """

        self._financials_yearly.value = value

    @property
    def earnings_history_path(self):
        """
        A getter method to get the path to the company's earnings history data.
        """

        return self._earnings_history.path

    @property
    def earnings_history_uses_index(self):
        """
        A getter method to a company's earnings history data uses an index.
        """

        return self._earnings_history.uses_index

    @property
    def earnings_history_location(self):
        """
        A getter method to get a company's earnings history location in the data.
        """

        return self._earnings_history.response_location

    @property
    def earnings_history_removables(self):
        """
        A getter method to get a company's earnings history removable data.
        """

        return self._earnings_history.response_removables

    @property
    def earnings_history(self):
        """
        A getter method to get a company's earnings history data.
        """

        return self._earnings_history.value

    @earnings_history.setter
    def earnings_history(self, value):
        """
        A setter method to set a company's earnings history data.
        :param value: The value to be set.
        """

        self._earnings_history.value = value

    @property
    def financial_data_path(self):
        """
        A getter method to get the path to the company's financial data data.
        """

        return self._financial_data.path

    @property
    def financial_data_uses_index(self):
        """
        A getter method to a company's financial data data uses an index.
        """

        return self._financial_data.uses_index

    @property
    def financial_data_location(self):
        """
        A getter method to get a company's financial data location in the data.
        """

        return self._financial_data.response_location

    @property
    def financial_data_removables(self):
        """
        A getter method to get a company's financial data removable data.
        """

        return self._financial_data.response_removables

    @property
    def financial_data(self):
        """
        A getter method to get a company's financial data data.
        """

        return self._financial_data.value

    @financial_data.setter
    def financial_data(self, value):
        """
        A setter method to set a company's financial data data.
        :param value: The value to be set.
        """

        self._financial_data.value = value

    @property
    def default_key_statistics_path(self):
        """
        A getter method to get the path to the company's default key statistics data.
        """

        return self._default_key_statistics.path

    @property
    def default_key_statistics_uses_index(self):
        """
        A getter method to a company's default key statistics data uses an index.
        """

        return self._default_key_statistics.uses_index

    @property
    def default_key_statistics_location(self):
        """
        A getter method to get a company's default key statistics location in the data.
        """

        return self._default_key_statistics.response_location

    @property
    def default_key_statistics_removables(self):
        """
        A getter method to get a company's default key statistics removable data.
        """

        return self._default_key_statistics.response_removables

    @property
    def default_key_statistics(self):
        """
        A getter method to get a company's default key statistics data.
        """

        return self._default_key_statistics.value

    @default_key_statistics.setter
    def default_key_statistics(self, value):
        """
        A setter method to set a company's default key statistics data.
        :param value: The value to be set.
        """

        self._default_key_statistics.value = value

    @property
    def institution_ownership_path(self):
        """
        A getter method to get the path to the company's institution ownership data.
        """

        return self._institution_ownership.path

    @property
    def institution_ownership_uses_index(self):
        """
        A getter method to a company's institution ownership data uses an index.
        """

        return self._institution_ownership.uses_index

    @property
    def institution_ownership_location(self):
        """
        A getter method to get a company's institution ownership location in the data.
        """

        return self._institution_ownership.response_location

    @property
    def institution_ownership_removables(self):
        """
        A getter method to get a company's institution ownership removable data.
        """

        return self._institution_ownership.response_removables

    @property
    def institution_ownership(self):
        """
        A getter method to get a company's institution ownership data.
        """

        return self._institution_ownership.value

    @institution_ownership.setter
    def institution_ownership(self, value):
        """
        A setter method to set a company's institution ownership data.
        :param value: The value to be set.
        """

        self._institution_ownership.value = value

    @property
    def insider_holders_path(self):
        """
        A getter method to get the path to the company's insider holders data.
        """

        return self._insider_holders.path

    @property
    def insider_holders_uses_index(self):
        """
        A getter method to a company's insider holders data uses an index.
        """

        return self._insider_holders.uses_index

    @property
    def insider_holders_location(self):
        """
        A getter method to get a company's insider holders location in the data.
        """

        return self._insider_holders.response_location

    @property
    def insider_holders_removables(self):
        """
        A getter method to get a company's insider holders removable data.
        """

        return self._insider_holders.response_removables

    @property
    def insider_holders(self):
        """
        A getter method to get a company's insider holders data.
        """

        return self._insider_holders.value

    @insider_holders.setter
    def insider_holders(self, value):
        """
        A setter method to set a company's insider holders data.
        :param value: The value to be set.
        """

        self._insider_holders.value = value

    @property
    def insider_transactions_path(self):
        """
        A getter method to get the path to the company's insider transactions data.
        """

        return self._insider_transactions.path

    @property
    def insider_transactions_uses_index(self):
        """
        A getter method to a company's insider transactions data uses an index.
        """

        return self._insider_transactions.uses_index

    @property
    def insider_transactions_location(self):
        """
        A getter method to get a company's insider transactions location in the data.
        """

        return self._insider_transactions.response_location

    @property
    def insider_transactions_removables(self):
        """
        A getter method to get a company's insider transactions removable data.
        """

        return self._insider_transactions.response_removables

    @property
    def insider_transactions(self):
        """
        A getter method to get a company's insider transactions data.
        """

        return self._insider_transactions.value

    @insider_transactions.setter
    def insider_transactions(self, value):
        """
        A setter method to set a company's insider transactions data.
        :param value: The value to be set.
        """

        self._insider_transactions.value = value

    @property
    def fund_ownership_path(self):
        """
        A getter method to get the path to the company's fund ownership data.
        """

        return self._fund_ownership.path

    @property
    def fund_ownership_uses_index(self):
        """
        A getter method to a company's fund ownership data uses an index.
        """

        return self._fund_ownership.uses_index

    @property
    def fund_ownership_location(self):
        """
        A getter method to get a company's fund ownership location in the data.
        """

        return self._fund_ownership.response_location

    @property
    def fund_ownership_removables(self):
        """
        A getter method to get a company's fund ownership removable data.
        """

        return self._fund_ownership.response_removables

    @property
    def fund_ownership(self):
        """
        A getter method to get a company's fund ownership data.
        """

        return self._fund_ownership.value

    @fund_ownership.setter
    def fund_ownership(self, value):
        """
        A setter method to set a company's fund ownership data.
        :param value: The value to be set.
        """

        self._fund_ownership.value = value

    @property
    def major_direct_holders_path(self):
        """
        A getter method to get the path to the company's major direct holders data.
        """

        return self._major_direct_holders.path

    @property
    def major_direct_holders_uses_index(self):
        """
        A getter method to a company's major direct holders data uses an index.
        """

        return self._major_direct_holders.uses_index

    @property
    def major_direct_holders_location(self):
        """
        A getter method to get a company's major direct holders location in the data.
        """

        return self._major_direct_holders.response_location

    @property
    def major_direct_holders_removables(self):
        """
        A getter method to get a company's major direct holders removable data.
        """

        return self._major_direct_holders.response_removables

    @property
    def major_direct_holders(self):
        """
        A getter method to get a company's major direct holders data.
        """

        return self._major_direct_holders.value

    @major_direct_holders.setter
    def major_direct_holders(self, value):
        """
        A setter method to set a company's major direct holders data.
        :param value: The value to be set.
        """

        self._major_direct_holders.value = value

    @property
    def major_direct_holders_breakdown_path(self):
        """
        A getter method to get the path to the company's major direct holders breakdown data.
        """

        return self._major_direct_holders_breakdown.path

    @property
    def major_direct_holders_breakdown_uses_index(self):
        """
        A getter method to a company's major direct holders breakdown data uses an index.
        """

        return self._major_direct_holders_breakdown.uses_index

    @property
    def major_direct_holders_breakdown_location(self):
        """
        A getter method to get a company's major direct holders breakdown location in the data.
        """

        return self._major_direct_holders_breakdown.response_location

    @property
    def major_direct_holders_breakdown_removables(self):
        """
        A getter method to get a company's major direct holders breakdown removable data.
        """

        return self._major_direct_holders_breakdown.response_removables

    @property
    def major_direct_holders_breakdown(self):
        """
        A getter method to get a company's major direct holders breakdown data.
        """

        return self._major_direct_holders_breakdown.value

    @major_direct_holders_breakdown.setter
    def major_direct_holders_breakdown(self, value):
        """
        A setter method to set a company's major direct holders breakdown data.
        :param value: The value to be set.
        """

        self._major_direct_holders_breakdown.value = value

    @property
    def recommendation_trend_path(self):
        """
        A getter method to get the path to the company's recommendation trend data.
        """

        return self._recommendation_trend.path

    @property
    def recommendation_trend_uses_index(self):
        """
        A getter method to a company's recommendation trend data uses an index.
        """

        return self._recommendation_trend.uses_index

    @property
    def recommendation_trend_location(self):
        """
        A getter method to get a company's recommendation trend location in the data.
        """

        return self._recommendation_trend.response_location

    @property
    def recommendation_trend_removables(self):
        """
        A getter method to get a company's recommendation trend removable data.
        """

        return self._recommendation_trend.response_removables

    @property
    def recommendation_trend(self):
        """
        A getter method to get a company's recommendation trend data.
        """

        return self._recommendation_trend.value

    @recommendation_trend.setter
    def recommendation_trend(self, value):
        """
        A setter method to set a company's recommendation trend data.
        :param value: The value to be set.
        """

        self._recommendation_trend.value = value

    @property
    def earnings_trend_path(self):
        """
        A getter method to get the path to the company's earnings trend data.
        """

        return self._earnings_trend.path

    @property
    def earnings_trend_uses_index(self):
        """
        A getter method to a company's earnings trend data uses an index.
        """

        return self._earnings_trend.uses_index

    @property
    def earnings_trend_location(self):
        """
        A getter method to get a company's earnings trend location in the data.
        """

        return self._earnings_trend.response_location

    @property
    def earnings_trend_removables(self):
        """
        A getter method to get a company's earnings trend removable data.
        """

        return self._earnings_trend.response_removables

    @property
    def earnings_trend(self):
        """
        A getter method to get a company's earnings trend data.
        """

        return self._earnings_trend.value

    @earnings_trend.setter
    def earnings_trend(self, value):
        """
        A setter method to set a company's earnings trend data.
        :param value: The value to be set.
        """

        self._earnings_trend.value = value

    @property
    def industry_trend_path(self):
        """
        A getter method to get the path to the company's industry trend data.
        """

        return self._industry_trend.path

    @property
    def industry_trend_uses_index(self):
        """
        A getter method to a company's industry trend data uses an index.
        """

        return self._industry_trend.uses_index

    @property
    def industry_trend_location(self):
        """
        A getter method to get a company's industry trend location in the data.
        """

        return self._industry_trend.response_location

    @property
    def industry_trend_removables(self):
        """
        A getter method to get a company's industry trend removable data.
        """

        return self._industry_trend.response_removables

    @property
    def industry_trend(self):
        """
        A getter method to get a company's industry trend data.
        """

        return self._industry_trend.value

    @industry_trend.setter
    def industry_trend(self, value):
        """
        A setter method to set a company's industry trend data.
        :param value: The value to be set.
        """

        self._industry_trend.value = value

    @property
    def index_trend_info_path(self):
        """
        A getter method to get the path to the company's index trend info data.
        """

        return self._index_trend_info.path

    @property
    def index_trend_info_uses_index(self):
        """
        A getter method to a company's index trend info data uses an index.
        """

        return self._index_trend_info.uses_index

    @property
    def index_trend_info_location(self):
        """
        A getter method to get a company's index trend info location in the data.
        """

        return self._index_trend_info.response_location

    @property
    def index_trend_info_removables(self):
        """
        A getter method to get a company's index trend info removable data.
        """

        return self._index_trend_info.response_removables

    @property
    def index_trend_info(self):
        """
        A getter method to get a company's index trend info data.
        """

        return self._index_trend_info.value

    @index_trend_info.setter
    def index_trend_info(self, value):
        """
        A setter method to set a company's index trend info data.
        :param value: The value to be set.
        """

        self._index_trend_info.value = value

    @property
    def index_trend_estimate_path(self):
        """
        A getter method to get the path to the company's index trend estimate data.
        """

        return self._index_trend_estimate.path

    @property
    def index_trend_estimate_uses_index(self):
        """
        A getter method to a company's index trend estimate data uses an index.
        """

        return self._index_trend_estimate.uses_index

    @property
    def index_trend_estimate_location(self):
        """
        A getter method to get a company's index trend estimate location in the data.
        """

        return self._index_trend_estimate.response_location

    @property
    def index_trend_estimate_removables(self):
        """
        A getter method to get a company's index trend estimate removable data.
        """

        return self._index_trend_estimate.response_removables

    @property
    def index_trend_estimate(self):
        """
        A getter method to get a company's index trend estimate data.
        """

        return self._index_trend_estimate.value

    @index_trend_estimate.setter
    def index_trend_estimate(self, value):
        """
        A setter method to set a company's index trend estimate data.
        :param value: The value to be set.
        """

        self._index_trend_estimate.value = value

    @property
    def sector_trend_path(self):
        """
        A getter method to get the path to the company's sector trend data.
        """

        return self._sector_trend.path

    @property
    def sector_trend_uses_index(self):
        """
        A getter method to a company's sector trend data uses an index.
        """

        return self._sector_trend.uses_index

    @property
    def sector_trend_location(self):
        """
        A getter method to get a company's sector trend location in the data.
        """

        return self._sector_trend.response_location

    @property
    def sector_trend_removables(self):
        """
        A getter method to get a company's sector trend removable data.
        """

        return self._sector_trend.response_removables

    @property
    def sector_trend(self):
        """
        A getter method to get a company's sector trend data.
        """

        return self._sector_trend.value

    @sector_trend.setter
    def sector_trend(self, value):
        """
        A setter method to set a company's sector trend data.
        :param value: The value to be set.
        """

        self._sector_trend.value = value

    @property
    def calendar_events_earnings_path(self):
        """
        A getter method to get the path to the company's calendar events earnings data.
        """

        return self._calendar_events_earnings.path

    @property
    def calendar_events_earnings_uses_index(self):
        """
        A getter method to a company's calendar events earnings data uses an index.
        """

        return self._calendar_events_earnings.uses_index

    @property
    def calendar_events_earnings_location(self):
        """
        A getter method to get a company's calendar events earnings location in the data.
        """

        return self._calendar_events_earnings.response_location

    @property
    def calendar_events_earnings_removables(self):
        """
        A getter method to get a company's calendar events earnings removable data.
        """

        return self._calendar_events_earnings.response_removables

    @property
    def calendar_events_earnings(self):
        """
        A getter method to get a company's calendar events earnings data.
        """

        return self._calendar_events_earnings.value

    @calendar_events_earnings.setter
    def calendar_events_earnings(self, value):
        """
        A setter method to set a company's calendar events earnings data.
        :param value: The value to be set.
        """

        self._calendar_events_earnings.value = value

    @property
    def calendar_events_dividends_path(self):
        """
        A getter method to get the path to the company's calendar events dividends data.
        """

        return self._calendar_events_dividends.path

    @property
    def calendar_events_dividends_uses_index(self):
        """
        A getter method to a company's calendar events dividends data uses an index.
        """

        return self._calendar_events_dividends.uses_index

    @property
    def calendar_events_dividends_location(self):
        """
        A getter method to get a company's calendar events dividends location in the data.
        """

        return self._calendar_events_dividends.response_location

    @property
    def calendar_events_dividends_removables(self):
        """
        A getter method to get a company's calendar events dividends removable data.
        """

        return self._calendar_events_dividends.response_removables

    @property
    def calendar_events_dividends(self):
        """
        A getter method to get a company's calendar events dividends data.
        """

        return self._calendar_events_dividends.value

    @calendar_events_dividends.setter
    def calendar_events_dividends(self, value):
        """
        A setter method to set a company's calendar events dividends data.
        :param value: The value to be set.
        """

        self._calendar_events_dividends.value = value

    @property
    def sec_filings_path(self):
        """
        A getter method to get the path to the company's sec filings data.
        """

        return self._sec_filings.path

    @property
    def sec_filings_uses_index(self):
        """
        A getter method to a company's sec filings data uses an index.
        """

        return self._sec_filings.uses_index

    @property
    def sec_filings_location(self):
        """
        A getter method to get a company's sec filings location in the data.
        """

        return self._sec_filings.response_location

    @property
    def sec_filings_removables(self):
        """
        A getter method to get a company's sec filings removable data.
        """

        return self._sec_filings.response_removables

    @property
    def sec_filings(self):
        """
        A getter method to get a company's sec filings data.
        """

        return self._sec_filings.value

    @sec_filings.setter
    def sec_filings(self, value):
        """
        A setter method to set a company's sec filings data.
        :param value: The value to be set.
        """

        self._sec_filings.value = value

    @property
    def upgrade_downgrade_history_path(self):
        """
        A getter method to get the path to the company's upgrade downgrade history data.
        """

        return self._upgrade_downgrade_history.path

    @property
    def upgrade_downgrade_history_uses_index(self):
        """
        A getter method to a company's upgrade downgrade history data uses an index.
        """

        return self._upgrade_downgrade_history.uses_index

    @property
    def upgrade_downgrade_history_location(self):
        """
        A getter method to get a company's upgrade downgrade history location in the data.
        """

        return self._upgrade_downgrade_history.response_location

    @property
    def upgrade_downgrade_history_removables(self):
        """
        A getter method to get a company's upgrade downgrade history removable data.
        """

        return self._upgrade_downgrade_history.response_removables

    @property
    def upgrade_downgrade_history(self):
        """
        A getter method to get a company's upgrade downgrade history data.
        """

        return self._upgrade_downgrade_history.value

    @upgrade_downgrade_history.setter
    def upgrade_downgrade_history(self, value):
        """
        A setter method to set a company's upgrade downgrade history data.
        :param value: The value to be set.
        """

        self._upgrade_downgrade_history.value = value

    @property
    def net_share_purchase_activity_path(self):
        """
        A getter method to get the path to the company's net share purchase activity data.
        """

        return self._net_share_purchase_activity.path

    @property
    def net_share_purchase_activity_uses_index(self):
        """
        A getter method to a company's net share purchase activity data uses an index.
        """

        return self._net_share_purchase_activity.uses_index

    @property
    def net_share_purchase_activity_location(self):
        """
        A getter method to get a company's net share purchase activity location in the data.
        """

        return self._net_share_purchase_activity.response_location

    @property
    def net_share_purchase_activity_removables(self):
        """
        A getter method to get a company's net share purchase activity removable data.
        """

        return self._net_share_purchase_activity.response_removables

    @property
    def net_share_purchase_activity(self):
        """
        A getter method to get a company's net share purchase activity data.
        """

        return self._net_share_purchase_activity.value

    @net_share_purchase_activity.setter
    def net_share_purchase_activity(self, value):
        """
        A setter method to set a company's net share purchase activity data.
        :param value: The value to be set.
        """

        self._net_share_purchase_activity.value = value
        
        
    class Datum:
        def __init__(self, value, title, path,
                     response_location, response_removables, uses_index):
            self._value = value
            self._title = title
            self._path = path
            self._uses_index = uses_index
            self._response_location = response_location
            self._response_removables = response_removables
        
        @property
        def value(self):
            return self._value
        
        @value.setter
        def value(self, value):
            self._value = value
            
        @property
        def title(self):
            return self._title
        
        @property
        def path(self):
            return self._path

        @property
        def uses_index(self):
            return self._uses_index

        @property
        def response_location(self):
            return self._response_location

        @property
        def response_removables(self):
            return self._response_removables


# for value in YahooSummary('aapl').as_list():
#     print('@property')
#     print('def {:}_path(self):'.format(value.title))
#     print('\t"""')
#     print(
#         '\tA getter method to get the path to the company\'s {:} data.'.format(
#             value.title.replace('_', ' ')))
#     print('\t"""')
#
#     print('')
#     print('\treturn self._{:}.path'.format(value.title))
#     print('')
#
#     print('@property')
#     print('def {:}_uses_index(self):'.format(value.title))
#     print('\t"""')
#     print(
#         '\tA getter method to a company\'s {:} data uses an index.'.format(
#             value.title.replace('_', ' ')))
#     print('\t"""')
#
#     print('')
#     print('\treturn self._{:}.uses_index'.format(value.title))
#     print('')
#
#     print('@property')
#     print('def {:}_location(self):'.format(value.title))
#     print('\t"""')
#     print(
#         '\tA getter method to get a company\'s {:} location in the data.'.format(
#             value.title.replace('_', ' ')))
#     print('\t"""')
#
#     print('')
#     print('\treturn self._{:}.response_location'.format(value.title))
#     print('')
#
#     print('@property')
#     print('def {:}_removables(self):'.format(value.title))
#     print('\t"""')
#     print('\tA getter method to get a company\'s {:} removable data.'.format(
#         value.title.replace('_', ' ')))
#     print('\t"""')
#
#     print('')
#     print('\treturn self._{:}.removables'.format(value.title))
#     print('')
#
#     print('@property')
#     print('def {:}(self):'.format(value.title))
#     print('\t"""')
#     print('\tA getter method to get a company\'s {:} data.'.format(
#         value.title.replace('_', ' ')))
#     print('\t"""')
#
#     print('')
#     print('\treturn self._{:}.value'.format(value.title))
#     print('')
#
#     print('@{:}.setter'.format(value.title))
#     print('def {:}(self, value):'.format(value.title))
#     print('\t"""')
#     print('\tA setter method to set a company\'s {:} data.'.format(
#         value.title.replace('_', ' ')))
#     print('\t:param value: The value to be set.')
#     print('\t"""')
#
#     print('')
#     print('\tself._{:}.value = value'.format(value.title))
#     print('')
        
        
        

