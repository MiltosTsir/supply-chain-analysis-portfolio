# Demand Forecasting – Notebooks

This folder contains Jupyter notebooks for the **Demand Forecasting** project.  
The notebooks include exploratory data analysis (EDA), time series decomposition, and baseline forecasting models.

## 01_eda_forecasting.ipynb
- **Purpose:**  
  Initial exploratory analysis of the dataset (`mock_kaggle.csv`) and creation of baseline forecasting models.

- **Steps included:**  
  1. **Load Data**  
     - Source: [mock_kaggle.csv](../data/raw/mock_kaggle.csv)  
     - Columns:  
       - `data` → Date  
       - `venda` → Sales (units sold)  
       - `estoque` → Stock levels  
       - `preco` → Price  

  2. **Exploratory Data Analysis (EDA)**  
     - Data types, missing values, descriptive statistics  
     - Daily plots: sales, stock, and price over time  

  3. **Time Series Decomposition**  
     - Breakdown of sales (`venda`) into **trend**, **seasonality**, and **residuals**  

  4. **Baseline Forecasts**  
     - **Naive Forecast** (yesterday = today)  
     - **Moving Average (7 days)**  
     - Evaluation with **MAPE**  
     - Plots comparing actual vs forecasts  

- **Next Steps:**  
  - Implement more advanced models (ARIMA, Prophet, ML approaches)  
  - Compare performance against baselines  

---

## Folder Structure
notebooks/
└── 01_eda_forecasting.ipynb # EDA and baselines
└── README_notebook.md # Documentation


