# Demand Forecasting (Flagship)  

## Overview
Forecast monthly demand for 50–100 SKUs to improve supply planning and reduce stockouts. This project demonstrates time series forecasting, model comparison, and business interpretation.

## Dataset
- Source: Walmart Recruiting – Store Sales Forecasting (Kaggle)  
- Link: https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting  
- Notes: Historical sales at store-department level; exogenous variables available.

## Objectives
- Build baseline and advanced models (naïve, moving average, ARIMA, Prophet).
- Compare accuracy via MAPE/RMSE and select the champion model.
- Translate accuracy into inventory and service-level implications.

## Methodology
1. Ingest & clean sales, calendar, and promo features.
2. EDA: trend/seasonality, holiday effects, SKU clustering.
3. Modeling: ARIMA grid search; Prophet with regressors.
4. Validation: expanding window CV; error distribution by SKU.
5. Results: SKU-level forecasts and confidence intervals; uplift on service level.

## Key Metrics
- **MAPE** = mean absolute percentage error.  
- **RMSE** = root mean squared error.  

## Files & Structure
data/
raw/ # original files (not versioned)
processed/ # cleaned & ready-to-model
notebooks/ # Jupyter notebooks (EDA, modeling, validation)
src/ # reusable Python scripts
reports/ # PDF/Markdown reports
Dashboards/ # Power BI / Tableau files
figures/ # exported charts


## How to Reproduce
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook

Open notebooks/01_eda.ipynb then 02_modeling_arima.ipynb and 03_modeling_prophet.ipynb.

Results (Highlights)
Prophet with holiday regressors reduced MAPE by ~X% vs baseline.
Expected reduction of stockouts at ABC-A items by ~Y% (scenario estimate).
Next Steps
Add weather/macroeconomic regressors.
Serve forecasts to Inventory Optimization project.
