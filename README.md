# pyTRT

[![PyPI version](https://badge.fury.io/py/pyTRT.svg)](https://badge.fury.io/py/pyTRT)
[![Tests](https://github.com/wouterpeere/pyTRT/actions/workflows/test.yml/badge.svg)](https://github.com/wouterpeere/pyTRT/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/wouterpeere/pyTRT/branch/main/graph/badge.svg?token=I9WWHW60OD)](https://codecov.io/gh/wouterpeere/pyTRT)

pyTRT is a python package with different methods for the interpretation of thermal response tests. The goal of this
package is to
bundle all available methodologies for TRT analysis so the user can easily compare one to another.

Currently, the following methods are implemented:

- Traditional ILS, based on the work of (Gehlin, S., 2002)

## Requirements

This code is tested with Python 3.10, 3.11, 3.12 and 3.13 and requires the following libraries (the versions mentioned
are the ones with which the code is tested)

- numpy >= 1.26.4
- pandas >= 1.4.3

For the tests

- pytest >= 7.1.2

## Getting started

In order to use `pyTrt`, one should first import the TRT measurement data. After that, any method inside `pyTRT` can be
used for the analysis.

```python
from pyTRT import TRTData, ILS

# import load
linz = TRTData('examples/data/Linz.csv', 't [s]', 'Tf [degC]', col_power='P [W]',
               decimal=',', undisturbed_ground=11.7)

# analyse the measurement data
result = ILS(linz, 150, 0.133 / 2, 2.3e6)

print(f'Thermal conductivity {result.thermal_conductivity}')
print(f'Effective borehole thermal resistance {result.borehole_resistance}')
````

## Citation

If you use this python package, please cite it using the citation below.

Next to that, please cite the work of the author from which you used the methodology.

**Traditional ILS**

Gehlin, S., 2002. Thermal Response Test. Method, Development and Evaluation (Ph. D. dissertation). Department of
Environmental Engineering, University of Lulea, Sweden.

## Collaborate

There are many different methods for the analysis of TRT measurement data. If you have developed a method of your own
and you want to include it in this package, you are encouraged to share this. Please follow the contribution workflow.
