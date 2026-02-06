"""EURUSD Candlestick Demo using Pegasus with TradingView-style zoom."""
import os
import dearpygui.dearpygui as dpg

# Import from pegasus package
from pegasus.core.context import Context
from pegasus.core.viewport import Viewport
from pegasus.utils.data import load_ohlc_csv
from pegasus.plotting.series import add_candle_series


def main():
    # Load data using pegasus utility
    csv_path = os.path.join(os.path.dirname(__file__), "EURUSD_2025-10-29.csv")
    print(f"Loading data from {csv_path}...")
    
    dates, opens, highs, lows, closes = load_ohlc_csv(csv_path)
    print(f"Loaded {len(dates)} candles.")
    
    # Initialize Pegasus context and viewport
    with Context() as ctx:
        vp = Viewport("Pegasus - EURUSD Demo", 1280, 800)
        ctx.setup()
        
        # Y-axis zoom state
        y_axis_hover_width = 60  # Approximate width of Y-axis label area
        
        def on_mouse_wheel(sender, app_data):
            """Handle mouse wheel for Y-axis zooming when in Y-axis area."""
            try:
                # Get mouse position and plot position
                mouse_x, mouse_y = dpg.get_mouse_pos()
                
                # Get the plot position and size
                plot_pos = dpg.get_item_pos("main_plot")
                plot_width = dpg.get_item_width("main_plot")
                
                # Y-axis is on the left side of the plot
                # Check if mouse is in Y-axis area (leftmost ~60 pixels of plot)
                in_y_axis = (plot_pos[0] <= mouse_x <= plot_pos[0] + y_axis_hover_width)
                
                if in_y_axis:
                    # Get current Y-axis limits
                    y_min, y_max = dpg.get_axis_limits("y_axis")
                    y_range = y_max - y_min
                    y_center = (y_min + y_max) / 2
                    
                    # Zoom in/out based on scroll direction
                    zoom_factor = 0.1
                    if app_data > 0:  # Scroll up = zoom in
                        new_range = y_range * (1 - zoom_factor)
                    else:  # Scroll down = zoom out
                        new_range = y_range * (1 + zoom_factor)
                    
                    # Set new limits centered on current view
                    new_min = y_center - new_range / 2
                    new_max = y_center + new_range / 2
                    dpg.set_axis_limits("y_axis", new_min, new_max)
            except Exception:
                pass  # Ignore errors during early initialization
        
        # Register global mouse wheel handler
        with dpg.handler_registry():
            dpg.add_mouse_wheel_handler(callback=on_mouse_wheel)
        
        with dpg.window(tag="primary_window"):
            dpg.add_text("EURUSD M1 Analysis")
            
            # Create plot with TradingView-style controls
            with dpg.plot(
                tag="main_plot",
                label="EURUSD M1",
                height=-1,
                width=-1,
                no_menus=False,
                pan_button=dpg.mvMouseButton_Left,  # Left-click drag to pan
                fit_button=dpg.mvMouseButton_Left,  # Double-click to fit
            ):
                dpg.add_plot_legend()
                
                # X-Axis with time scale
                dpg.add_plot_axis(dpg.mvXAxis, label="Time (UTC)", tag="x_axis", scale=dpg.mvPlotScale_Time)
                
                # Y-Axis
                with dpg.plot_axis(dpg.mvYAxis, label="Price", tag="y_axis"):
                    add_candle_series(dates, opens, highs, lows, closes, label="EURUSD")
            
            # Fit to data on startup
            dpg.fit_axis_data("y_axis")
        
        vp.set_primary_window("primary_window", True)
        ctx.start()


if __name__ == "__main__":
    main()
