import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import plasma, utils
import numpy as np
import  tfx
# from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext

app = plasma.App()
data = app.datasets[0]

x_cols = ['Time',
          'Amount',
          'V1',
          'V2',
          'V3',
          'V4',
          'V5',
          'V6',
          'V7',
          'V8',
          'V9',
          'V10',
          'V11',
          'V12',
          'V13',
          'V14',
          'V15',
          'V16',
          'V17',
          'V18',
          'V19',
          'V20',
          'V21',
          'V22',
          'V23',
          'V24',
          'V25',
          'V26',
          'V27',
          'V28']

y_cols = ['Class']

datasets = utils.split_data(data,
                            [0,.15],
                            [x_cols,y_cols],
                            pre_shuffle=True,
                            to_numpy=False,
                            train_no_pos=False,
                            debug_on=True)
print('')
utils.counts_check(datasets,y_cols[0])

train_data = datasets['train']
test_data = datasets['test']


