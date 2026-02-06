"""Context manager for Dear PyGui lifecycle."""
import dearpygui.dearpygui as dpg


class Context:
    """
    Manages the Dear PyGui context lifecycle.
    
    Usage:
        with Context() as ctx:
            vp = Viewport("My App", 1280, 800)
            ctx.setup()
            # ... create windows and plots ...
            ctx.start()
    """
    
    def __init__(self):
        self.is_running = False

    def __enter__(self):
        dpg.create_context()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        dpg.destroy_context()

    def setup(self):
        """Prepares the DPG environment. Must be called after creating viewport."""
        dpg.setup_dearpygui()

    def start(self):
        """Starts the DPG render loop."""
        dpg.show_viewport()
        dpg.start_dearpygui()
