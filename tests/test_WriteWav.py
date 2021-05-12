from FuncToWav.write_wav import WriteWav
from FuncToWav.song_builder import SongBuilder

def test_writeHeader():
    wavFileGen = WriteWav(1, 'testHeader')
    wavFileGen.createFile()

def test_writeSong():
    sb = SongBuilder()
    sb.appendToSong("c5", 0, endTime=0.5)
    sb.appendToSong("b4", 0.5, endTime=0.75)
    sb.appendToSong("a4", 0.75, endTime=1)
    sb.appendToSong("g4", 1, endTime=1.5)
    sb.appendToSong("f4", 1.5, endTime=2)
    sb.appendToSong("e4", 2, endTime=2.5)
    sb.appendToSong("d4", 2.5, endTime=3)
    sb.appendToSong("c4", 3, endTime=4)
    song = sb.buildSong()
    print(sb.length)
    wavFileGen = WriteWav(sb.length, 'testSong')
    wavFileGen.createFile()
    wavFileGen.appendData(song)
