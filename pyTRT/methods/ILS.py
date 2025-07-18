"""
This file contains the code for the ILS approach for analysing the TRT measurements.
"""
import math

import numpy as np

from pyTRT.utils import TRTData
from pyTRT.methods.baseclass import _Method


class ILS(_Method):
    """
    This class contains the infinite line source (ILS) method for the analysis of the TRT measurements.
    """

    def __init__(self, data: TRTData, borehole_length: float, borehole_radius: float, volumetric_heat_capacity: float):
        """
        Initialises the infinite line source (ILS) method for the analysis of the TRT measurements.
        This method is based on the work of (Gehlin, S., 2002) [#Gehlin]_.

        Parameters
        ----------
        data : TRTData
            Object with the TRT measurement data.
        borehole_length : float
            Length of the borehole heat exchanger [m]
        borehole_radius : float
            Radius of the borehole [m]
        volumetric_heat_capacity : float
            Volumetric heat capacity [J/(m³K)]

        References
        ----------
        .. [#gehlin2002] Gehlin, S. (2002). *Thermal Response Test: Method, Development and Evaluation* (Ph.D. dissertation).
           Department of Environmental Engineering, Luleå University of Technology, Sweden.
        """

        a, b = np.polyfit(data.log_time_array, data.temperature_array, 1)

        ks = data.average_power / (4 * math.pi * borehole_length * a)

        gamma = 0.5772156649  # Euler-Mascheroni Constant
        Rb = (b - data.undisturbed_ground_temperature) * borehole_length / data.average_power - 1 / (
                4 * math.pi * ks) * (
                     np.log(4 * ks / volumetric_heat_capacity / (borehole_radius ** 2)) - gamma)

        # initiate baseclass
        super().__init__(Rb, ks)
