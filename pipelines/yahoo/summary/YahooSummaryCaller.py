from pipelines.base.BaseReader import BaseReader

import re


class YahooSummaryCaller(BaseReader):
    """
    Class for reading a yahoo Summary from the A.P.I. or from the
    dataset.
    """

    def __init__(self, symbol,
                 include_asset_profile=False,
                 include_income_statement_history=False,
                 include_income_statement_history_quarterly=False,
                 include_balance_sheet_history=False,
                 include_balance_sheet_history_quarterly=False,
                 include_cash_flow_statement_history=False,
                 include_cash_flow_statement_history_quarterly=False,
                 include_earnings=False,
                 include_earnings_history=False,
                 include_financial_data=False,
                 include_default_key_statistics=False,
                 include_institution_ownership=False,
                 include_insider_holders=False,
                 include_insider_transactions=False,
                 include_fund_ownership=False,
                 include_major_direct_holders=False,
                 include_major_direct_holders_breakdown=False,
                 include_recommendation_trend=False,
                 include_earnings_trend=False,
                 include_industry_trend=False,
                 include_index_trend=False,
                 include_sector_trend=False,
                 include_calendar_events=False,
                 include_sec_filings=False,
                 include_upgrade_downgrade_history=False,
                 include_net_share_purchase_activity=False,
                 include_all=False):
        """
        Constructor for the YahooSummaryReader class to read copmany summaries from the yahoo Finance API.
        :param symbol: The company(s) for which summaries are to be retrieved.
        :type symbol: Union[str, list]
        :param include_asset_profile: Include a company's profile and company officer list.
        :type include_asset_profile: bool
        :param include_income_statement_history: Include a company's income statement history?
        :type include_income_statement_history: bool
        :param include_income_statement_history_quarterly: Include a company's quarterly income statement history
        :type include_income_statement_history_quarterly: bool
        :param include_balance_sheet_history: Include a company's balance sheet history.
        :type include_balance_sheet_history: bool
        :param include_balance_sheet_history_quarterly: Include a company's quarterly balance sheet history.
        :type include_balance_sheet_history_quarterly: bool
        :param include_cash_flow_statement_history: Include a company's cash flow statement history.
        :type include_cash_flow_statement_history: bool
        :param include_cash_flow_statement_history_quarterly: Include a company's quarterly cash flow statement history.
        :type include_cash_flow_statement_history_quarterly: bool
        :param include_earnings: Include a company's earnings estimates and financials.
        :type include_earnings: bool
        :param include_earnings_history: Include a company's earnings history.
        :type include_earnings_history: bool
        :param include_financial_data: Include a company's financial pipelines.
        :type include_financial_data: bool
        :param include_default_key_statistics: Include a company's key statistics.
        :type include_default_key_statistics: bool
        :param include_institution_ownership: Include a company's insitutional owners.
        :type include_institution_ownership: bool
        :param include_insider_holders: Include a company's insider holders.
        :type include_insider_holders: bool
        :param include_insider_transactions: Include a company's insider transactions.
        :type include_insider_transactions: bool
        :param include_fund_ownership: Include a company's fund owners.
        :type include_fund_ownership: bool
        :param include_major_direct_holders: Include a company's major direct holders.
        :type include_major_direct_holders: bool
        :param include_major_direct_holders_breakdown: Include a company's major direct holders breakdown.
        :type include_major_direct_holders_breakdown: bool
        :param include_recommendation_trend: Include a company's recommendation trend.
        :type include_recommendation_trend: bool
        :param include_earnings_trend: Include a company's earnings trend.
        :type include_earnings_trend: bool
        :param include_industry_trend: Include a company's industry trend.
        :type include_industry_trend: bool
        :param include_index_trend: Include a company's index trend information and estimates.
        :type include_index_trend: bool
        :param include_sector_trend: Include a company's sector trend.
        :type include_sector_trend: bool
        :param include_calendar_events: Include a company's earnings events and dividends events.
        :type include_calendar_events: bool
        :param include_sec_filings: Include a company's SEC filings history.
        :type include_sec_filings: bool
        :param include_upgrade_downgrade_history: Include a company's upgrade and downgrade history.
        :type include_upgrade_downgrade_history: bool
        :param include_net_share_purchase_activity: Include a company's net purchase activity.
        :type include_net_share_purchase_activity: bool
        :param include_all: Include all available information about the company.
        :type include_all: bool
        """
        # Assign all financial information to the value requested.
        self.include_asset_profile = include_all or include_asset_profile
        self.include_income_statement_history = include_all or include_income_statement_history
        self.include_income_statement_history_quarterly = include_all or include_income_statement_history_quarterly
        self.include_balance_sheet_history = include_all or include_balance_sheet_history
        self.include_balance_sheet_history_quarterly = include_all or include_balance_sheet_history_quarterly
        self.include_cash_flow_statement_history = include_all or include_cash_flow_statement_history
        self.include_cash_flow_statement_history_quarterly = include_all or include_cash_flow_statement_history_quarterly
        self.include_earnings = include_earnings or include_all
        self.include_earnings_history = include_all or include_earnings_history
        self.include_financial_data = include_all or include_financial_data
        self.include_default_key_statistics = include_all or include_default_key_statistics

        # Assign all holders information to the value requested.
        self.include_institution_ownership = include_all or include_institution_ownership
        self.include_insider_holders = include_all or include_insider_holders
        self.include_insider_transactions = include_all or include_insider_transactions
        self.include_fund_ownership = include_all or include_fund_ownership
        self.include_major_direct_holders = include_all or include_major_direct_holders
        self.include_major_direct_holders_breakdown = include_all or include_major_direct_holders_breakdown

        # Assign all trends information to the value requested.
        self.include_recommendation_trend = include_all or include_recommendation_trend
        self.include_earnings_trend = include_all or include_earnings_trend
        self.include_industry_trend = include_all or include_industry_trend
        self.include_index_trend = include_all or include_index_trend
        self.include_sector_trend = include_all or include_sector_trend

        # Assign all non-financial information to the value requested.
        self.include_calendar_events = include_all or include_calendar_events
        self.include_sec_filings = include_all or include_sec_filings
        self.include_upgrade_downgrade_history = include_all or include_upgrade_downgrade_history
        self.include_net_share_purchase_activity = include_all or include_net_share_purchase_activity

        self.include_all = include_all

        # Set the pattern used to define the response dataframe schema formatting.

        # Call the super class's constructor.
        super().__init__(symbol)

    @property
    def url(self):
        """
        Property to get the url for the yahoo Finance summary API. The API needs to be formatted with a symbol.
        :return: A string containing the API url that needs to be formatted.
        :rtype: str
        """

        return 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{}'

    @property
    def params(self):
        """
        Property to get a string containing the comma separated list of parameters for the yahoo Finance summary API.
        :return: A dict containing a modules key with a string containing the comma separated list of parameters value.
        :rtype: dict
        """

        # Set the string list to empty.
        modules_list = ''

        # Check to see which financial parameters need to be included in the string list.
        if self.include_asset_profile:
            modules_list += 'assetProfile,'
        if self.include_income_statement_history:
            modules_list += 'incomeStatementHistory,'
        if self.include_income_statement_history_quarterly:
            modules_list += 'incomeStatementHistoryQuarterly,'
        if self.include_balance_sheet_history:
            modules_list += 'balanceSheetHistory,'
        if self.include_balance_sheet_history_quarterly:
            modules_list += 'balanceSheetHistoryQuarterly,'
        if self.include_cash_flow_statement_history:
            modules_list += 'cashFlowStatementHistory,'
        if self.include_cash_flow_statement_history_quarterly:
            modules_list += 'cashFlowStatementHistoryQuarterly,'
        if self.include_earnings:
            modules_list += 'earnings,'
        if self.include_earnings_history:
            modules_list += 'earningsHistory,'
        if self.include_financial_data:
            modules_list += 'financialData,'
        if self.include_default_key_statistics:
            modules_list += 'defaultKeyStatistics,'

        # Check to see which holders parameters need to be included in the string list.
        if self.include_institution_ownership:
            modules_list += 'institutionOwnership,'
        if self.include_insider_holders:
            modules_list += 'insiderHolders,'
        if self.include_insider_transactions:
            modules_list += 'insiderTransactions,'
        if self.include_fund_ownership:
            modules_list += 'fundOwnership,'
        if self.include_major_direct_holders:
            modules_list += 'majorDirectHolders,'
        if self.include_major_direct_holders_breakdown:
            modules_list += 'majorHoldersBreakdown,'

        # Check to see which trends parameters need to be included in the string list.
        if self.include_recommendation_trend:
            modules_list += 'recommendationTrend,'
        if self.include_earnings_trend:
            modules_list += 'earningsTrend,'
        if self.include_industry_trend:
            modules_list += 'industryTrend,'
        if self.include_index_trend:
            modules_list += 'indexTrend,'
        if self.include_sector_trend:
            modules_list += 'sectorTrend,'

        # Check to see which non-financial parameters need to be included in the string list.
        if self.include_calendar_events:
            modules_list += 'calendarEvents,'
        if self.include_sec_filings:
            modules_list += 'secFilings,'
        if self.include_upgrade_downgrade_history:
            modules_list += 'upgradeDowngradeHistory,'
        if self.include_net_share_purchase_activity:
            modules_list += 'netSharePurchaseActivity,'

        # Create the dict and return it.
        return {'modules': modules_list}

