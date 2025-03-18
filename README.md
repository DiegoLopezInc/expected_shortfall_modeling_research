# Expected Shortfall Model Implementation and Analysis
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Overview
This repository contains an implementation and analysis of Expected Shortfall (ES) models for market risk measurement, developed as part of a Master's thesis in Computer Science focusing on financial risk management.

## Research Objectives
1. Implement and compare different ES calculation methodologies
2. Analyze the performance of ES vs traditional VaR approaches
3. Evaluate ES model behavior during stress periods
4. Propose improvements to existing ES estimation techniques

## Background
Yes, market risk professionals, including those at bulge bracket banks, have increasingly shifted attention toward models that address the limitations of Value-at-Risk (VaR), particularly its inability to capture tail risk (extreme events) and its lack of subadditivity (a mathematical property ensuring diversification benefits are properly reflected). One model that has gained significant traction as a "better" alternative is **Expected Shortfall (ES)**, also known as Conditional Value-at-Risk (CVaR).

### Expected Shortfall (ES): A Superior Alternative
**What It Is**: Expected Shortfall measures the average loss expected in the worst-case scenarios beyond a certain confidence level. Unlike VaR, which only provides a threshold (e.g., "losses won’t exceed $50 million with 99% confidence"), ES calculates the average of all losses exceeding that threshold, giving a fuller picture of tail risk.

#### Why Market Risk Professionals Are Interested
1. **Better Tail Risk Capture**: VaR ignores the severity of losses beyond its cutoff, which became a glaring issue during the 2008 financial crisis when extreme losses far exceeded VaR predictions. ES, by contrast, focuses on the "tail" of the loss distribution, making it more relevant for managing black-swan events—like market crashes or geopolitical shocks—that bulge bracket banks (e.g., Goldman Sachs, JPMorgan) must prepare for.
2. **Regulatory Push**: The Basel Committee on Banking Supervision, under Basel III/IV frameworks, has encouraged a shift from VaR to ES for internal models-based approaches to market risk capital calculations. As of March 18, 2025, this regulatory momentum has made ES a priority for risk departments aiming to stay compliant and optimize capital allocation.
3. **Coherence**: ES is a "coherent" risk measure (satisfying properties like subadditivity), meaning it better reflects the risk reduction from diversification across a portfolio—crucial for banks managing complex, multi-asset trading books.
4. **Practical Appeal**: Professionals appreciate ES’s ability to integrate with stress testing and scenario analysis, which are staples in bulge bracket risk management. For example, Morgan Stanley might use ES to assess the average loss in a repeat of the 2020 COVID-19 market drop, rather than just a single-point estimate.

#### Example in Practice
Imagine Citigroup’s market risk team modeling its fixed-income portfolio. They calculate a 99% ES of $75 million over one day. This means that in the worst 1% of scenarios, the average loss would be $75 million—offering a more conservative and informative metric than a VaR of, say, $50 million. They could then adjust hedges (e.g., buying more interest rate swaps) or reduce exposure based on this insight.

### Other Emerging Models
While ES is the frontrunner, market risk professionals are also exploring:
- **Extreme Value Theory (EVT)**: Focuses explicitly on tail events using statistical distributions like the Generalized Pareto Distribution. It’s gaining interest for its precision in rare-event modeling, though it’s more complex to implement.
- **Machine Learning-Based Models**: Banks like Bank of America are experimenting with AI-driven models that analyze vast datasets (market data, news sentiment, etc.) to predict risk dynamically. These are still supplementary but show promise for real-time adaptability.

### Why ES Stands Out
As of 2025, ES strikes a balance between theoretical rigor and practical implementation, aligning with both regulatory trends and the need for robust risk management in volatile markets (e.g., post-COVID recovery, rising interest rates). Market risk teams at bulge bracket banks are particularly drawn to its ability to quantify "how bad things could get" rather than just "how likely they are," making it a hot topic in risk management discussions today.

## Project Structure
```
expected_shortfall_model/
├── data/                   # Market data and test datasets
├── notebooks/             # Jupyter notebooks for analysis
├── src/                   # Source code
│   ├── models/           # ES model implementations
│   ├── utils/            # Helper functions
│   └── visualization/    # Plotting utilities
├── tests/                # Unit tests
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from src.models import ExpectedShortfall

# Initialize model
es_model = ExpectedShortfall(confidence_level=0.975)

# Fit to historical data
es_model.fit(returns_data)

# Calculate ES
es_value = es_model.calculate()
```

## Research Methodology
1. **Data Collection**: Historical market data from major indices and asset classes
2. **Model Implementation**: Historical simulation and parametric approaches
3. **Backtesting**: Out-of-sample performance evaluation
4. **Comparative Analysis**: Benchmarking against VaR and other risk measures

## Current Findings
- Implementation and analysis in progress
- Initial results suggest improved tail risk capture compared to VaR
- Further validation needed for stress period behavior

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Citation
If you use this code in your research, please cite:
```bibtex
@mastersthesis{lastname2025expected,
  title={Expected Shortfall Model Implementation and Analysis},
  author={[Your Name]},
  year={2025},
  school={[Your University]}
}
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
[Your Name] - [your.email@university.edu]
GitHub: [@yourusername]