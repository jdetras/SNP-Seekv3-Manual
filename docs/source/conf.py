# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SNP-Seek v3 Manual'
copyright = '2025, Breeding Innovations and Informatics, Rice Breeding Innovations, International Rice Research Institute'
author = 'Jeffrey Detras'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'myst_parser',
	'sphinxcontrib.images',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_js_files = ['js/external_links.js']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

images_config = {
    'override_image_directive': True,
    'default_image_width': '300px',
    'default_image_target': '_self',
    'default_group': 'default',
    'download': False,
}

html_static_path = ['_static']

html_css_files = [
    'lightbox2/css/lightbox.min.css',
]

html_js_files = [
    'lightbox2/js/lightbox.min.js',
]

def setup(app):
    app.add_css_file('lightbox2/css/lightbox.min.css')
    app.add_js_file('lightbox2/js/lightbox.min.js')

def setup(app):
    app.add_css_file('custom.css')  # for Sphinx >= 1.8