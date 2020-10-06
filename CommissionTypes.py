import backtrader as bt


class FixedAndPercentCommission(bt.CommInfoBase):
    params = (
        ('stocklike', True),
        ('commission', 0.0003),
        ('commission_fixed', 2.0),
        ('percabs', True),
    )

    def _getcommission(self, size, price, pseudoexec):
        return self.p.commission_fixed + abs(size) * price * self.p.commission


DeGiroCommission = FixedAndPercentCommission(commission=0.0003, commission_fixed=2.0)
