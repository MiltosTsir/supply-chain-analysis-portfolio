# Figures – Demand Forecasting

This folder contains the figures generated from the analysis of the `mock_kaggle.csv` dataset.  
The plots support the Exploratory Data Analysis (EDA), baseline forecasts, and advanced models.

---

## List of Figures

- **daily_sales.png**  
  Daily sales (`venda`) plotted over time.

- **stock_over_time.png**  
  Stock levels (`estoque`) plotted over time.

- **price_over_time.png**  
  Product price (`preco`) evolution over time.

- **arima_forecast.png**  
  ARIMA model forecast compared with actual sales (train/test split).

- **prophet_forecast.png**  
  Prophet model forecast with predicted trend and seasonality.

- **prophet_components.png**  
  Prophet model components showing **trend**, **weekly seasonality**, and **yearly seasonality**.

---

## Notes
- All figures are saved as `.png` with `dpi=300`.  
- Plots were generated in Google Colab and uploaded manually to GitHub.  
- These figures are referenced in the project report: [`reports/demand_forecasting_report.md`](../reports/demand_forecasting_report.md).
