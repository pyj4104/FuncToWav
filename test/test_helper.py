import pytest
from extended_int import int_inf
from functools import reduce
from FuncToWav.helper import heaviside, combineFuncs

@pytest.mark.parametrize("x,sTime,eTime,expected",[
    [0, 0, 5, 1],
    [5, 0, 5, 1],
    [-1, 0, 5, 0],
    [6, 0, 5, 0],
    [0, 0, int_inf, 1],
    [10000, 0, int_inf, 1],
    [-1, 0, int_inf, 0],
    [1000000000000000, 0, int_inf, 1],
    [0.5, 0, int_inf, 1],
])
def test_heaviside(x, sTime, eTime, expected):
    assert heaviside(x, sTime, eTime) == expected

@pytest.mark.parametrize("a,b,expected",[
    [lambda x: x+x, lambda x: x+x, lambda x: 4*x],
])
def test_combineFuncs(a, b, expected):
    xs = list(range(100))
    for x in zip(xs):
        assert combineFuncs(a, b)(x) == expected(x)

@pytest.mark.parametrize("x",[
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
def test_reduce(x):
    funcs = [
        lambda x: x+x,
        lambda x: x+x,
        lambda x: x+x,
        lambda x: x+x,
    ]
    newFunc = reduce(combineFuncs, funcs)
    assert newFunc(x) == 8*x
