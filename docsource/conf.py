# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "Teext"
copyright = "2020, PAL"
author = "PAL"


# -- General configuration ---------------------------------------------------

autoclass_content = "class"  # include both class docstring and __init__
autodoc_default_options = {
    # Make sure that any autodoc declarations show the right members
    "members": True,
    "inherited-members": True,
    "show-inheritance": True,
    "autosummary": True,
    "autosummary-no-nesting": True,
}
autodoc_typehints = "description"
napoleon_numpy_docstring = False  # Force consistency, leave only Google
napoleon_use_rtype = False  # More legible
add_module_names = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Need the autodoc and autosummary packages to generate our docs.
    "sphinx.ext.autodoc",
    # 'sphinx.ext.autosummary',
    # The Napoleon extension allows for nicer argument formatting.
    "sphinx.ext.napoleon",
    "autodocsumm",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
