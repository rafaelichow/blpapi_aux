# blpapi_aux
This repository contains auxiliary functions and data to go with Bloomberg's blpapi (https://www.bloomberg.com/professional/support/api-library/):

1 - tia https://github.com/bpsmith/tia/blob/master/tia/bbg/v3api.py: has the most completed resources, data-wise. For Python3, some simple changes are required in the source code.

2 - BLPinterface https://github.com/691175002/BLPInterface: has the same BDP, BDS and BDH as in Bloomberg's Excel Add In. The most practical interface for those who are already familiared with Bloomberg's tools.

3 - My function isin_bloomberg takes an ISIN as an input and returns the Bloomberg ticker as the output. Can be very useful depending on the source of your data.
