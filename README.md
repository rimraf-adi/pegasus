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
git clone https://github.com/yourusername/pegasus.git
cd pegasus

# Install dependencies
uv sync

# Run the demo
uv run python demo.py
```

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
- Asynchronous data streaming compatible with WebSocket/TCP feeds (e.g., binance-rs, kaiko)

## Quick Start

```python
import pegasus as pg
import numpy as np

# Create context
pg.create_context()

# Create viewport
pg.create_viewport(title="Pegasus Demo", width=1200, height=800)

# Setup Dear PyGui
pg.setup_dearpygui()

with pg.window(label="Chart Example", width=1100, height=700):
    # Generate sample data
    x = np.linspace(0, 4 * np.pi, 100000)  # 100k data points
    y = np.sin(x) * np.exp(-x/10)
    
    # Create plot
    with pg.plot(label="High-Performance Line Chart", height=600, width=1000):
        pg.add_plot_legend()
        pg.add_plot_axis(pg.mvXAxis, label="X")
        pg.add_plot_axis(pg.mvYAxis, label="Y")
        pg.add_line_series(x, y, label="sin(x) * exp(-x/10)")

# Show viewport
pg.show_viewport()

# Main loop
pg.start_dearpygui()

# Cleanup
pg.destroy_context()
```

## Performance Tuning

### Managing Vertex Buffers
Pegasus provides direct control over vertex buffer allocation:

```python
# Pre-allocate vertex buffer for known data sizes
pg.set_vertex_buffer_size(series_tag, num_points=1000000)

# Use zero-copy updates for streaming data
pg.update_series_data(series_tag, new_data, copy=False)
```

### Batch Rendering
Group multiple series updates to minimize GPU overhead:

```python
with pg.batch_render():
    for series in active_series:
        pg.update_series_data(series.tag, series.data)
```

### Texture Memory Management
For heatmaps and surfaces:

```python
# Bind custom textures
texture_id = pg.create_texture(width, height, format=pg.RGBA32F)
pg.bind_texture_to_series(series_tag, texture_id)

# Update texture data without reallocation
pg.update_texture_data(texture_id, new_data)
```

## API Reference

### Core

```python
pegasus.create_context()
pegasus.destroy_context()
pegasus.create_viewport(title, width, height)
pegasus.setup_dearpygui()
pegasus.show_viewport()
pegasus.start_dearpygui()
```

### Plotting

```python
pegasus.plot(label, **kwargs)
pegasus.add_plot_legend()
pegasus.add_plot_axis(axis, label)
pegasus.add_line_series(x, y, label)
pegasus.add_scatter_series(x, y, label)
pegasus.add_bar_series(x, y, label)
pegasus.add_candle_series(dates, opens, highs, lows, closes)
pegasus.add_ohlc_series(dates, opens, highs, lows, closes)
pegasus.add_renko_series(dates, closes, brick_size)
pegasus.add_kagi_series(dates, closes, reversal_amount)
pegasus.add_point_figure_series(dates, closes, box_size)
pegasus.add_heatmap(data, width, height)
pegasus.add_surface(x, y, z)
```

### Styling

```python
pegasus.load_theme(theme_path)
pegasus.set_theme("cyberpunk")  # Built-in themes: cyberpunk, terminal, light
pegasus.set_item_style(item, color=None, rounding=None, thickness=None)
```

### Event System

```python
pegasus.add_click_handler(callback)
pegasus.add_drag_handler(callback)
pegasus.add_zoom_handler(callback)
pegasus.add_query_handler(callback)  # Rectangle selection
```

## Cookbooks

### HFT Dashboard
Real-time order book visualization with Level 2/3 data:

```python
# See examples/hft_dashboard.py
```

### Real-time FFT Analysis
Streaming spectral analysis with sub-frame latency:

```python
# See examples/fft_analyzer.py
```

### Multi-window Docking Layouts
Complex workspace arrangements with persistent layouts:

```python
# See examples/docking_layout.py
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

## Theming

JSON-based hot-reloadable theme engine:

```json
{
  "name": "cyberpunk",
  "colors": {
    "background": [10, 10, 20, 255],
    "grid": [30, 30, 50, 255],
    "line_primary": [0, 255, 200, 255],
    "line_secondary": [255, 0, 128, 255]
  },
  "rounding": 2.0,
  "spacing": 4.0
}
```

Built-in themes:
- **Cyberpunk**: Neon colors on dark background
- **Terminal**: Monochrome green-on-black
- **Light**: Clean white background for presentations

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Built on [Dear PyGui](https://github.com/hoffstadt/DearPyGui)
- Powered by [Dear ImGui](https://github.com/ocornut/imgui)
- GPU acceleration via platform-native backends (DirectX, Metal, OpenGL)
