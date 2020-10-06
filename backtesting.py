import datetime

import backtrader as bt
from CommissionTypes import DeGiroCommission
import strats
from matplotlib import dates

if __name__ == '__main__':
    # Init cerebro
    cerebro = bt.Cerebro()
    cerebro.broker.set_cash(50000)
    cerebro.broker.addcommissioninfo(DeGiroCommission)

    # add strat
    cerebro.addstrategy(strats.TestStrategy)
    cerebro.addstrategy(strats.BuyAndHold)
    #
    cerebro.addsizer(bt.sizers.PercentSizer, percents=80)
    # cerebro.addsizer(bt.sizers.FixedSize, stake=1)

    # add data
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime(2019, 12, 31)
    data = bt.feeds.GenericCSVData(dataname="data\\daily\\FLOW.AS.csv",
                                   dtformat=('%Y-%m-%d'),
                                   volume=6, openinterest=-1,
                                   fromdate=start,
                                   todate=end)
    # data = bt.feeds.YahooFinanceData(dataname="IAEX.AS", fromdate=start, todate=end)
    cerebro.adddata(data)
    # cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, data=data)
    # cerebro.addanalyzer(bt.analyzers.TimeReturn, data=data)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot(start=start, end=end)
