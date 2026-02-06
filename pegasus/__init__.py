"""
Pegasus: A bare-metal, GPU-accelerated high-performance charting library.

Simplified API - import chart types directly:
    from pegasus import CandlestickChart, LineChart, ScatterChart
    from pegasus import load_ohlc_csv
"""

from __future__ import annotations

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

# High-level chart classes
from pegasus.charts import CandlestickChart, LineChart, ScatterChart

# Data utilities
from pegasus.utils.data import load_ohlc_csv

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    # Charts
    "CandlestickChart",
    "LineChart", 
    "ScatterChart",
    # Data
    "load_ohlc_csv",
]
