# This file is execfile()d with the current directory set to its containing dir.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
import shutil
from time import sleep
import subprocess
import re

# import json

# import sphinx_rtd_theme  # noqa

# -- Custom Python script ----------------------------------------------------
# Run the generate_overview.py script (blocking)
subprocess.run(["python", "../scripts/generate_overviews.py"])

sleep(2.0)

# -- Path setup --------------------------------------------------------------

__location__ = os.path.dirname(__file__)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.join(__location__, "../src"))

# -- Run sphinx-apidoc -------------------------------------------------------
# This hack is necessary since RTD does not issue `sphinx-apidoc` before running
# `sphinx-build -b html . _build/html`. See Issue:
# https://github.com/readthedocs/readthedocs.org/issues/1139
# DON'T FORGET: Check the box "Install your project inside a virtualenv using
# setup.py install" in the RTD Advanced Settings.
# Additionally it helps us to avoid running apidoc manually

try:  # for Sphinx >= 1.7
    from sphinx.ext import apidoc
except ImportError:
    from sphinx import apidoc

output_dir = os.path.join(__location__, "api")
module_dir = os.path.join(__location__, "../src/ac_microcourses")
try:
    shutil.rmtree(output_dir)
except FileNotFoundError:
    pass

try:
    import sphinx

    cmd_line = f"sphinx-apidoc --implicit-namespaces -f -o {output_dir} {module_dir}"

    args = cmd_line.split(" ")
    if tuple(sphinx.__version__.split(".")) >= ("1", "7"):
        # This is a rudimentary parse_version to avoid external dependencies
        args = args[1:]

    apidoc.main(args)
except Exception as e:
    print("Running `sphinx-apidoc` failed!\n{}".format(e))

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.ifconfig",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    # "sphinx_rtd_theme",
    "sphinx_book_theme",
    "sphinx_copybutton",
    "sphinx_design",
    "nbsphinx",
    "nbsphinx_link",
    "sphinx_gallery.load_style",
    # "myst_parser", # auto-activated by myst_nb
    "myst_nb",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# maybe unnecessary now (NOTE: I renamed 2.* files, but have not updated them
# below - not sure if this affects whether these will run or not)
nbsphinx_thumbnails = {
    "courses/hello-world/1.1-running-the-demo": "_static/sdl-demo/star-protocols-graphical-abstract.png",
    "courses/hello-world/1.2-blink-and-read": "_static/sdl-demo/green-led.jpg",
    "courses/hello-world/1.3-bayesian-optimization": "_static/sdl-demo/grid-vs-random-vs-bayesian-ax-logo.png",
    "courses/hello-world/1.4-hardware-software-communication": "_static/mqtt-workflow.png",
    "courses/hello-world/1.5-data-logging": "_static/mongodb.png",
    "courses/hello-world/1.6-connecting-the-pieces": "_static/connecting-pieces.png",
    "courses/hello-world/1.7-convert-to-a-lab-sensor-system": "_static/lab-sensor-system.png",
    "courses/data-science/2.1-gentle-intro-bayesian": "_static/bayes-opt-1d.png",
    "courses/data-science/2.2-multi-objective-opt": "_static/2.2-multi-objective-opt.png",
    "courses/data-science/2.3-constrained-opt": "_static/2.3-constrained-opt.png",
    "courses/data-science/2.4-high-dimensional-opt": "_static/2.4-high-dimensional-opt.png",
    "courses/data-science/2.5-multi-fidelity-opt": "_static/2.5-multi-fidelity-opt.png",
    "courses/data-science/2.6-predefined-candidates": "_static/2.6-predefined-candidates.png",
    "courses/data-science/2.7-benchmarks": "_static/2.7-benchmarks.png",
    "courses/robotics/3.1-pumps-and-pipettes": "_static/3.1-pumps-and-pipettes.png",
    "courses/robotics/3.2-liquid-handlers": "_static/3.2-liquid-handlers.png",
    "courses/robotics/3.3-mobile-robotics": "_static/3.3-mobile-robotics.png",
    "courses/robotics/3.4-computer-vision": "_static/3.4-computer-vision.png",
    "courses/robotics/3.5-solid-sample-transfer": "_static/3.5-solid-sample-transfer.png",
    "courses/software-dev/4.1-vscode-setup": "_static/4.1-vscode-setup.png",
    "courses/software-dev/4.2-vscode-debugging": "_static/4.2-vscode-debugging.png",
    "courses/software-dev/4.3-unit-testing": "_static/4.3-unit-testing.png",
    "courses/software-dev/4.4-automated-docs": "_static/4.4-automated-docs.png",
    "courses/software-dev/4.5-continuous-integration": "_static/4.5-continuous-integration.png",
    "courses/software-dev/4.6-project-templates": "_static/4.6-project-templates.png",
    "courses/software-dev/4.7-cloud-servers": "_static/4.7-cloud-servers.png",
    "courses/software-dev/4.8-cloud-computing": "_static/4.8-cloud-computing.png",
    "courses/capstone/5.1-project-proposal": "_static/5.1-project-proposal.png",
    "courses/capstone/5.2-design-and-execution": "_static/5.2-design-and-execution.png",
    "courses/capstone/5.3-dissemination": "_static/5.3-dissemination.png",
}

# Configure MyST-Parser
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# myst-nb
nb_execution_timeout = 60  # for long-running notebooks (e.g., Bayes opt)
nb_execution_excludepatterns = [
    "1.4-hardware-software-communication.ipynb",  # MicroPython code
    "1.4.1-onboard-led-temp.ipynb",  # assumes a MCU is actively receiving
    "1.5-data-logging.ipynb",  # MicroPython code
    "1.5.3-aws-lambda-read.ipynb",  # just not tested
    "2.*",  # TODO: Bayes opt notebooks
    "3.*",  # TODO: Robotics notebooks
    "4.*",  # TODO: Software dev notebooks
    "5.*",  # TODO: Capstone notebooks
]  # list of patterns

# SMOKE_TEST = os.getenv("SMOKE_TEST")
SMOKE_TEST = True
if SMOKE_TEST:
    nb_execution_excludepatterns += [
        "1.3.1-ax-service-api.ipynb",
        "1.3.2-ax-service-api-basic.ipynb",
        "1.5.1-pymongo.ipynb",
    ]

# with open("variables.json", "r") as f:
#     myst_substitutions = json.load(f)


# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "ac-microcourses"
author = "Sterling G. Baird"
copyright = ["2023, Acceleration Consortium", "2023, Sterling G. Baird"]

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# version: The short X.Y version.
# release: The full version, including alpha/beta/rc tags.
# If you don’t need the separation provided between version and release,
# just set them both to the same value.
try:
    from ac_microcourses import __version__ as version
except ImportError:
    version = ""

if not version or version.lower() == "unknown":
    version = os.getenv("READTHEDOCS_VERSION", "unknown")  # automatically set by RTD

release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If this is True, todo emits a warning for each TODO entries. The default is False.
todo_emit_warnings = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a
# list of builtin themes. Theme options are theme-specific and customize the
# look and feel of a theme further.  For a list of options available for each
# theme, see the documentation.

# tags.add("navigation") # not needed, since ":hidden:" doesn't affect the sidebar
# html_theme = "sphinx_rtd_theme"
# html_theme_options = {
#     "navigation_depth": 2,
#     "collapse_navigation": False,
#     "prev_next_buttons_location": "both",
# }

# html_theme = "alabaster"
# html_theme_options = {
#     # "sidebar_width": "300px",
#     # "page_width": "1200px",
# }

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_provider": "github",
    "repository_url": "https://github.com/AccelerationConsortium/ac-microcourses",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "launch_buttons": {"colab_url": "https://colab.research.google.com"},
    "home_page_in_toc": True,
    "show_navbar_depth": 1,  # Adjust based on your structure
    "navigation_with_keys": True,
    # "navbar_center": ["navbar-nav"], # adds Course 1 / Course 2 buttons at top
}

# html_sidebars = {
#     "path/to/page": [],
# }
# html_theme = "pydata_sphinx_theme"
# html_theme_options = {"show_prev_next": True, "nosidebar": False}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# html_js_files = [
#     "custom.js",
# ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "Acceleration-Consortium-vectortunnel-colour-black-background.png"
html_logo = "logos/Acceleration-Consortium-vectortunnel-colour.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "logos/ac-vector-tunnel-color-black-background-32x32.ico"
# html_favicon = "logos/ac-vector-tunnel-color-32x32.ico"
# html_favicon = "logos/Acceleration-Consortium-vectortunnel-black.ico"
# html_favicon = "logos/Acceleration-Consortium-vectortunnel-colour-black-glow.ico"
# html_favicon = "logos/Acceleration-Consortium-vectortunnel-colour-soft-black-glow.ico"
# html_favicon = "logos/scroll-logo.ico"
# html_favicon = "logos/ac-red-scroll-logo.ico"
# html_favicon = (
#     "logos/Acceleration-Consortium-vectortunnel-colour-circle-black-background.ico"
# )

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# # Function to add custom CSS for specific pages
# def setup(app):
#     app.add_css_file("default.css")  # This will be your default CSS
#     # Inject custom CSS conditionally based on the page
#     app.connect("html-page-context", add_custom_css)
# def add_custom_css(app, pagename, templatename, context, doctree):
#     pattern = re.compile(r"courses/.+/\d+\.\d+(\.\d+)?-.*")
#     if pattern.match(pagename):
#         app.add_css_file("custom.css")
# # Custom CSS files
# html_css_files = [
#     "default.css",
# ]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "ac-microcourses-doc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    # "papersize": "letterpaper",
    # The font size ("10pt", "11pt" or "12pt").
    # "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    # "preamble": "",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "user_guide.tex",
        "ac-microcourses Documentation",
        "Sterling G. Baird",
        "manual",
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = ""

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -- External mapping --------------------------------------------------------
python_version = ".".join(map(str, sys.version_info[0:2]))
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "python": ("https://docs.python.org/" + python_version, None),
    "matplotlib": ("https://matplotlib.org", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "setuptools": ("https://setuptools.pypa.io/en/stable/", None),
    "pyscaffold": ("https://pyscaffold.org/en/stable", None),
}

print(f"loading configurations for {project} {version} ...", file=sys.stderr)
