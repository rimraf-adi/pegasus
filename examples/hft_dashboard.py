"""HFT Dashboard example with real-time order book visualization."""

from __future__ import annotations

import pegasus as pg
import numpy as np
from typing import List, Dict
import random


class OrderBookSimulator:
    """Simulates real-time order book data."""

    def __init__(self, levels: int = 10):
        self.levels = levels
        self.mid_price = 50000.0
        self.spread = 0.5

    def get_order_book(self) -> Dict[str, List[float]]:
        """Generate simulated order book snapshot."""
        bids = []
        asks = []

        for i in range(self.levels):
            bid_price = self.mid_price - self.spread / 2 - i * 0.1
            ask_price = self.mid_price + self.spread / 2 + i * 0.1
            bid_size = random.uniform(0.1, 2.0) * (1 - i / self.levels)
            ask_size = random.uniform(0.1, 2.0) * (1 - i / self.levels)

            bids.append((bid_price, bid_size))
            asks.append((ask_price, ask_size))

        return {"bids": bids, "asks": asks}

    def update(self):
        """Update mid price."""
        self.mid_price += random.uniform(-5, 5)


def create_candlestick_data(n: int = 100) -> tuple:
    """Generate sample candlestick data."""
    dates = np.arange(n)
    opens = 50000 + np.cumsum(np.random.randn(n) * 10)
    highs = opens + np.abs(np.random.randn(n) * 50)
    lows = opens - np.abs(np.random.randn(n) * 50)
    closes = opens + np.random.randn(n) * 30

    return dates, opens, highs, lows, closes


def main():
    """Run HFT dashboard example."""
    # Setup
    pg.create_context()
    viewport = pg.Viewport(pg.ViewportConfig(title="HFT Dashboard", width=1400, height=900))
    viewport.create()
    viewport.setup_dearpygui()

    # Generate initial data
    simulator = OrderBookSimulator(levels=20)
    dates, opens, highs, lows, closes = create_candlestick_data(200)

    # Create window with docking
    with pg.window(label="HFT Dashboard", width=1300, height=800):
        # Price chart with candlesticks
        with pg.plot(label="BTC/USD Price", height=400, width=1200):
            pg.add_plot_legend()
            pg.add_plot_axis(pg.mvXAxis, label="Time")
            y_axis = pg.add_plot_axis(pg.mvYAxis, label="Price ($)")

            candle_tag = pg.add_candle_series(
                dates,
                opens,
                highs,
                lows,
                closes,
                label="Price",
                parent=y_axis,
            )

        # Order book depth chart
        with pg.plot(label="Order Book Depth", height=300, width=600):
            pg.add_plot_legend()
            pg.add_plot_axis(pg.mvXAxis, label="Price ($)")
            y_axis = pg.add_plot_axis(pg.mvYAxis, label="Size")

            # Will be updated in real-time
            bid_tag = pg.add_bar_series([], [], label="Bids", parent=y_axis)
            ask_tag = pg.add_bar_series([], [], label="Asks", parent=y_axis)

        # Volume profile
        with pg.plot(label="Volume Profile", height=300, width=600):
            pg.add_plot_legend()
            pg.add_plot_axis(pg.mvXAxis, label="Volume")
            pg.add_plot_axis(pg.mvYAxis, label="Price ($)")

    # Show and run
    viewport.show()
    print("HFT Dashboard running...")
    print("Note: This is a simulated demo with random data")
    viewport.start()

    pg.destroy_context()


if __name__ == "__main__":
    main()
