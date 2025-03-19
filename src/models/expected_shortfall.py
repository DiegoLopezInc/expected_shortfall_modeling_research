"""
Expected Shortfall (ES) model implementation.

This module provides implementations of various Expected Shortfall calculation methods
including Historical Simulation, Parametric, and Monte Carlo approaches.
"""

import numpy as np
from scipy import stats
from typing import Union, Optional, Tuple


class ExpectedShortfall:
    def __init__(self, confidence_level: float = 0.975):
        """
        Initialize Expected Shortfall calculator.
        
        Args:
            confidence_level: The confidence level for ES calculation (default: 0.975)
        """
        if not 0 < confidence_level < 1:
            raise ValueError("Confidence level must be between 0 and 1")
        self.confidence_level = confidence_level
        
    def historical_es(self, returns: np.ndarray) -> float:
        """
        Calculate ES using historical simulation method.
        
        Args:
            returns: Array of historical returns
            
        Returns:
            Historical Expected Shortfall estimate
        """
        var_threshold = np.percentile(returns, (1 - self.confidence_level) * 100)
        tail_losses = returns[returns <= var_threshold]
        return -np.mean(tail_losses)
    
    def parametric_es(
        self, 
        returns: np.ndarray, 
        dist: str = 'normal'
    ) -> float:
        """
        Calculate ES using parametric method.
        
        Args:
            returns: Array of historical returns
            dist: Distribution assumption ('normal' or 'student-t')
            
        Returns:
            Parametric Expected Shortfall estimate
        """
        if dist not in ['normal', 'student-t']:
            raise ValueError("Distribution must be either 'normal' or 'student-t'")
            
        mu = np.mean(returns)
        sigma = np.std(returns, ddof=1)
        
        if dist == 'normal':
            z_score = stats.norm.ppf(1 - self.confidence_level)
            es = -(mu + sigma * (stats.norm.pdf(z_score) / (1 - self.confidence_level)))
        else:
            # TODO: Implement Student-t distribution ES calculation
            raise NotImplementedError("Student-t distribution not yet implemented")
            
        return es
    
    def monte_carlo_es(
        self, 
        returns: np.ndarray, 
        n_simulations: int = 10000,
        seed: Optional[int] = None
    ) -> float:
        """
        Calculate ES using Monte Carlo simulation.
        
        Args:
            returns: Array of historical returns
            n_simulations: Number of Monte Carlo simulations
            seed: Random seed for reproducibility
            
        Returns:
            Monte Carlo Expected Shortfall estimate
        """
        if seed is not None:
            np.random.seed(seed)
            
        mu = np.mean(returns)
        sigma = np.std(returns, ddof=1)
        
        simulated_returns = np.random.normal(mu, sigma, n_simulations)
        return self.historical_es(simulated_returns)
