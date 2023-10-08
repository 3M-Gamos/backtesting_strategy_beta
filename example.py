import sys
print(sys.executable)
from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover
import talib
class RsiOscillator(Strategy):
    upper_bound= 70
    lower_bound= 30
    def init(self):
        self.rsi=self.I(talib.RSI, self.data.Close, 14)
    def next(self):
        
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()
bt = Backtest(GOOG, RsiOscillator, cash = 10000)
print(bt.run())
print(bt.plot())

