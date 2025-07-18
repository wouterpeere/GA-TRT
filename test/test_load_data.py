import pandas as pd
import numpy as np
import pytest

from pyTRT import TRTData


def test_p_average():
    data = TRTData('data/test_linz.csv', 't [s]', 'Tf [degC]', col_power='P [W]', decimal=',')
    assert np.isclose(data.average_power, 7191.3840791032635)
