# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Raven'
copyright = '2023, GTRI'
author = 'GTRI'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_design'
]

myst_enable_extensions = ["colon_fence"]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTML output
#html_theme = "sphinx_book_theme"
#html_theme = "pydata_sphinx_theme"
html_theme = "furo"

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    '''Custom CSS for Width of RTD'''
    app.add_css_file('my_theme.css')
