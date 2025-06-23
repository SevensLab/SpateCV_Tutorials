# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup -----------------------------------------------------
# If needed, uncomment and adjust the path
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information --------------------------------------------
project = 'SpateCV'
copyright = '2025, Jiaqi Yuan'
author = 'Jiaqi Yuan'
release = '1.0.0'

# -- General configuration ------------------------------------------
extensions = []  # No additional extensions needed for static HTML
templates_path = ['_templates']
exclude_patterns = []

# -- HTML output ----------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_extra_path = ['notebooks_html']
html_context = {}
html_css_files = ['custom.css']