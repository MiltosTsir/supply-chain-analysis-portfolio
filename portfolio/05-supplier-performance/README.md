# Supplier Performance & Procurement Analysis  <!-- For GitHub -->

## Overview
Evaluate supplier performance using KPIs such as cost, lead time, and reliability. Build supplier scorecards to guide sourcing decisions and procurement strategy.

## Dataset
- Source: Retail Data Analytics (Kaggle)  
- Link: https://www.kaggle.com/datasets/nisargpatel/retail-data-analytics  
- Alternative: Maven Analytics – Office Supply Chain  
- Link: https://www.mavenanalytics.io/data-playground  
- Notes: Procurement dataset with purchase orders, supplier IDs, costs, and delivery times.

## Objectives
- Calculate KPIs for each supplier: average lead time, unit cost, defect rate (if available), and on-time delivery rate.
- Rank suppliers and create supplier scorecards.
- Identify cost-saving and risk-mitigation opportunities.
- Provide procurement recommendations.

## Methodology
1. **Data preparation**: clean PO data, aggregate by supplier.
2. **KPI calculation**:  
   - Average lead time = mean(delivery_date – order_date)  
   - On-time delivery % = (on-time deliveries ÷ total deliveries) × 100  
   - Unit cost = total spend ÷ units delivered  
3. **Visualization**: compare suppliers across KPIs.
4. **Supplier scorecard**: weight KPIs to assign overall performance score.
5. **Insights**: identify top/bottom suppliers and procurement strategy options.

## Metrics
- Average lead time (days)  
- On-time delivery %  
- Average unit cost (€)  
- Supplier performance score (weighted index)  

## Files & Structure
data/
raw/ # raw PO data
processed/ # supplier-level KPIs
notebooks/ # EDA, KPI calculation, scorecard
src/ # supplier_metrics.py
reports/ # PDF/Markdown supplier scorecards
Dashboards/ # Power BI/Tableau dashboards
figures/ # charts of supplier comparison


## How to Reproduce
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
Open notebooks/01_kpi_calculation.ipynb → 02_scorecard.ipynb.
Results (Highlights)
Supplier A had the lowest cost but longest lead time.
Supplier B achieved 98% on-time delivery with slightly higher cost.
Weighted scorecard identified Supplier B as best strategic partner.
