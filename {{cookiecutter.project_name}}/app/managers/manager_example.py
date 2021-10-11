__all__ = ['Args_Example']

# be sure to include rputils in your environment to allow manager classes to exist
import rputils

from typing import Union
from pathlib import Path

import pandas as pd


# %% MANAGERS
class Args_Example(rputils.ArgManager):
    """
    Example ArgManager class utilized to send arguments through to a method defined
    within the project src package support library --> {{cookiecutter.support_library}}
    """

    def __init__(self, func, **kwargs):
        self.func = func
        self.returned = None
        super().__init__(func=func.function, **kwargs)

    def update(self, year):
        if year <= 2030:
            year = "2018"
        else:
            year = "2060"

    def apply(self, return_=False):
        pass
