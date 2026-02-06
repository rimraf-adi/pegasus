import dearpygui.dearpygui as dpg

def add_plot_legend(parent=None):
    dpg.add_plot_legend(parent=parent)

def add_plot_axis(axis, label="", parent=None, **kwargs):
    # This is a bit complex as DPG has add_plot_axis but usually inside a plot.
    # Wrappers usually return tags.
    pass

mvXAxis = dpg.mvXAxis
mvYAxis = dpg.mvYAxis
mvYAxis2 = 1 # Placeholder if not directly exposed in dpg namespace the same way
mvYAxis3 = 2 # Placeholder
