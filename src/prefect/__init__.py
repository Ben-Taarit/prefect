# Setup version and path constants

from . import _version
import pathlib

__version__ = _version.get_versions()["version"]
# The absolute path to this module
__module_path__ = pathlib.Path(__file__).parent
# The absolute path to the root of the repository
__root_path__ = __module_path__.parents[1]
# The absolute path to the built UI within the Python module
__ui_static_path__ = __module_path__ / "orion" / "ui"

del _version

# User-facing API
# For details on the import syntax, see https://github.com/microsoft/pyright/blob/main/docs/typed-libraries.md#library-interface

from .logging.loggers import get_run_logger
from .orion.schemas.states import State
from .flows import flow
from .tasks import task
from .context import tags

# Import the serializers so they are registered
import prefect.serializers

# Iniitialize the process level profile at import time
import prefect.context

prefect.context.initialize_module_profile()
