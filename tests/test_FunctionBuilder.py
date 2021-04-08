import pytest
from FuncToWav.song_builder import SongBuilder

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

@pytest.mark.parametrize("scale,octave,expected", [
    ['a', '4', 49],
    ['a#', '4', 50],
    ['ab', '4', 48],
    ['g#', '4', 48]
])
def test___keyToNum__(scale, octave, expected):
    fBuilder = SongBuilder()
    assert fBuilder._keyToNum(scale, octave) == expected

def freqToFunc():
    pass

def buildSong():
    pass
