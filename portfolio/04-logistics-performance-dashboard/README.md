# Logistics Performance Dashboard  

## Overview
Develop an interactive dashboard to monitor logistics KPIs such as On-Time-In-Full (OTIF), lead times, and transportation costs. The dashboard provides real-time visibility for supply chain managers to make faster, data-driven decisions.

## Dataset
- Source: Customer Analytics / Shipping Data (Kaggle)  
- Link: https://www.kaggle.com/datasets/prachi13/customer-analytics  
- Alternative: Freight Shipment Data (Kaggle)  
- Link: https://www.kaggle.com/datasets/bhanupratapbiswas/freight-shipment-data  
- Notes: Shipment-level data including customer ID, shipping mode, order & delivery dates, costs.

## Objectives
- Build KPI definitions for logistics performance (OTIF, average lead time, transportation cost per unit).
- Design an interactive dashboard with drill-down capability.
- Visualize trends and identify bottlenecks (e.g., delayed carriers, high-cost modes).
- Provide scenario analysis for improvement initiatives.

## Methodology
1. Data preparation: calculate lead times, delivery performance, cost KPIs.
2. Define formulas:  
   - OTIF = (On-time and in-full orders ÷ Total orders) × 100  
   - Average Lead Time = mean(delivery_date – order_date)  
   - Transport Cost per Unit = total_transport_cost ÷ units_shipped  
3. Create data model in Power BI or Tableau.
4. Build dashboard: summary page + detail by region, mode, carrier.
5. Highlight insights with KPIs and visuals.

## Metrics
- OTIF %  
- Average lead time (days)  
- Transportation cost per unit (€)  
- Cost share by shipping mode  

## Files & Structure
data/
raw/ # original shipping dataset
processed/ # data with lead times & KPIs calculated
notebooks/ # optional EDA in Jupyter
src/ # Python scripts for KPI calculation (if used)
reports/ # PDF/Markdown report with KPI summary
Dashboards/ # Power BI/Tableau files (.pbix or .twbx)
figures/ # exported screenshots of dashboards


## How to Reproduce
```bash
# Prepare dataset
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook

Use notebooks to pre-compute KPIs.
Load processed dataset into Power BI / Tableau.
Open .pbix or .twbx file inside Dashboards/.
Results (Highlights)
Dashboard shows OTIF trend over 12 months and bottlenecks by carrier.
Identified Mode X as 30% more expensive per unit vs alternative.
Suggested improvement: renegotiate contracts and shift volume.
Next Steps
Automate data refresh from ERP system.
Add CO₂ emissions per transport mode to extend into sustainability.
