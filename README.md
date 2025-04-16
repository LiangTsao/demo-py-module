# Sample Python Module

A simple sample Python module showcasing modern Python packaging practices.

## Installation

You can install the package directly from source:

```bash
pip install .
```

## Building

This project uses `hatchling` as the build backend. To build the package:

1. Install build dependencies:
```bash
pip install build
```

2. Build the distribution packages:
```bash
python -m build
```

This will create two files in the `dist/` directory:
- A wheel file (*.whl) for installing the package
- A source distribution (*.tar.gz) for distribution

### Publishing to PyPI

To publish the package to PyPI:

1. Install twine:
```bash
pip install twine
```

2. Upload to PyPI:
```bash
twine upload dist/*
```

## Usage

Here's a simple example of how to use the module:

```python
from sample_module import greet

# Get a greeting message
message = greet("Alice")
print(message)  # Output: Hello, Alice! Welcome to sample-module.
```

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install development dependencies: `pip install -e .[dev]`

This will install the package in editable mode with all development dependencies including pytest, ruff, and other testing/linting tools.

## Testing

To run tests:

```bash
python -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.