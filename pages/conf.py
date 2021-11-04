# -*- coding: utf-8 -*-

project = u'GPU Filter Bank'
copyright = u'2021'
source_suffix = ['.rst', '.md', '.ipynb']
master_doc = 'index'
language = None
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'RTDSphinxThemeSampledoc'
# extensions = ["myst_parser"]
extensions = ["myst_nb"]
jupyter_execute_notebooks = "off"