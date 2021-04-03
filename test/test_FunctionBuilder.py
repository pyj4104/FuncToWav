import pytest
from song_builder.function_builder import SongBuilder

@pytest.mark.parametrize("input,expected",[
    ["a4", 49],
    ["A4", 49],
    ["a0", 1],
    ["c8", 88]
])
def test_keyToNum(input, expected):
    fBuilder = SongBuilder()
    assert fBuilder.keyToNum(input) == expected

@pytest.mark.parametrize("input,expected",[
    [49, 440.000],
    [1,27.500],
    [88,4186.009]
])
def test_numToFreq(input, expected):
    fBuilder = SongBuilder()
    assert fBuilder.numToFreq(input) == expected
