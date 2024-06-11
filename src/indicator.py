import numpy as np
import warnings
from typing import Tuple

def RoI(ini_val: float, final_value: float) -> float:
    """
    Calculate the Return on Investment (RoI).
    
    Input parameters:
    ini_val: float: The initial value of the investment.
    final_value: float: The final value of the investment.
    
    Returns:
    float: The RoI as a percentage, rounded to two decimal places.
    
    The function computes the RoI by taking the difference between the final and initial values,
    dividing by the initial value, and multiplying by 100 to get the percentage.
    """
    return round((final_value - ini_val) / ini_val * 100, 2)

def winRate(returns: np.array) -> float:
    """
    Calculate the win rate of trades.
    
    Input parameters:
    returns: np.array: An array of returns from trades.
    
    Returns:
    float: The win rate as a percentage, rounded to two decimal places.
    
    The function computes the win rate by counting the number of positive returns and dividing
    by the total number of non-zero returns, then multiplying by 100 to get the percentage.
    """
    returns = returns.astype(float)
    win = np.count_nonzero(returns > 0)
    total_transaction = np.count_nonzero(returns != 0)
    return round(win / total_transaction * 100, 2)

def MDD(value_history: np.ndarray) -> float:
    """
    Calculate the Maximum Drawdown (MDD) of the account value history.
    
    Input parameters:
    value_history: np.ndarray: An array of historical account values.
    
    Returns:
    float: The MDD as a percentage, rounded to two decimal places.
    
    The function computes the MDD by finding the peak and trough values in the history,
    then calculating the percentage drop from the peak to the trough.
    """
    value_history = value_history.astype(float)
    peak_value = np.max(value_history)
    trough_value = np.min(value_history)
    return round((peak_value - trough_value) / peak_value * 100, 2)

def odds(returns: np.ndarray) -> float:
    """
    Calculate the odds of winning trades to losing trades.
    
    Input parameters:
    returns: np.ndarray: An array of returns from trades.
    
    Returns:
    float: The odds of winning trades to losing trades, rounded to four decimal places.
    
    The function computes the odds by dividing the number of positive returns by the number
    of negative returns. If there are no losses, the function returns infinity.
    """
    returns = returns.astype(float)
    win = np.count_nonzero(returns > 0)
    loss = np.count_nonzero(returns < 0)
    if loss == 0.0:
        return np.inf
    return round(win / loss, 4)

def oddsRatio(group1: np.ndarray, group2: np.ndarray) -> Tuple[float, float, float]:
    """
    Calculate the odds ratio between two groups of trade returns.
    
    Input parameters:
    group1: np.ndarray: An array of returns from the first group of trades.
    group2: np.ndarray: An array of returns from the second group of trades.
    
    Returns:
    Tuple[float, float, float]: A tuple containing the odds of group1, the odds of group2,
    and the odds ratio (group1 / group2), all rounded to four decimal places.
    
    The function computes the odds for each group and then calculates the odds ratio.
    If the odds for either group is infinity or NaN, appropriate warnings are issued
    and special handling is applied.
    """
    group1 = odds(group1.astype(float))
    group2 = odds(group2.astype(float))
    if np.isinf(group1) and np.isinf(group2):
        warnings.warn("The odds of group1 and group2 are inf, return nan", UserWarning)
        return group1, group2, np.nan
    if np.isnan(group1):
        warnings.warn("The odds of group1 is inf, return inf", UserWarning)
        return group1, group2, 0
    if np.isnan(group2):
        warnings.warn("The odds of group2 is inf, return 0", UserWarning)
        return group1, group2, np.inf
    return group1, group2, round(group1 / group2, 4)

def profitFactor(net_returns: np.ndarray) -> float:
    """
    Calculate the profit factor of trades.
    
    Input parameters:
    net_returns: np.ndarray: An array of net returns from trades.
    
    Returns:
    float: The profit factor, rounded to four decimal places.
    
    The function computes the profit factor by dividing the sum of positive returns by the
    absolute sum of negative returns. If there are no losses, a warning is issued and the
    loss value is set to zero.
    """
    net_returns = net_returns.astype(float)
    goss_profits = np.sum(net_returns[net_returns > 0])
    goss_loss = abs(np.sum(net_returns[net_returns < 0]))
    if goss_loss == 0.0:
        goss_loss = 0
        warnings.warn("The number of loss trading is 0. The value of odds would be abnormal", UserWarning)
    return round(goss_profits / goss_loss, 4)

def sharpRatio(returns: np.ndarray, roi: float) -> float:
    """
    Calculate the Sharpe Ratio of trades.
    
    Input parameters:
    returns: np.ndarray: An array of returns from trades.
    roi: float: The return on investment.
    
    Returns:
    float: The Sharpe Ratio, rounded to four decimal places.
    
    The function computes the Sharpe Ratio by subtracting the risk-free rate from the ROI,
    then dividing by the standard deviation of the non-zero returns. If the standard deviation
    is zero, a warning is issued and infinity is returned.
    """
    returns = returns.astype(float)
    returns = returns[returns != 0]
    profits_std = returns.std()
    RISK_FREE_RATE = 0.02  # short-term US government bonds rate
    if profits_std == 0.0:
        warnings.warn("The value of std is 0, return inf.", UserWarning)
        return np.inf
    return round((roi - RISK_FREE_RATE) / profits_std, 4)

    
    
    