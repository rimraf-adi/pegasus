"""Viewport manager for Dear PyGui."""
import dearpygui.dearpygui as dpg


class Viewport:
    """
    Manages the main application window (viewport).
    
    Args:
        title: Window title
        width: Window width in pixels
        height: Window height in pixels
    """
    
    def __init__(self, title: str = "Pegasus", width: int = 1280, height: int = 800):
        self.title = title
        self.width = width
        self.height = height
        dpg.create_viewport(title=title, width=width, height=height)

    def show(self):
        """Shows the viewport."""
        dpg.show_viewport()

    def set_primary_window(self, window_tag: str, value: bool = True):
        """Sets a window as the primary (fullscreen) window."""
        dpg.set_primary_window(window_tag, value)
