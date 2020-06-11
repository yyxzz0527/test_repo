__author__ = 'daibing'

from OperatingProcedures import OperatingProcedures
from version import VERSION

_version_ = VERSION


class OperatingProcedures(OperatingProcedures):
    """
    This test library provides some keywords to allow
    opening, reading, Test Excel Driver files
    from Robot Framework.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'