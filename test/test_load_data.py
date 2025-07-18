import pandas as pd
import numpy as np
import pytest

from pyTRT import TRTData, FOLDER


def test_p_average():
    data = TRTData(FOLDER.parent.joinpath("test/data/test_linz.csv"), 't [s]', 'Tf [degC]', col_power='P [W]',
                   decimal=',')
    assert np.isclose(data.average_power, 7191.3840791032635)
