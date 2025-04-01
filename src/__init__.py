# src/__init__.py
__version__ = "1.0.0"
__all__ = ['detection', 'simulation', 'alert', 'mitigation', 'ui']

# Enable ASAN for all C modules
import os
os.environ['ASAN_OPTIONS'] = 'detect_leaks=1'
