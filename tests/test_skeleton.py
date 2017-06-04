#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from ginebig.skeleton import fib

__author__ = "Randal J. Barnes"
__copyright__ = "Randal J. Barnes"
__license__ = "new-bsd"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)