"""
Visualization utilities for risk metrics and analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple, List


def plot_return_distribution(
    returns: np.ndarray,
    es_level: float,
    var_level: float,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6)
) -> None:
    """
    Plot return distribution with VaR and ES levels.
    
    Args:
        returns: Array of returns
        es_level: Expected Shortfall level
        var_level: Value at Risk level
        title: Plot title
        figsize: Figure size
    """
    plt.figure(figsize=figsize)
    sns.histplot(returns, stat='density', alpha=0.6)
    sns.kdeplot(returns, color='red')
    
    plt.axvline(x=-var_level, color='orange', linestyle='--', 
                label=f'VaR ({var_level:.2%})')
    plt.axvline(x=-es_level, color='red', linestyle='--',
                label=f'ES ({es_level:.2%})')
    
    plt.title(title or 'Return Distribution with Risk Metrics')
    plt.xlabel('Returns')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_rolling_risk_metrics(
    returns: np.ndarray,
    var_values: List[float],
    es_values: List[float],
    window: int,
    figsize: Tuple[int, int] = (12, 6)
) -> None:
    """
    Plot rolling VaR and ES metrics.
    
    Args:
        returns: Array of returns
        var_values: List of VaR values
        es_values: List of ES values
        window: Rolling window size
        figsize: Figure size
    """
    plt.figure(figsize=figsize)
    
    dates = np.arange(len(var_values))
    plt.plot(dates, var_values, label='VaR', color='orange')
    plt.plot(dates, es_values, label='ES', color='red')
    plt.plot(dates, returns[-len(dates):], 
             alpha=0.3, color='gray', label='Returns')
    
    plt.title(f'Rolling Risk Metrics ({window}-day window)')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
