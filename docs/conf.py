import sys
import os
import pkg_resources

import pylons_sphinx_themes
import pyramid_watcher

# Get the project root dir, which is the parent dir of this
# cwd = os.getcwd()
# project_root = os.path.dirname(cwd)
#
# # Insert the project root dir as the first element in the PYTHONPATH.
# # This lets us ensure that the source package is imported, and that its
# # version is used.
# sys.path.insert(0, project_root)

# -- General configuration ---------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pyramid_watcher'
copyright = u'2019, Paul Everitt'

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = pkg_resources.get_distribution('pyramid_watcher').version
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------

# Add and use Pylons theme
sys.path.append(os.path.abspath('_themes'))
html_theme_path = pylons_sphinx_themes.get_html_themes_path()
html_theme = 'pylons'


html_theme_options = {
    'github_url': 'https://github.com/pauleveritt/pyramid_watcher'
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'pyramid_watcher'

# The name of an image file (relative to this directory) to place at the
# top of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon
# of the docs.  This file should be a Windows icon file (.ico) being
# 16x16 or 32x32 pixels large.
#html_favicon = None
html_static_path = ['_static']
