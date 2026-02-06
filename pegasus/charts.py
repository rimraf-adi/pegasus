"""High-level chart classes for Pegasus."""
import dearpygui.dearpygui as dpg
from typing import List, Optional, Callable


class Chart:
    """Base chart class that handles DPG lifecycle and common functionality."""
    
    def __init__(self, title: str = "Pegasus Chart", width: int = 1280, height: int = 800):
        self.title = title
        self.width = width
        self.height = height
        self._plot_tag = "main_plot"
        self._window_tag = "primary_window"
        self._x_axis_tag = "x_axis"
        self._y_axis_tag = "y_axis"
        self._y_axis_hover_width = 60
        
    def _setup_scroll_zoom_handler(self):
        """Register mouse wheel handler for axis-specific zooming."""
        def on_mouse_wheel(sender, app_data):
            try:
                mouse_x, _ = dpg.get_mouse_pos(local=False)  # Viewport coordinates
                
                # Y-axis is roughly leftmost 80px of the viewport
                in_y_axis = mouse_x < 80
                
                zoom_factor = 0.1
                
                if in_y_axis:
                    # Zoom Y-axis only
                    y_min, y_max = dpg.get_axis_limits(self._y_axis_tag)
                    y_range = y_max - y_min
                    y_center = (y_min + y_max) / 2
                    
                    if app_data > 0:
                        new_range = y_range * (1 - zoom_factor)
                    else:
                        new_range = y_range * (1 + zoom_factor)
                    
                    dpg.set_axis_limits(self._y_axis_tag, y_center - new_range/2, y_center + new_range/2)
                else:
                    # Zoom X-axis only (plot area)
                    x_min, x_max = dpg.get_axis_limits(self._x_axis_tag)
                    x_range = x_max - x_min
                    x_center = (x_min + x_max) / 2
                    
                    if app_data > 0:
                        new_range = x_range * (1 - zoom_factor)
                    else:
                        new_range = x_range * (1 + zoom_factor)
                    
                    dpg.set_axis_limits(self._x_axis_tag, x_center - new_range/2, x_center + new_range/2)
            except Exception as e:
                print(f"Scroll error: {e}")
        
        with dpg.handler_registry():
            dpg.add_mouse_wheel_handler(callback=on_mouse_wheel)

    def _create_context(self):
        """Initialize DPG context and viewport."""
        dpg.create_context()
        dpg.create_viewport(title=self.title, width=self.width, height=self.height)
        dpg.setup_dearpygui()
        
    def _start_render_loop(self):
        """Start the DPG render loop."""
        dpg.set_primary_window(self._window_tag, True)
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def show(self):
        """Display the chart. Override in subclasses."""
        raise NotImplementedError


class CandlestickChart(Chart):
    """
    TradingView-style candlestick chart.
    
    Features:
        - Scroll on chart: Zoom time axis only
        - Scroll on Y-axis: Zoom price axis
        - Left-click drag: Pan
        - Double-click: Reset/fit to data
    """
    
    def __init__(self, dates: List[float], opens: List[float], highs: List[float],
                 lows: List[float], closes: List[float], label: str = "OHLC",
                 title: str = "Pegasus Candlestick Chart", width: int = 1280, height: int = 800,
                 bull_color: tuple = (0, 255, 117, 255), bear_color: tuple = (255, 82, 82, 255),
                 weight: float = 0.25):
        super().__init__(title, width, height)
        self.dates = dates
        self.opens = opens
        self.highs = highs
        self.lows = lows
        self.closes = closes
        self.label = label
        self.bull_color = bull_color
        self.bear_color = bear_color
        self.weight = weight
    
    def show(self):
        """Render and display the candlestick chart."""
        self._create_context()
        self._setup_scroll_zoom_handler()
        
        with dpg.window(tag=self._window_tag):
            dpg.add_text(self.title)
            
            with dpg.plot(
                tag=self._plot_tag,
                label=self.label,
                height=-1,
                width=-1,
                no_menus=False,
                pan_button=dpg.mvMouseButton_Left,   # Left-click drag to pan
                fit_button=dpg.mvMouseButton_Middle, # Middle-click double-click to fit
            ):
                dpg.add_plot_legend()
                
                # X-Axis with time scale
                dpg.add_plot_axis(dpg.mvXAxis, label="Time", tag=self._x_axis_tag, 
                                  scale=dpg.mvPlotScale_Time)
                
                # Y-Axis
                with dpg.plot_axis(dpg.mvYAxis, label="Price", tag=self._y_axis_tag):
                    # DPG expects: dates, opens, closes, lows, highs
                    kwargs = {
                        'label': self.label,
                        'bull_color': self.bull_color,
                        'bear_color': self.bear_color,
                        'weight': self.weight,
                    }
                    dpg.add_candle_series(
                        self.dates, self.opens, self.closes, self.lows, self.highs,
                        **kwargs
                    )
            
            dpg.fit_axis_data(self._y_axis_tag)
        
        self._start_render_loop()


class LineChart(Chart):
    """Simple line chart."""
    
    def __init__(self, x: List[float], y: List[float], label: str = "Line",
                 title: str = "Pegasus Line Chart", width: int = 1280, height: int = 800,
                 color: tuple = (0, 255, 255, 255)):
        super().__init__(title, width, height)
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    
    def show(self):
        """Render and display the line chart."""
        self._create_context()
        
        with dpg.window(tag=self._window_tag):
            dpg.add_text(self.title)
            
            with dpg.plot(
                tag=self._plot_tag,
                label=self.label,
                height=-1,
                width=-1,
                pan_button=dpg.mvMouseButton_Left,
                fit_button=dpg.mvMouseButton_Left,
            ):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="X", tag=self._x_axis_tag)
                
                with dpg.plot_axis(dpg.mvYAxis, label="Y", tag=self._y_axis_tag):
                    dpg.add_line_series(self.x, self.y, label=self.label)
            
            dpg.fit_axis_data(self._y_axis_tag)
        
        self._start_render_loop()


class ScatterChart(Chart):
    """Scatter plot chart."""
    
    def __init__(self, x: List[float], y: List[float], label: str = "Scatter",
                 title: str = "Pegasus Scatter Chart", width: int = 1280, height: int = 800):
        super().__init__(title, width, height)
        self.x = x
        self.y = y
        self.label = label
    
    def show(self):
        """Render and display the scatter chart."""
        self._create_context()
        
        with dpg.window(tag=self._window_tag):
            dpg.add_text(self.title)
            
            with dpg.plot(
                tag=self._plot_tag,
                label=self.label,
                height=-1,
                width=-1,
                pan_button=dpg.mvMouseButton_Left,
                fit_button=dpg.mvMouseButton_Left,
            ):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="X", tag=self._x_axis_tag)
                
                with dpg.plot_axis(dpg.mvYAxis, label="Y", tag=self._y_axis_tag):
                    dpg.add_scatter_series(self.x, self.y, label=self.label)
            
            dpg.fit_axis_data(self._y_axis_tag)
        
        self._start_render_loop()
