"""EURUSD Candlestick Demo using Pegasus simplified API."""
import os
from pegasus import CandlestickChart, load_ohlc_csv


def main():
    # Load data
    csv_path = os.path.join(os.path.dirname(__file__), "EURUSD_2025-10-29.csv")
    print(f"Loading data from {csv_path}...")
    
    dates, opens, highs, lows, closes = load_ohlc_csv(csv_path)
    print(f"Loaded {len(dates)} candles.")
    
    # Create and show chart
    chart = CandlestickChart(
        dates, opens, highs, lows, closes,
        label="EURUSD",
        title="Pegasus - EURUSD M1 Analysis"
    )
    chart.show()


if __name__ == "__main__":
    main()
