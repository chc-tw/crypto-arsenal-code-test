import scipy
import numpy as np
import warnings

def RoI(cost: float, final_value: float) -> float:
    return round((final_value - cost) / cost,3)

def winRate(returns: np.array) -> np.float:
    returns = returns.astype(float)
    win = np.count_nonzero(returns>0)
    return round(win / len(returns),3)*100

def MDD(value_history: np.ndarray) -> float:
    value_history = value_history.astype(float)
    peak_value = np.max(value_history)
    trough_value = np.min(value_history)
    return round((peak_value - rough_value) / peak_value, 3)

def odds(returns: np.ndarray) -> float:
    returns = returns.astype(float)
    win = np.count_nonzero(returns>0)
    loss = np.count_nonzero(returns<0)
    if loss == 0.0:
        return np.inf
    return round(win/loss, 3)

def oddsRatio(group1: np.ndarray, group2: np.ndarray) -> float:
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
    return group1, group2, round(group1/group2,3)

def profitFactor(returns) -> float:
    returns = returns.astype(float)
    goss_profits = np.cumsum(returns[returns>0])
    goss_loss = abs(np.cumsum(returns[returns<0]))
    if goss_loss == 0.0:
        goss_loss = 0
        warnings.warn("The number of loss trading is 0. The value of odds would be abnomal", UserWarning)
    return round(goss_profits/goss_loss,3)

def sharpRatio(returns: np.ndarray) -> float:
    returns = returns.astype(float)
    profits_ev = returns.mean()
    profits_std = returns.std()
    NO_RISK_RATE = 0.02
    if profit_std == 0.0:
        warnings.warn("The value of std is 0, return inf.", UserWarning)
        return np.inf
    return round((profit_ev - NO_RISK_RATE) / profit_std, 3)
    
    
    