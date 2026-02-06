"""CSV data loading utilities for Pegasus."""
import pandas as pd
from typing import Optional


def load_ohlc_csv(
    filepath: str,
    date_col: str = "DATE",
    time_col: Optional[str] = "TIME",
    open_col: str = "OPEN",
    high_col: str = "HIGH",
    low_col: str = "LOW",
    close_col: str = "CLOSE",
    date_format: str = "%Y.%m.%d",
    time_format: str = "%H:%M:%S",
):
    """
    Loads OHLC CSV data and returns lists compatible with Dear PyGui candlestick series.
    
    Args:
        filepath: Path to the CSV file
        date_col: Column name for date (or datetime if time_col is None)
        time_col: Column name for time (None if datetime is in single column)
        open_col: Column name for open price
        high_col: Column name for high price
        low_col: Column name for low price
        close_col: Column name for close price
        date_format: strftime format for date
        time_format: strftime format for time
    
    Returns:
        tuple: (dates, opens, highs, lows, closes) as lists of floats
    
    Example:
        # Default column names
        dates, opens, highs, lows, closes = load_ohlc_csv("data.csv")
        
        # Custom column names
        dates, opens, highs, lows, closes = load_ohlc_csv(
            "data.csv",
            date_col="Date",
            time_col="Time",
            open_col="Open",
            high_col="High",
            low_col="Low",
            close_col="Close"
        )
        
        # Single datetime column
        dates, opens, highs, lows, closes = load_ohlc_csv(
            "data.csv",
            date_col="Datetime",
            time_col=None,
            date_format="%Y-%m-%d %H:%M:%S"
        )
    """
    df = pd.read_csv(filepath)
    
    # Handle datetime parsing
    if time_col is not None:
        # Combine DATE and TIME columns
        datetime_format = f"{date_format} {time_format}"
        df['datetime'] = pd.to_datetime(df[date_col] + ' ' + df[time_col], format=datetime_format)
    else:
        # Single datetime column
        df['datetime'] = pd.to_datetime(df[date_col], format=date_format)
    
    # Use .timestamp() for correct Unix seconds
    dates = df['datetime'].apply(lambda x: x.timestamp()).tolist()
    
    return (
        dates,
        df[open_col].tolist(),
        df[high_col].tolist(),
        df[low_col].tolist(),
        df[close_col].tolist(),
    )
