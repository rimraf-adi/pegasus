# Pegasus Themes

This directory contains JSON theme files for the Pegasus charting library.

## Available Themes

### cyberpunk.json
Neon cyberpunk aesthetic with dark background and bright cyan/magenta accents.
Best for: Dark environments, trading dashboards, high-contrast visualization.

### terminal.json  
Classic terminal green-on-black monochrome theme.
Best for: Minimalist interfaces, retro aesthetics, reduced eye strain.

### light.json
Clean white background with blue/red/green accents.
Best for: Presentations, documentation screenshots, bright environments.

## Usage

```python
import pegasus as pg

# Load built-in theme
pg.set_theme("cyberpunk")

# Load custom theme from file
config = pg.load_theme("path/to/custom_theme.json")
```

## Creating Custom Themes

Create a JSON file following this structure:

```json
{
  "name": "my_theme",
  "description": "Description of the theme",
  "colors": {
    "background": [R, G, B, A],
    "line_primary": [R, G, B, A],
    ...
  },
  "rounding": 2.0,
  "spacing": 4.0,
  "thickness": {
    "line": 2.0,
    "grid": 1.0,
    "border": 1.0
  }
}
```

### Color Keys

- `background`: Main plot background
- `background_secondary`: Secondary/UI background
- `grid`: Grid line color
- `grid_major`: Major grid line color
- `line_primary`: Primary data series color
- `line_secondary`: Secondary data series color
- `line_tertiary`: Tertiary data series color
- `text`: Primary text color
- `text_secondary`: Secondary/muted text color
- `border`: Border color
- `up`: Positive/up movement color (candlesticks)
- `down`: Negative/down movement color (candlesticks)
- `highlight`: Selection highlight color
- `selection`: Query rectangle color

## Hot Reloading

Themes can be hot-reloaded during development:

```python
# Enable hot reload
pg.load_theme("themes/cyberpunk.json", hot_reload=True)
```

Modify the JSON file and see changes immediately without restarting.
