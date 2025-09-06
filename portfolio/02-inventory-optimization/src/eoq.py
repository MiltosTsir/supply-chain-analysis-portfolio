# For GitHub: minimal EOQ helper
import math

def eoq(annual_demand, order_cost, annual_holding_cost):
    """Return Economic Order Quantity."""
    return math.sqrt((2 * annual_demand * order_cost) / annual_holding_cost)
