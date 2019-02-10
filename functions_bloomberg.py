import pandas as pd
import numpy as np
import blpapi

def isin_bloomberg(isin):
    """
    This function takes an isin as an input and returns
    a Bloomberg ticker as an output.

    The order of priority when searching for indexes is to first
    look for Brazilian tickers, then look for American tickers and
    finally look for European tickers
    """
    db = pd.read_csv('isin_database.csv',dtype={'ticker': str}).set_index('isin')
    if pd.notnull(isin):

        if isin in db.index:
            ticker = db.loc[isin, 'ticker']
            result = ''

            if isinstance(ticker, pd.Series):
                if (db.loc[isin, 'ticker_type'][0] == 'Equity') or any(db.loc[isin, 'ticker_type'] == 'Equity'):

                    if any(db.loc[isin, 'exchange'] == 'BZ'):
                        result = ticker[np.where(db['exchange'][isin] == 'BZ')[0][0]]

                    elif np.where(db['exchange'][isin] == 'US')[0].size != 0:
                        result = ticker[np.where(db['exchange'][isin] == 'US')[0][0]]

                    elif np.where(db['exchange'][isin] == 'EU')[0].size != 0:
                        result = ticker[np.where(db['exchange'][isin] == 'EU')[0][0]]

                    return result


                elif (db.loc[isin, 'ticker_type'][0] == 'Corp') or (db.loc[isin, 'ticker_type'][0] == 'Govt'):
                    result = db.loc[isin, 'ticker'][0]
                    return result

            else:
                return ticker

        else:
            return np.nan

    else:
        return np.nan
