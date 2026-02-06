"""Core context management for Pegasus."""

from __future__ import annotations

import dearpygui.dearpygui as dpg
from typing import Optional, Dict, Any


class Context:
    """
    High-level context manager for Pegasus applications.

    Wraps Dear PyGui context with additional Pegasus-specific configuration
    and performance optimizations.
    """

    _instance: Optional[Context] = None

    def __new__(cls) -> Context:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if hasattr(self, "_initialized"):
            return
        self._initialized = False
        self._context_active = False
        self._config: Dict[str, Any] = {}

    def create(self, config: Optional[Dict[str, Any]] = None) -> None:
        """
        Create the Dear PyGui context.

        Args:
            config: Optional configuration dictionary for context settings
        """
        if self._context_active:
            return

        dpg.create_context()
        self._context_active = True
        self._config = config or {}

        # Apply Pegasus defaults
        self._apply_defaults()

    def _apply_defaults(self) -> None:
        """Apply Pegasus-specific default configurations."""
        # Optimize for high-frequency rendering
        dpg.configure_app(auto_save_init_file=False, init_file="")

    def destroy(self) -> None:
        """Destroy the context and cleanup resources."""
        if self._context_active:
            dpg.destroy_context()
            self._context_active = False
            Context._instance = None

    def is_active(self) -> bool:
        """Check if context is active."""
        return self._context_active

    def __enter__(self) -> Context:
        """Context manager entry."""
        self.create()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.destroy()
