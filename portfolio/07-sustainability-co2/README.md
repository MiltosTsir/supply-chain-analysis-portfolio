# Sustainability: CO₂ Emissions by Transport Mode 

## Overview
Analyze CO₂ emissions of different transportation modes (air, sea, rail, road) and provide insights for sustainable supply chain design. Build KPIs that compare emissions vs cost and service level.

## Dataset
- Source: Transportation Dataset (Kaggle)  
- Link: https://www.kaggle.com/datasets/motazsaad/transportation-dataset  
- Notes: Contains transport mode, distances, costs, and CO₂ emissions data.

## Objectives
- Calculate CO₂ emissions per unit and per ton-km for each transport mode.
- Compare emissions vs cost trade-offs.
- Visualize modal split and sustainability KPIs.
- Recommend greener transport strategies.

## Methodology
1. **Data preparation**: clean and normalize distances, costs, and emissions.
2. **KPIs**:  
   - Emissions per ton-km = total CO₂ ÷ ton-km  
   - Cost per ton-km = total cost ÷ ton-km  
3. **Analysis**: compare all modes; identify outliers (e.g., air freight).
4. **Visualization**: scatter plot (cost vs emissions), pie chart modal split.
5. **Scenario modeling**: simulate shifting 10–20% volume to greener modes.

## Metrics
- CO₂ per ton-km (kg/ton-km)  
- Cost per ton-km (€)  
- Modal share (%)  
- Emissions reduction potential (%)  

## Files & Structure
data/
raw/ # original transportation dataset
processed/ # cleaned dataset with ton-km & KPIs
notebooks/ # EDA, KPI calculation, scenario analysis
src/ # emissions_calculator.py
reports/ # sustainability report
Dashboards/ # Power BI/Tableau dashboards
figures/ # charts (scatter, pie, bar)


## How to Reproduce
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook

Run notebooks/01_kpi_calculation.ipynb → 02_scenario_analysis.ipynb.
Results (Highlights)
Air freight emitted ~50× more CO₂ per ton-km than sea freight.
Shifting 15% volume from air to sea cut emissions by ~40% with only +10% lead time.
Dashboard highlights cost vs emissions trade-offs by mode.
Next Steps
Add CO₂ per carrier (if data available).
Include sustainability cost (carbon tax simulation).
Integrate results into Logistics Dashboard (Project 4).
