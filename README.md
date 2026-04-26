# How Do Inflation Metrics Influence S&P500 Returns and Volatility

This is my 2nd year Data Science project at the University of Exeter for the module BEE2041_A_2_202526. The project involves collecting, analysing and reporting the findings to reveal how three inflation metrics: Inflation, inflation volatility and inflation surprise correlate to two core performance measures of the S&P500: returns and volatility.

The analysis uses 300 monthly observations from 01/01/2001-12/31/2025 and collects 3 sets of raw data from 2 websites:

- **FRED** (CPIAUCSL)
- **FRED** (MICH)
- **Yahoo Finance** (^GSPC)
  
##Repository structure:

Inflation_Stock_Returns_Analysis/
│
├── Data/
│   ├── Cleaned_data/
│   └── Raw_data/
│
├── Executed_scripts/
│   ├── Analysis_output.ipynb
│   ├── Clean_output.ipynb
│   └── Get_raw_data_output.ipynb
│
├── Outputs/
│   ├── Figures/
│   └── Tables/
│
├── Scripts/
│   ├── Get_raw_data.ipynb
│   ├── Clean.ipynb
│   ├── Analysis.ipynb
│   └── Make.py
│
├── FRED_API_key.txt
├── LICENSE
└── README.md

##Library and Version requirements:

Python: 3.12.0
Pandas: 3.0.1
Matplotlib: 3.10.8
Seaborn: 0.13.2
Scipy: 1.17.1
Statsmodels: 0.14.6
Scikit-learn: 1.8.0
Numpy: 2.4.4
Yfinance: 1.2.0
Fredapi: N/A

