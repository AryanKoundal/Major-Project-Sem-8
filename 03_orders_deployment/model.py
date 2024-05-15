# helper objects for the other ones
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

import queue
from enum import Enum

signal_queue = queue.Queue()


class Prediction(Enum):
    LONG = 1
    SHORT = 2
    NEUTRAL = 3
    STOP = 4


class Signal:
    def __init__(self):
        self.model_id = None
        self.signal_id = None
        self.instrument = None
        self.prediction_time = None
        self.prediction = None
        self.quantity = None

    def __repr__(self):
        return str(self.__dict__)


class SignalProcessingException(Exception):
    pass


