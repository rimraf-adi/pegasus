"""
Pegasus: A bare-metal, GPU-accelerated high-performance charting library.

Built on Dear PyGui for quantitative analysts, HFT researchers, and systems engineers
requiring millisecond-latency feedback.
"""

from __future__ import annotations

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

# Lazy imports - users import from submodules directly to avoid DPG context conflicts
# Example usage:
#   from pegasus.core.context import Context
#   from pegasus.core.viewport import Viewport
#   from pegasus.utils.data import load_ohlc_csv
#   from pegasus.plotting.series import add_candle_series

__all__ = [
    "__version__",
    "__author__",
    "__license__",
]
