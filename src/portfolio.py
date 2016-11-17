import pandas as pd
import numpy as np
from abc import ABCMeta, abstractmethod


class Portfolio(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_positions(self):
        raise NotImplementedError("generate_positions() not implemented")


class MarketOnClosePortfolio(Portfolio):

    def __init__(self, bars, signals, initial_capital=100000.0):

        self.bars = bars
        self.signals = signals
        self.initial_capital = initial_capital
        self.positions = self.generate_positions()


    def generate_positions(self):
        positions = pd.DataFrame(index=self.signals.index).fillna(0.0)
        positions[self] = 100 * self.signals['positions']
        return positions








