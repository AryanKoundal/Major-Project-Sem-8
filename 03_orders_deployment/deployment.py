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
import threading
from model import signal_queue
from processor import SignalProcessor

from sma import sma  # imports the trading strategy

model_parameters = dict()
model_parameters['instrument'] = 'EUR_USD'
model_parameters['frequency'] = 'M1'
model_parameters['trading_quantity'] = 10000
model_parameters['n_signals_to_gen'] = 10

model_parameters['sma1'] = 3
model_parameters['sma2'] = 10
model_parameters['trade_immediately'] = True

if __name__ == '__main__':
    conf_file = 'oanda.cfg'

    threading.Thread(target=SignalProcessor(conf_file).listen_to_signal,
            daemon=True).start()
    strategy = sma(model_parameters, 'oanda.cfg')
    strategy.generate_signal()

    signal_queue.join()
