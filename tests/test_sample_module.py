"""Test suite for demo-py-module."""

import pytest
from sample_module import greet

def test_greet():
    """Test the greet function."""
    # Test with a regular name
    assert greet("Alice") == "Hello, Alice! Welcome to sample-module."
    
    # Test with empty string
    assert greet("") == "Hello, ! Welcome to sample-module."
    
    # Test with special characters
    assert greet("John Doe!") == "Hello, John Doe!! Welcome to sample-module."

