import os
import sys
sys.path.insert(0, os.path.abspath('../'))

extensions = [
    'sphinx.ext.autodoc',  # Automatically documents Python code
    'sphinx.ext.napoleon',  # Supports Google-style and NumPy-style docstrings
]
