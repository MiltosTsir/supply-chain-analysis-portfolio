# Inventory Optimization (Flagship)  

## Overview
Optimize inventory policies across multiple SKUs by calculating EOQ, Safety Stock, and Reorder Point. The goal is to reduce total cost of inventory while maintaining target service levels.

## Dataset
- Source: Product Demand Forecasting (Kaggle)
- Link: https://www.kaggle.com/datasets/felixzhao/productdemandforecasting
- Notes: Historical demand by product; you can augment with synthetic lead times and costs.

## Objectives
- Compute EOQ per SKU and compare against current order quantities.
- Size Safety Stock for target service levels (e.g., 95%–99%).
- Determine Reorder Points considering demand and lead-time variability.
- Quantify impact on holding, ordering, and stockout costs.

## Methodology
1. **Data preparation:** aggregate demand by SKU, estimate mean and std; add unit cost, holding rate, order cost, lead time.
2. **EOQ calculation:** classic Wilson formula; sensitivity to holding/ordering costs.
3. **Safety stock:** z-score × lead-time demand variability; multiple service-level scenarios.
4. **Reorder point:** average lead-time demand + safety stock; simulate stockouts.
5. **Evaluation:** before/after comparison on total cost & service level; ABC focus.

## Key Formulas
- **EOQ**  
  \[EOQ = \sqrt{\frac{2 \cdot D \cdot S}{H}}\]
  where \(D\)=annual demand, \(S\)=ordering cost per order, \(H\)=annual holding cost per unit.

- **Safety Stock (normal approx.)**  
  \[SS = z \cdot \sigma_{L}\]
  where \(z\)=z-score for target service, \(\sigma_{L}\)=std of demand during lead time.  
  If demand σ_d and lead time L (constant): \(\sigma_{L} = \sigma_d \sqrt{L}\).

- **Reorder Point**  
  \[ROP = \mu_{L} + SS\]
  where \(\mu_{L}\)=mean demand during lead time.

## Metrics
- Total Annual Cost = Holding + Ordering (+ optional Stockout penalty)
- Service Level (cycle service level or fill rate)
- Inventory turns

## Files & Structure
data/
raw/ # original files (not versioned)
processed/ # cleaned, with costs & lead times
notebooks/ # 01_eda.ipynb, 02_eoq_ss_rop.ipynb, 03_scenarios.ipynb
src/ # eoq.py, safety_stock.py, utils.py
reports/ # markdown/pdf summary with results
Dashboards/ # Power BI/Tableau comparison of policies
figures/ # exported charts


## How to Reproduce

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
Open notebooks/01_eda.ipynb → 02_eoq_ss_rop.ipynb → 03_scenarios.ipynb.

Results (Highlights)
EOQ policy reduces total cost by ~X% vs current ordering.
Safety stock at 97.5% CSL cuts stockouts by ~Y% with Z€ extra holding.
Next Steps
Different service levels per ABC class (A=98%, B=95%, C=90%).
Add supplier lead-time uncertainty scenarios; link outputs to replenishment dashboard.
