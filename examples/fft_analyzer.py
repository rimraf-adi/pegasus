"""Real-time FFT Analysis example."""

from __future__ import annotations

import pegasus as pg
import numpy as np
from typing import List
import time


def generate_signal(
    t: np.ndarray, frequencies: List[float], noise_level: float = 0.1
) -> np.ndarray:
    """Generate a multi-frequency signal with noise."""
    signal = np.zeros_like(t)
    for freq in frequencies:
        signal += np.sin(2 * np.pi * freq * t)
    signal += noise_level * np.random.randn(len(t))
    return signal


def compute_fft(signal: np.ndarray, sample_rate: float) -> tuple:
    """Compute FFT of signal."""
    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1 / sample_rate)
    magnitude = np.abs(fft)

    # Return only positive frequencies
    positive_freqs = freqs[: len(freqs) // 2]
    positive_magnitude = magnitude[: len(magnitude) // 2]

    return positive_freqs, positive_magnitude


def main():
    """Run real-time FFT analyzer."""
    # Setup
    pg.create_context()
    viewport = pg.Viewport(
        pg.ViewportConfig(title="Real-time FFT Analyzer", width=1200, height=800)
    )
    viewport.create()
    viewport.setup_dearpygui()

    # Parameters
    sample_rate = 1000.0  # Hz
    duration = 1.0  # seconds
    num_samples = int(sample_rate * duration)

    # Generate initial signal
    t = np.linspace(0, duration, num_samples)
    frequencies = [50, 120, 200]  # Hz
    signal = generate_signal(t, frequencies)
    freqs, magnitude = compute_fft(signal, sample_rate)

    # Create window
    with pg.window(label="FFT Analyzer", width=1100, height=700):
        # Time domain plot
        with pg.plot(label="Time Domain Signal", height=300, width=1000):
            pg.add_plot_legend()
            pg.add_plot_axis(pg.mvXAxis, label="Time (s)")
            y_axis = pg.add_plot_axis(pg.mvYAxis, label="Amplitude")

            time_tag = pg.add_line_series(t, signal, label="Signal", parent=y_axis)

        # Frequency domain plot
        with pg.plot(label="Frequency Domain (FFT)", height=300, width=1000):
            pg.add_plot_legend()
            pg.add_plot_axis(pg.mvXAxis, label="Frequency (Hz)")
            y_axis = pg.add_plot_axis(pg.mvYAxis, label="Magnitude")

            freq_tag = pg.add_line_series(freqs, magnitude, label="FFT Magnitude", parent=y_axis)

            # Add markers for detected peaks
            threshold = np.max(magnitude) * 0.5
            peaks = freqs[magnitude > threshold]
            for peak in peaks[:3]:  # Mark top 3 peaks
                pg.add_plot_axis(pg.mvXAxis, label=f"Peak @ {peak:.1f} Hz")

    # Show and run
    viewport.show()
    print("FFT Analyzer running...")
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Signal Frequencies: {frequencies} Hz")
    viewport.start()

    pg.destroy_context()


if __name__ == "__main__":
    main()
