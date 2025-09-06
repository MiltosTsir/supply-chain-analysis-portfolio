# For GitHub: minimal facility-location MILP with PuLP
import pulp as pl

def build_model(F, R, demand, capacity, fixed_cost, trans_cost):
    y = pl.LpVariable.dicts("open", F, lowBound=0, upBound=1, cat="Binary")
    x = pl.LpVariable.dicts("flow", [(f, r) for f in F for r in R], lowBound=0)

    m = pl.LpProblem("facility_location", pl.LpMinimize)
    m += pl.lpSum(fixed_cost[f] * y[f] for f in F) + \
         pl.lpSum(trans_cost[f, r] * x[(f, r)] for f in F for r in R)

    for r in R:
        m += pl.lpSum(x[(f, r)] for f in F) >= demand[r], f"demand_{r}"

    for f in F:
        m += pl.lpSum(x[(f, r)] for r in R) <= capacity[f] * y[f], f"cap_{f}"

    return m, x, y
