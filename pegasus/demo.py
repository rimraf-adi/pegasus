"""Main demo script for Pegasus."""

from __future__ import annotations

import pegasus as pg
import numpy as np


def main():
    """Run the main Pegasus demo."""
    print("=" * 50)
    print("Pegasus - High-Performance Charting Library")
    print("Built on Dear PyGui")
    print("=" * 50)
    print()

    # Create context
    pg.create_context()

    # Create viewport
    viewport = pg.Viewport(
        pg.ViewportConfig(
            title="Pegasus Demo - 1M+ Data Points @ 60 FPS",
            width=1400,
            height=900,
        )
    )
    viewport.create()
    viewport.setup_dearpygui()

    print("Generating 1,000,000 data points...")

    # Generate massive dataset
    n_points = 1_000_000
    x = np.linspace(0, 100, n_points)

    # Complex waveform
    y1 = np.sin(x) * np.exp(-x / 50) + 0.1 * np.sin(x * 10)
    y2 = np.cos(x * 0.5) * np.exp(-x / 80)
    y3 = np.sin(x * 2) * np.cos(x * 0.3) * 0.5

    # Create main window
    with pg.window(label="Pegasus Performance Demo", width=1300, height=800):
        # Info text
        pg.dpg.add_text(f"Displaying {n_points:,} data points per series")
        pg.dpg.add_text("Try zooming and panning - no downsampling needed!")
        pg.dpg.add_separator()

        # Main plot with multiple series
        with pg.plot(
            label="High-Frequency Data Visualization",
            height=700,
            width=1250,
            anti_aliased=True,
        ):
            pg.add_plot_legend()

            # X axis
            pg.add_plot_axis(pg.mvXAxis, label="Time")

            # Y axis
            y_axis = pg.add_plot_axis(pg.mvYAxis, label="Amplitude")

            # Add all series with GPU acceleration
            pg.add_line_series(
                x,
                y1,
                label="Primary Signal",
                parent=y_axis,
            )
            pg.add_line_series(
                x,
                y2,
                label="Secondary Signal",
                parent=y_axis,
            )
            pg.add_line_series(
                x,
                y3,
                label="Tertiary Signal",
                parent=y_axis,
            )

    # Show and run
    viewport.show()
    print()
    print("Demo running...")
    print("Performance: GPU-accelerated rendering")
    print("Features: Zoom, pan, and query without lag")
    print()
    print("Close window to exit.")
    print()

    viewport.start()

    # Cleanup
    pg.destroy_context()
    print()
    print("Demo complete!")


if __name__ == "__main__":
    main()
