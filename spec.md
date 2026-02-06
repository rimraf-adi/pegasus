# Pegasus: High-Performance GPU Visualization Engine

## 1. Library Overview
- **Core Identity**: A bare-metal, GPU-accelerated visualization engine built on Dear PyGui (ImGui).
- **Target Audience**: Quantitative analysts, HFT researchers, and systems engineers requiring millisecond-latency feedback.
- **Philosophy**: "Zero-Latency, Infinite Config." Prioritizes raw frame time and complete render pipeline control over high-level abstractions.
- **Performance Target**: Capable of rendering **millions** of data points at 60+ FPS without downsampling or decimation.

## 2. Key Capabilities
- **Hyper-Customizable Render Pipeline**: 
    - Full access to low-level ImGui draw lists (polylines, beziers, custom primitives).
    - Custom shader integration and texture binding for high-frequency heatmaps/surfaces.
    - Granular styling API allowing per-element overriding of colors, rounding, and spacing.
- **Advanced Financial & Scientific Primitives**: 
    - Native support for Candlestick, OHLC, Renko, Kagi, and Point & Figure charts.
    - Real-time Order Book (L2/L3) visualization layers.
    - Dynamic 3D plotting with interactive rotation and high-density point clouds.
- **Deep Integration**: 
    - Zero-copy mechanism for NumPy/Pandas -> GPU buffer transfers.
    - Asynchronous data streaming compatible with WebSocket/TCP feeds (e.g., binance-rs, kaiko).

## 3. Documentation Structure
- **Architecture Deep Dive**: Understanding the Dear PyGui render loop and event polling optimization.
- **Installation**: Quick-setup via generic wheels and optimized local builds (Rust extensions where applicable).
- **Performance Tuning**: Guide on managing vertex buffers, texture memory, and batch rendering techniques.
- **API Reference**: Modular breakdown (Core, Plotting, Styling, Event System).
- **Cookbooks**: "HFT Dashboard", "Real-time FFT Analysis", "Multi-window Docking Layouts".

## 4. Technical Highlights
- **Direct GPU Mapping**: Bypasses Python's GIL for rendering logic where possible; leverages heavily optimized C++ backends.
- **Event-Driven Architecture**: Callback-based system for tools (drawing lines, fibonacci levels) with sub-frame latency.
- **Reactive Layouts**: Fully dockable, collapsible, and resizable windowing system "out of the box".
- **Theming**: JSON-based hot-reloadable theme engine supporting "Cyberpunk", "Terminal", and "Light" modes.