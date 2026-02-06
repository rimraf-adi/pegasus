# Pegasus

A bare-metal, GPU-accelerated high-performance charting library built on Dear PyGui.

## Overview

Pegasus is a visualization engine designed for quantitative analysts, HFT researchers, and systems engineers who require millisecond-latency feedback. Built on Dear PyGui (ImGui), it prioritizes raw frame time and complete render pipeline control over high-level abstractions.

**Performance Target**: Capable of rendering **millions** of data points at 60+ FPS without downsampling or decimation.

## Philosophy

"Zero-Latency, Infinite Config."

## Installation

Pegasus uses `uv` as its package manager.

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/rimraf-adi/pegasus.git
cd pegasus

# Install dependencies
uv sync

# Run the demo
uv run plot_eurusd.py
```

## Quick Start

### Candlestick Chart (TradingView-style)

```python
from pegasus import CandlestickChart, load_ohlc_csv

# Load OHLC data
dates, opens, highs, lows, closes = load_ohlc_csv("EURUSD_2025-10-29.csv")

# Create and display chart
chart = CandlestickChart(
    dates, opens, highs, lows, closes,
    label="EURUSD",
    title="EURUSD M1 Analysis"
)
chart.show()
```

### Line Chart

```python
from pegasus import LineChart
import numpy as np

x = np.linspace(0, 10, 1000).tolist()
y = [np.sin(xi) for xi in x]

chart = LineChart(x, y, label="Sine Wave", title="My Line Chart")
chart.show()
```

### Scatter Chart

```python
from pegasus import ScatterChart
import numpy as np

x = np.random.randn(500).tolist()
y = np.random.randn(500).tolist()

chart = ScatterChart(x, y, label="Random Points", title="Scatter Plot")
chart.show()
```

## Chart Controls

### CandlestickChart (TradingView-style)

| Action | Description |
|--------|-------------|
| **Scroll on chart** | Zoom time (X) axis only |
| **Scroll on Y-axis** | Zoom price (Y) axis only |
| **Left-click drag** | Pan the chart |
| **Middle-click double-click** | Reset/fit to data |

## Data Loading

### `load_ohlc_csv` - Flexible CSV Loading

Load OHLC data from CSV files with customizable column names:

```python
from pegasus import load_ohlc_csv

# Default column names (DATE, TIME, OPEN, HIGH, LOW, CLOSE)
dates, opens, highs, lows, closes = load_ohlc_csv("data.csv")

# Custom column names
dates, opens, highs, lows, closes = load_ohlc_csv(
    "data.csv",
    date_col="Date",
    time_col="Time",
    open_col="Open",
    high_col="High",
    low_col="Low",
    close_col="Close",
    date_format="%Y-%m-%d",
    time_format="%H:%M:%S"
)

# Single datetime column (no separate time column)
dates, opens, highs, lows, closes = load_ohlc_csv(
    "data.csv",
    date_col="Datetime",
    time_col=None,  # Set to None for single column
    date_format="%Y-%m-%d %H:%M:%S"
)
```

**Parameters:**

| Parameter | Default | Description |
|-----------|---------|-------------|
| `filepath` | *required* | Path to CSV file |
| `date_col` | `"DATE"` | Column name for date |
| `time_col` | `"TIME"` | Column name for time (set to `None` for combined datetime) |
| `open_col` | `"OPEN"` | Column name for open price |
| `high_col` | `"HIGH"` | Column name for high price |
| `low_col` | `"LOW"` | Column name for low price |
| `close_col` | `"CLOSE"` | Column name for close price |
| `date_format` | `"%Y.%m.%d"` | Date parsing format |
| `time_format` | `"%H:%M:%S"` | Time parsing format |

## Chart Classes

### CandlestickChart

```python
CandlestickChart(
    dates: List[float],      # Unix timestamps
    opens: List[float],
    highs: List[float],
    lows: List[float],
    closes: List[float],
    label: str = "OHLC",
    title: str = "Pegasus Candlestick Chart",
    width: int = 1280,
    height: int = 800,
    bull_color: tuple = (0, 255, 117, 255),   # Green
    bear_color: tuple = (255, 82, 82, 255),   # Red
    weight: float = 0.25
)
```

### LineChart

```python
LineChart(
    x: List[float],
    y: List[float],
    label: str = "Line",
    title: str = "Pegasus Line Chart",
    width: int = 1280,
    height: int = 800,
    color: tuple = (0, 255, 255, 255)
)
```

### ScatterChart

```python
ScatterChart(
    x: List[float],
    y: List[float],
    label: str = "Scatter",
    title: str = "Pegasus Scatter Chart",
    width: int = 1280,
    height: int = 800
)
```

## Architecture

### Dear PyGui Render Loop

Pegasus leverages Dear PyGui's immediate-mode architecture:

1. **Frame Start**: Poll events, update input state
2. **Build Phase**: Reconstruct UI from scratch (no retained state)
3. **Draw Phase**: Submit draw commands to GPU
4. **Present**: Swap buffers, cap to target FPS

### Event Polling Optimization

Sub-frame latency through:
- Direct Win32/X11/Cocoa event loop integration
- Minimal Python-side event processing
- Callback-based tool system

### Direct GPU Mapping

- Bypasses Python's GIL for rendering logic
- Leverages heavily optimized C++ backends
- Direct buffer mapping for NumPy arrays

## Key Capabilities

### Hyper-Customizable Render Pipeline
- Full access to low-level ImGui draw lists (polylines, beziers, custom primitives)
- Custom shader integration and texture binding for high-frequency heatmaps/surfaces
- Granular styling API allowing per-element overriding of colors, rounding, and spacing

### Advanced Financial & Scientific Primitives
- Native support for Candlestick, OHLC, Renko, Kagi, and Point & Figure charts
- Real-time Order Book (L2/L3) visualization layers
- Dynamic 3D plotting with interactive rotation and high-density point clouds

### Deep Integration
- Zero-copy mechanism for NumPy/Pandas → GPU buffer transfers
- Asynchronous data streaming compatible with WebSocket/TCP feeds

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Built on [Dear PyGui](https://github.com/hoffstadt/DearPyGui)
- Powered by [Dear ImGui](https://github.com/ocornut/imgui)
- GPU acceleration via platform-native backends (DirectX, Metal, OpenGL)
