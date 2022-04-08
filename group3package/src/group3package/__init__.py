# read version from installed package
from importlib.metadata import version
__version__ = version("group3package")

from . import download_data, filter, process_data, regression, remove_column, summary_graph, visualize_data
