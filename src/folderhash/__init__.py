"""Compare folder contents via hash."""
__version__ = '1.0.0'

__title__ = 'folderhash'
# keep the __description__ synchronized with the module docstring
__description__ = 'Compare folder contents via hash.'
__url__ = 'https://github.com/scolby33/folderhash'

__author__ = 'Scott Colby'
__email__ = 'scolby33@gmail.com'

__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2017 Scott Colby'

# perform project imports here, e.g.
# from . import a_module
# from .b_module import Class, function
from .cli import main as cli

__all__ = [cli]
