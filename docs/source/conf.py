# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'AgriOS'
copyright = '2025, Advance Insight'
author = 'Advance Insight'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "myst_parser",           # enables Markdown
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes']
# html_theme = 'furo'
# html_static_path = ["_static"]
# html_css_files = ["custom.css"]

html_context = {
    "display_github": True,                         # show the “Edit on GitHub” link
    "github_user": "advanceinsight",                # ⬅️ your GitHub org/user
    "github_repo": "agrios_documentation",          # ⬅️ your repo
    "github_version": "main",                       # branch
    "conf_py_path": "/docs/source/",                # path to your docs root, WITH trailing slash
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
