"""
Tests for Expected Shortfall implementation.
"""

import numpy as np
import pytest
from src.models.expected_shortfall import ExpectedShortfall


@pytest.fixture
def sample_returns():
    """Generate sample returns for testing."""
    np.random.seed(42)
    return np.random.normal(0, 0.02, 1000)


def test_es_initialization():
    """Test ES class initialization."""
    es = ExpectedShortfall(confidence_level=0.975)
    assert es.confidence_level == 0.975
    
    with pytest.raises(ValueError):
        ExpectedShortfall(confidence_level=1.5)


def test_historical_es(sample_returns):
    """Test historical ES calculation."""
    es = ExpectedShortfall()
    es_value = es.historical_es(sample_returns)
    assert isinstance(es_value, float)
    assert es_value > 0  # ES should be positive for losses


def test_parametric_es(sample_returns):
    """Test parametric ES calculation."""
    es = ExpectedShortfall()
    es_value = es.parametric_es(sample_returns, dist='normal')
    assert isinstance(es_value, float)
    assert es_value > 0
    
    with pytest.raises(ValueError):
        es.parametric_es(sample_returns, dist='invalid')
        
    with pytest.raises(NotImplementedError):
        es.parametric_es(sample_returns, dist='student-t')


def test_monte_carlo_es(sample_returns):
    """Test Monte Carlo ES calculation."""
    es = ExpectedShortfall()
    es_value = es.monte_carlo_es(sample_returns, n_simulations=1000, seed=42)
    assert isinstance(es_value, float)
    assert es_value > 0
    
    # Test reproducibility with seed
    es_value2 = es.monte_carlo_es(sample_returns, n_simulations=1000, seed=42)
    assert es_value == es_value2
