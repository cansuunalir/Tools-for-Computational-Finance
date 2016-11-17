import pandas as pd
import numpy as np
from portfolio import Portfolio, MarketOnClosePortfolio


def backtest_close(self, port):
    portfolio = pd.DataFrame(index=port.bars.index)
    portfolio['Holdings'] = port.positions.mul(port.bars['Close'], axis='index')
    portfolio['Cash'] = port.initial_capital - portfolio['Holdings'].cumsum
    portfolio['Total'] = portfolio['Cash'] + port.positions[self].cumsum()*port.bars['Close']
    portfolio['Returns'] = portfolio['Total'].pct_change()
    return portfolio

