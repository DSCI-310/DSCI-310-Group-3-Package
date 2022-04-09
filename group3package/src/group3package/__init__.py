# read version from installed package
from importlib.metadata import version
__version__ = version("group3package")

from . import filter, regression, remove_column
