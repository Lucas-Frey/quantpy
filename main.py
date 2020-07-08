from pipelines.yahoo.summary.YahooSummary import YahooSummary
from pipelines.yahoo.quote.YahooQuote import YahooQuote
from pipelines.yahoo.summary.YahooSummaryCaller import YahooSummaryCaller
from pipelines.yahoo.summary.YahooSummaryProcessor import YahooSummaryProcessor
from pipelines.yahoo.summary.YahooSummaryWriter import YahooSummaryWriter

from printers.SerialPrinter import SerialPrinter
import os

import datetime

if __name__ == '__main__':
    banner = '+{:-<118}+'.format('')
    message = '| {:<116} |'.format('Welcome,')

    now = datetime.datetime.now()

    print(banner)
    print('| {:<116} |'.format('Welcome,'))
    print('| {:<116} |'.format(''))
    print('| {:<116} |'.format('The time is {:}:{:} (CST). This makes it {:} hours since your last login. Please note, there may be dataset'.format(now.hour, now.minute, format(str(12)))))
    print('| {:<116} |'.format('updates that need to be performed before any algorithmic development can be correctly completed. However, you may'))
    print('| {:<116} |'.format('choose any of the following command areas to get started with algorthmic trading.'))
    print('| {:<116} |'.format(''))
    print('| {:<116} |'.format('Best,'))
    print('| {:<116} |'.format(''))
    print('| {:<116} |'.format('Quantpy'))

    print('+{:-<39}+{:-<39}+{:-<38}+'.format('','',''))
    print('| {:<37} | {:<37} | {:<36} |'.format('Dataset Maintenance Panel (1)', 'Strategy Development Panel (2)', 'Twitter Panel (3)'))
    print('+{:-<39}+{:-<39}+{:-<38}+'.format('', '', ''))
    print('| {:<37} | {:<37} | {:<36} |'.format('Dataset diagnostics:', 'Strategy Diagnostics:', 'Twitter Diagnostics:'))
    print('| {:<37} | {:<37} | {:<36} |'.format('- Companies: ', '- Indicators: ', '- Tweets: '))
    print('| {:<37} | {:<37} | {:<36} |'.format('- Last Updated: ', '- Strategies: ', '- Last Tweet: '))
    print('| {:<37} | {:<37} | {:<36} |'.format('- Sources: ', '- Strategies Tested: ', '- Followers: '))
    print('| {:<37} | {:<37} | {:<36} |'.format('- Yahoo Connection: ', '- Strategies Passed: ', '- Messages: '))
    print('| {:<37} | {:<37} | {:<36} |'.format('', '- Strategies Failed: ', ''))
    print('+{:-<39}+{:-<39}+{:-<38}+'.format('', '', ''))