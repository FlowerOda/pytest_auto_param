# -*- coding: utf-8 -*-
'''
@author：  花小田
@datetime：2021-08-19 12:14
@summary： https://github.com/mgeier/pytest-auto-parametrize
'''
import inspect
import pytest
from _pytest.mark import ParameterSet


def auto_parametrize(argvalues, *args, **kwargs):
    """Deduce argument names from function signature.
        The argument values correspond to the function arguments in the
        given order.  Any trailing argument names can be fixtures or
        arguments from ``@pytest.mark.parametrize(...)`` decorators.
        """
    def decorator(func):
        try:
            argvalue = argvalues[0]
        except IndexError:
            raise ValueError('argvalues must be non-empty')
        except TypeError:
            raise TypeError('argvalues must be a sequence')
        argvalue = ParameterSet.extract_from(argvalue).values
        argspec = inspect.getfullargspec(func)[0]
        if 'self' in argspec:
            argspec.remove('self')
        argnames = argspec[:len(argvalue)] if isinstance(argvalue, (list, tuple)) else  argspec[0]
        return pytest.mark.parametrize(
            argnames, argvalues, *args, **kwargs)(func)
    return decorator


def pytest_configure():
    pytest.auto_parametrize = auto_parametrize
