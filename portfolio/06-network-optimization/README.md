# Network Optimization (Warehouse Location)  <!-- For GitHub -->

## Overview
Design an optimal warehouse location (or set of locations) to minimize total logistics cost while meeting regional demand and service constraints. This demonstrates linear programming for supply chain network design.

## Dataset
- Source: **Synthetic** (create demand per region, distances/cost per lane, facility fixed costs)
- Reference example: IBM – Supply Chain Optimization (GitHub)  
  https://github.com/IBM/supply-chain-optimization
- Notes: Include a data dictionary describing each table (regions, demand, lanes, facilities).

## Objectives
- Minimize total cost = fixed facility cost + transport cost.
- Decide which facilities to open and how much flow to ship to each region.
- Enforce capacity and demand-satisfaction constraints.
- Run what-if scenarios (capacity, costs, SLAs).

## Methodology
1. **Data**: build tables for `regions_demand`, `facilities` (fixed_cost, capacity), `lanes` (origin, destination, cost_per_unit).
2. **Model (MILP)**:
   - Binary open/close variables for facilities.
   - Continuous shipment variables per lane.
   - Constraints: demand fulfillment, facility capacity, flow only if facility open.
3. **Solve** with PuLP (or OR-Tools) and report objective value & decisions.
4. **Scenarios**: increase capacity/costs; add service radius (distance cap).
5. **Visualization**: map flows; bar charts of capacity utilization.

## Key Equations
- **Objective:**  
  \[min \sum_{f} F_f \cdot y_f + \sum_{f,r} c_{fr} \cdot x_{fr}\]
  \(y_f \in \{0,1\}\) open facility f, \(x_{fr} \ge 0\) flow f→r.
- **Demand:**  \(\sum_f x_{fr} \ge d_r \ \forall r\)
- **Capacity:** \(\sum_r x_{fr} \le cap_f \cdot y_f \ \forall f\)

## Files & Structure
data/
raw/ # synthetic CSVs: regions_demand.csv, facilities.csv, lanes.csv
processed/ # validated & merged tables
notebooks/ # 01_eda.ipynb, 02_model_formulation.ipynb, 03_scenarios.ipynb
src/ # model.py (PuLP/OR-Tools), data_loaders.py, utils.py
reports/ # summary & scenario comparisons
Dashboards/ # optional Power BI/Tableau for flows/costs
figures/ # maps & charts


## How to Reproduce
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
Run notebooks/02_model_formulation.ipynb or src/model.py to solve the MILP.
Results (Highlights)
Optimal facility set: <F1, F3> with total cost €X and utilization Y%.
Average distance to regions reduced by Z% vs baseline.
Next Steps
Add service-time constraints (max distance/time).
Consider multi-echelon (plants → DCs → customers) and CO₂ cost.
