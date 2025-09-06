# ABC/XYZ Analysis  <!-- For GitHub -->

## Overview
Classify products into categories based on their contribution to total sales (ABC) and demand variability (XYZ). This helps prioritize inventory management policies and align service levels with business value.

## Dataset
- Source: Superstore Sales Dataset (Kaggle)  
- Link: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final  
- Notes: Transaction-level retail dataset including product, category, sales, and order dates.

## Objectives
- Perform **ABC analysis** (Pareto-based classification by revenue contribution).
- Perform **XYZ analysis** (demand variability using coefficient of variation).
- Combine results into an **ABC-XYZ matrix** to recommend inventory strategies.

## Methodology
1. **Data preparation**: aggregate sales quantity and revenue per SKU.
2. **ABC classification**: sort SKUs by contribution, compute cumulative %, cut-offs at 80/95/100%.
3. **XYZ classification**: calculate coefficient of variation (σ/μ) of monthly demand.
   - X = low variability (CV < 0.5)  
   - Y = medium (0.5–1.0)  
   - Z = high (>1.0)  
4. Combine ABC & XYZ classes → 9-cell matrix.
5. Recommend policies:  
   - AX: tight control, high service level.  
   - CZ: minimal stock, make-to-order.  

## Metrics
- % of revenue per class  
- % of SKUs per class  
- Average service level policy per cell  

## Files & Structure
data/
raw/ # original superstore dataset
processed/ # SKU-level aggregated data with CV
notebooks/ # analysis, visualization
src/ # abc.py, xyz.py, matrix.py
reports/ # summary of classification
Dashboards/ # Power BI/Tableau heatmap of ABC-XYZ
figures/ # exported bar charts, heatmaps


## How to Reproduce
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook

Results (Highlights)
~20% of SKUs generated ~80% of revenue (A items).
XYZ classification identified ~40% of items with unstable demand (Z).
ABC-XYZ matrix recommended differentiated service policies and stocking rules.
Next Steps
Integrate ABC-XYZ matrix with Safety Stock simulation.
Add supplier lead-time data for full inventory segmentation.
