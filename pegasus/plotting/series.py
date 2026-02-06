"""Plotting series wrappers for Dear PyGui."""
import dearpygui.dearpygui as dpg


def add_candle_series(dates, opens, highs, lows, closes, label="Candlesticks", parent=None,
                      bull_color=(0, 255, 117, 255), bear_color=(255, 82, 82, 255), weight=0.25):
    """
    Adds a candlestick series to the plot.
    
    Input matches OHLC standard order: Open, High, Low, Close.
    DPG expects: dates, opens, closes, lows, highs.
    
    Args:
        dates: List of Unix timestamps
        opens: List of open prices
        highs: List of high prices
        lows: List of low prices
        closes: List of close prices
        label: Series label
        parent: Parent axis tag
        bull_color: RGBA tuple for bullish candles
        bear_color: RGBA tuple for bearish candles
        weight: Candle body width (0.0 to 1.0)
    """
    # Remap to DPG order: dates, opens, closes, lows, highs
    # Note: parent is only passed if explicitly provided (not None)
    kwargs = {
        'label': label,
        'bull_color': bull_color,
        'bear_color': bear_color,
        'weight': weight,
    }
    if parent is not None:
        kwargs['parent'] = parent
    
    dpg.add_candle_series(dates, opens, closes, lows, highs, **kwargs)


def add_line_series(x, y, label="Line", parent=None):
    """Adds a line series to the plot."""
    dpg.add_line_series(x, y, label=label, parent=parent)


def add_scatter_series(x, y, label="Scatter", parent=None):
    """Adds a scatter series to the plot."""
    dpg.add_scatter_series(x, y, label=label, parent=parent)


def add_bar_series(x, y, label="Bar", parent=None):
    """Adds a bar series to the plot."""
    dpg.add_bar_series(x, y, label=label, parent=parent)


def add_ohlc_series(dates, opens, highs, lows, closes, label="OHLC", parent=None):
    """Adds an OHLC series (uses candlestick renderer)."""
    dpg.add_candle_series(dates, opens, closes, lows, highs, label=label, parent=parent)


# Stubs for advanced chart types (to be implemented)
def add_renko_series(data, label="Renko", parent=None):
    """Placeholder for Renko chart series."""
    pass


def add_kagi_series(data, label="Kagi", parent=None):
    """Placeholder for Kagi chart series."""
    pass


def add_point_figure_series(data, label="Point & Figure", parent=None):
    """Placeholder for Point & Figure chart series."""
    pass


def add_heatmap(values, rows, cols, label="Heatmap", parent=None):
    """Adds a heatmap series."""
    dpg.add_heatmap_series(values, rows, cols, label=label, parent=parent)


def add_surface(x, y, z, rows, cols, label="Surface", parent=None):
    """Placeholder for 3D surface plot."""
    pass
