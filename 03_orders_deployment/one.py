#
# Example Code for Algorithmic Strategy Deployment
# on Oanda (https://oanda.com)
#
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
# The code is for illustration purposes only. No warranties or representations
# to the extent permitted by applicable law. The code does not
# represent investment advice or a recommendation in any regard.
#


''' This is a trading strategy template for an algorithmic trading strategy based
    on technical indicators that can be defined flexibly.
'''
import numpy as np
from model import Prediction
from base import BaseStrategy


class one(BaseStrategy):
    """
    This is the set of default model parameters.
        Override and add where applicable.
    """

    def __init__(self, model_parameters, config):
        super().__init__(model_parameters, config)
        if model_parameters['sma'] > self.n_bars:
            self.n_bars = model_parameters['sma'] * 3

    def custom_data_preparation(self, data, is_training_data):
        """
        Add required data preparations here.
        """
        prediction = self.instrument + '_prediction'
        data['sma'] = (data[self.instrument + '_close'].rolling(
            self.sma).mean().shift(1))
        data.dropna(inplace=True)
        price = data[self.instrument + '_close'].shift(1)
        data[prediction] = np.where(price > data['sma'], 1, -1)

    def on_signal(self, predicted_data, signal_date):
        """
        This method is called every time the strategy generates a signal.
        """
        direction = predicted_data.loc[signal_date][
                self.instrument + '_prediction']
        if direction == -1:
            prediction = Prediction.SHORT
        else:
            prediction = Prediction.LONG
        return prediction
