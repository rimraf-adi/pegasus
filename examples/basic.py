"""Basic example demonstrating Pegasus charting capabilities."""

from __future__ import annotations

import pegasus as pg
import numpy as np


def main():
    """Run the basic chart example."""
    # Create context
    pg.create_context()

    # Create and configure viewport
    viewport = pg.Viewport(
        pg.ViewportConfig(
            title="Pegasus Basic Example",
            width=1200,
            height=800,
        )
    )
    viewport.create()
    viewport.setup_dearpygui()

    # Generate sample data - 100k points
    print("Generating 100,000 data points...")
    x = np.linspace(0, 4 * np.pi, 100000)
    y1 = np.sin(x) * np.exp(-x / 10)
    y2 = np.cos(x) * np.exp(-x / 10)

    # Create main window
    with pg.window(label="Chart Demo", width=1100, height=700):
        # Create plot
        with pg.plot(label="High-Performance Line Chart", height=600, width=1000):
            pg.add_plot_legend()

            # X axis
            pg.add_plot_axis(pg.mvXAxis, label="Time")

            # Y axis with series
            y_axis = pg.add_plot_axis(pg.mvYAxis, label="Amplitude")

            # Add series
            pg.add_line_series(x, y1, label="sin(x) * exp(-x/10)", parent=y_axis)
            pg.add_line_series(x, y2, label="cos(x) * exp(-x/10)", parent=y_axis)

    # Show and run
    viewport.show()
    print("Running... Close window to exit.")
    viewport.start()

    # Cleanup
    pg.destroy_context()


if __name__ == "__main__":
    main()
