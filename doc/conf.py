# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Cactus"
copyright = "2024, Advanced Analytics @ ENGIE"
author = "Advanced Analytics @ ENGIE"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # Markdown support
    "sphinx_rtd_theme",  # Read the Docs theme
    "rst2pdf.pdfbuilder",  # PDF builder
    "sphinx.ext.mathjax",  # MathJax support
]

master_doc = "index"  # The master toctree document
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_last_updated_fmt = "%b %d, %Y"
html_static_path = ["_static"]
html_css_files = ["layout.css"]  # Additional formating file
html_theme_options = {
    "logo_only": True,  # Only display the logo image, do not display the project name at the top of the sidebar
    "prev_next_buttons_location": "bottom",  # Display the previous and next buttons on the bottom of the page
}
html_logo = "docs/cactus-logo.svg"
