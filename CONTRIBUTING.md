# Contributing to Pegasus

Thank you for your interest in contributing to Pegasus! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- Python 3.10 or higher
- `uv` package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pegasus.git
cd pegasus
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Install pre-commit hooks:
```bash
uv run pre-commit install
```

## Development Workflow

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=pegasus

# Run benchmarks
uv run pytest --benchmark-only
```

### Code Quality

We use several tools to maintain code quality:

```bash
# Format code
uv run black pegasus/ examples/

# Lint code
uv run ruff check pegasus/ examples/

# Type check
uv run mypy pegasus/
```

### Running Examples

```bash
# Basic example
uv run python examples/basic.py

# HFT Dashboard
uv run python examples/hft_dashboard.py

# FFT Analyzer
uv run python examples/fft_analyzer.py

# Main demo
uv run pegasus-demo
```

## Project Structure

```
pegasus/
├── pegasus/              # Main package
│   ├── core/            # Core functionality (context, viewport)
│   ├── plotting/        # Chart types and axes
│   ├── styling/         # Themes and appearance
│   ├── events/          # Event handlers
│   ├── performance/     # Optimization utilities
│   ├── types.py         # Type definitions
│   ├── demo.py          # Main demo script
│   └── __init__.py      # Package exports
├── examples/            # Example scripts
├── themes/              # JSON theme files
├── tests/               # Test suite
├── pyproject.toml       # Project configuration
└── README.md           # Documentation
```

## Contributing Guidelines

### Code Style

- Follow PEP 8 with a 100-character line limit
- Use type hints for all function signatures
- Write docstrings for all public functions and classes
- Keep functions focused and under 50 lines when possible

### Commit Messages

Use conventional commits format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Test additions or changes
- `chore:` Maintenance tasks

Example:
```
feat: add support for OHLC charts

Implements candlestick and OHLC series with customizable colors
for up/down movements.
```

### Pull Request Process

1. **Create a branch**: `git checkout -b feature/your-feature-name`
2. **Make your changes**: Follow the code style guidelines
3. **Add tests**: Ensure your changes are covered by tests
4. **Update documentation**: Update README.md if needed
5. **Run quality checks**: `uv run black . && uv run ruff check . && uv run mypy .`
6. **Commit**: Use conventional commit messages
7. **Push**: `git push origin feature/your-feature-name`
8. **Create PR**: Open a pull request with a clear description

### Performance Considerations

Pegasus prioritizes performance. When contributing:

- Profile your changes with large datasets (1M+ points)
- Avoid unnecessary data copying
- Use NumPy vectorized operations
- Consider memory usage for large datasets
- Document performance implications of new features

### Testing

- Write unit tests for all new functionality
- Include performance benchmarks for chart types
- Test with edge cases (empty data, single point, very large datasets)
- Ensure examples run without errors

## Areas for Contribution

We welcome contributions in the following areas:

### High Priority
- Additional chart types (box plots, violin plots, etc.)
- Performance optimizations
- Real-time data streaming improvements
- Documentation and tutorials

### Medium Priority
- Additional color themes
- Export functionality (PNG, SVG, PDF)
- Interactive tool improvements
- Cross-platform testing

### Good First Issues
- Documentation improvements
- Code examples
- Bug fixes
- Test coverage

## Questions?

- Open an issue for bugs or feature requests
- Join discussions in existing issues
- Reach out to maintainers

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code:

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Respect different viewpoints and experiences

## License

By contributing to Pegasus, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Pegasus!
