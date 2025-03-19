"""
Data loading and preprocessing utilities for market risk analysis.
"""

import pandas as pd
import yfinance as yf
from typing import List, Union, Optional
from datetime import datetime, timedelta


def fetch_market_data(
    tickers: Union[str, List[str]],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    interval: str = '1d'
) -> pd.DataFrame:
    """
    Fetch market data from Yahoo Finance.
    
    Args:
        tickers: Single ticker or list of tickers
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        interval: Data interval ('1d', '1wk', '1mo')
        
    Returns:
        DataFrame with market data
    """
    if isinstance(tickers, str):
        tickers = [tickers]
        
    if end_date is None:
        end_date = datetime.now().strftime('%Y-%m-%d')
    if start_date is None:
        start_date = (datetime.strptime(end_date, '%Y-%m-%d') - 
                     timedelta(days=365)).strftime('%Y-%m-%d')
    
    data = pd.DataFrame()
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date, interval=interval)
        if not hist.empty:
            hist['Ticker'] = ticker
            data = pd.concat([data, hist])
            
    return data


def calculate_returns(
    prices: pd.Series,
    method: str = 'log'
) -> pd.Series:
    """
    Calculate returns from price series.
    
    Args:
        prices: Series of asset prices
        method: Return calculation method ('log' or 'simple')
        
    Returns:
        Series of returns
    """
    if method not in ['log', 'simple']:
        raise ValueError("Method must be either 'log' or 'simple'")
        
    if method == 'log':
        returns = np.log(prices / prices.shift(1))
    else:
        returns = prices.pct_change()
        
    return returns.dropna()
