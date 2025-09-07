# Project 01 – Demand Forecasting

## Overview
This project focuses on **demand forecasting** using time series analysis.  
The goal is to explore historical sales data, identify trends and seasonality, and build baseline forecasting models.  
Later iterations will include advanced forecasting models such as ARIMA, Prophet, and ML approaches.

> **Update:** Notebooks now use the **processed data pipeline**.  
> Source: `data/processed/cleaned_sales.csv` (created in Colab from `data/raw/mock_kaggle.csv` with features such as lags and moving averages).

---

## Dataset
- **File:** [`mock_kaggle.csv`](data/raw/mock_kaggle.csv)  
- **Size:** 937 rows × 4 columns  
- **Columns:**
  - `data` → Date of sales record  
  - `venda` → Units sold (sales)  
  - `estoque` → Stock levels  
  - `preco` → Product price  

More details can be found in [`README_data.md`](data/raw/README_data.md).

---

## Notebooks
- [`01_eda_forecasting.ipynb`](notebooks/01_eda_forecasting.ipynb)  
  - Loads the dataset  
  - Exploratory Data Analysis (EDA)  
  - Time series decomposition (trend, seasonality, residuals)  
  - Baseline forecasts (Naive, 7-day Moving Average)  
  - Evaluation with MAPE  

Documentation: [`README_notebook.md`](notebooks/README_notebook.md)

---

## Folder Structure
01-demand-forecasting/
├── data/
│ ├── raw/
│ │ ├── mock_kaggle.csv
│ │ └── README_data.md
│ └── processed/ # (to be added later)
├── notebooks/
│ ├── 01_eda_forecasting.ipynb
│ └── README_notebook.md
├── src/ # (functions and scripts – to be developed)
├── reports/ # (markdown or pdf reports)
├── Dashboards/ # (Power BI / Tableau dashboards)
├── figures/ # (charts and screenshots)
└── README.md # (this file)


---

## Next Steps
1. Implement advanced forecasting models:
   - ARIMA
   - Facebook Prophet
   - ML models (XGBoost, LSTM)
2. Compare model performance against baselines.
3. Visualize results in dashboards (Power BI / Tableau).
4. Document insights in reports.
