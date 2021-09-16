# -*- coding: utf-8 -*-
'''
@author：  花小田
@datetime：2021/8/19 14:47
@summary： 避免在pytest.mark.parametrize参数化中编写重复参数
'''
import pytest

testparams = [
    (1, 2, 3, 4, 5, 6, 7),
    (7, 6, 5, 4, 3, 2, 1),
]

class TestAutoParam:

    @pytest.mark.parametrize('a, b, c, d, e, f, g', testparams)
    def test_many_args_old(self,a, b, c, d, e, f, g):
        assert a+b+c+d+e+f+g==28

    @pytest.auto_parametrize(testparams,ids=['test data 1','test data 2'])
    def test_many_args_new(self,a, b, c, d, e, f, g):
        assert a+b+c+d+e+f+g==28



