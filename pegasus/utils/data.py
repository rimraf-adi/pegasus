"""CSV data loading utilities for Pegasus."""
import pandas as pd


def load_ohlc_csv(filepath: str, date_col: str = "DATE", time_col: str = "TIME",
                  date_format: str = "%Y.%m.%d", time_format: str = "%H:%M:%S"):
    """
    Loads OHLC CSV data and returns lists compatible with Dear PyGui candlestick series.
    
    Args:
        filepath: Path to the CSV file
        date_col: Column name for date
        time_col: Column name for time
        date_format: strftime format for date
        time_format: strftime format for time
    
    Returns:
        tuple: (dates, opens, highs, lows, closes) as lists of floats
    """
    df = pd.read_csv(filepath)
    
    # Combine DATE and TIME columns
    datetime_format = f"{date_format} {time_format}"
    df['datetime'] = pd.to_datetime(df[date_col] + ' ' + df[time_col], format=datetime_format)
    
    # Use .timestamp() for correct Unix seconds
    dates = df['datetime'].apply(lambda x: x.timestamp()).tolist()
    
    return (
        dates,
        df['OPEN'].tolist(),
        df['HIGH'].tolist(),
        df['LOW'].tolist(),
        df['CLOSE'].tolist()
    )
