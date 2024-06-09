import jso
import pandas as pd
import warnings

def loadTrades(filename: str) -> pd.DataFrame:
    """
    Load trade data from a JSON file and return it as a pandas DataFrame.
    
    Input parameters:
    filename: str: The path to the JSON file containing the trade data.
    
    Returns:
    pd.DataFrame: A pandas DataFrame containing the trade data.
    
    The function reads a JSON file, extracts the 'data' field, and converts it into a pandas DataFrame.
    If the DataFrame contains any null values, a warning is issued.
    """
    with open(filename, 'r') as file:
        df = pd.DataFrame(json.load(file)['data'])
    if df.isnull().values.any():
        warnings.warn("The data contains null values.", UserWarning)
    return df


def valueAfTrade(init_val: float, profits: np.ndarray) -> np.ndarray:
    """
    Calculate the account value after each trade.
    
    Input parameters:
    init_val: float: The initial value of the account.
    profits: np.ndarray: An array of profits for each trade, where negative values indicate losses.
    
    Returns:
    np.ndarray: An array of account values after each trade, including the initial value.
    
    The function takes an initial account value and an array of trade profits. It appends the initial
    value to the beginning of the profits array, then calculates the cumulative sum to obtain the
    account value after each trade.
    """
    profits = np.append(init_val, profits, axis=0)
    vals = np.cumsum(profits, axis=0)
    return vals

