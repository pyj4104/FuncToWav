import numpy
from extended_int import int_inf
from math import sin
from song_builder import heaviside
from typing import Callable

keyToNum = {
    'c': 0,
    'c#': 1,
    'd': 2,
    'd#': 3,
    'e': 4,
    'f': 5,
    'f#': 6,
    'g': 7,
    'g#': 8,
    'a': 9,
    'a#': 10,
    'b': 11
}

class SongBuilder:
    length: int
    sampleRate: int
    song: []

    def __init__(self):
        self.song = []
        self.sampleRate = 48000
        self.length = 0

    def appendToSong(self, key: str, startTime: int, duration: int = None, endTime: int = int_inf):
        if (duration == None) and (endTime == int_inf):
            endTime = int_inf
        elif (duration == None) and (endTime != int_inf):
            endTime = endTime
            self.length = self.length if self.length >= starTime+duration else starTime+duration
        elif (duration != None) and (endTime == int_inf):
            endTime = startTime+duration
            self.length = self.length if self.length >= starTime+duration else starTime+duration
        else:
            if startTime+duration != endTime:
                raise ValueError("the note duration + note start timing must match end timing")

        part = {
            "freq": self.numToFreq(self.keyToNum(key)),
            "startTime": startTime,
            "endTime": endTime
        }
        self.song.append(part)
    
    def freqToFunc(self, part: dict) -> Callable[[int], float]:
        freq = part["freq"]
        sTime = part["startTime"]
        eTime = part["eTime"]
        return lambda x: sin(freq * x) *

    def numToFreq(self, num: int) -> float:
        return round((2**((num-49)/12)*440),3)

    def keyToNum(self, key: str) -> int:
        if len(key) == 3:
            scale = key[:2]
            octave = key[2]
        elif len(key) == 2:
            scale = key[0]
            octave = key[1]
        elif len(key) == 1:
            scale = key
            octave = 4
        else:
            raise ValueError("It's not possible to convert the input to key number")

        return self.__keyToNum__(scale, octave)

    def __keyToNum__(self, scale: str, octave: str) -> int:
        print(scale)
        if scale.lower() not in keyToNum:
            raise ValueError("The letter code is not one of the scale")
        
        num = int(octave)*12+keyToNum[scale.lower()]-8

        if num < 1 or num > 88:
            raise ValueError("Unsupported tone")

        return num
