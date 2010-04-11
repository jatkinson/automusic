"""
    This file contains all the necessary musical definitions
"""


### Root / Key

[C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B] = [0,1,2,3,4,5,6,7,8,9,10,11]


### Musical Modes: Authentic / Plagal

Lydian = [0, 2, 4, 6, 7, 9, 11, 12]     # Most Pleasing-Sound Scale
Dorain = [0, 2, 3, 5, 7, 9, 10, 12]
Mixolydian = [0, 2, 4, 5, 7, 9, 10, 12]


### Chords

I   = [0, 4, 7]   # Tonic
ii  = [2, 5, 9]   # Supertonic
iii = [0]         # Mediant
IV  = [0]         # Subdominant
V   = [7, 11, 14] # Dominant
Vi  = [0]         # Submediant
VII = [0]         # Subtonic


def minor(chord):
    """
        Return Minor Chord
    """
    chord[1] -= 1
    return chord


def diminish(chord):
    """
        Diminish the chord
    """
    chord[1] -= 1
    chord[2] -= 1
    return chord

def augment(chord):
    """
        Augment the Chord
    """
    chord[2] += 1
    return chord


def getChord(root, chord):
    """
        Return the notes of a given chord
    """
    notes = []
    for note in chord:
        notes.append(root + note)
    return notes


def getMode(key, mode, octave):
    """
        Return the notes of a given mode
    """
    notes = []
    for (note) in range (octave[0] * 12, octave[1] * 12):
        if (note - int(key)) % 12 in mode:
            notes.append(note)
    return notes


def int_to_char(notes):
    """
        Convert notes in integer into notes in characters
    """
    
    d = {0:'C', 1:'Db', 2:'D', 3:'Eb', 4:'E', 5:'F', 6:'Gb', 7:'G',
         8:'Ab', 9:'A', 10:'Bb', 11:'B'}

    if type(notes) == int:
        char_notes = d[notes % 12] + str(notes / 12)
        
    elif type(notes) == list:
        char_notes = []
        for note in notes:
            char_notes.append(d[note % 12] + str(note / 12))

    return char_notes


def detect_key(notes):
    """
        Return the most-likely key of the input notes
        *** Need to be imporved ***
    """
    d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    
    for note in notes:
        d[int(note) % 12] += 1

    if   d[8] > 0: return 'A'  #  A Major : F#, C#, G#
    elif d[6] > 0: return 'D'  #  D Major : F#, C#
    elif d[1] > 0: return 'G'  #  G Major : F#
    else:          return 'C'  #  C Major



if __name__ == '__main__':
    print getMode(C, Lydian, [4,8])
    print int_to_char(minor(getChord(Gb, I)))

    example = '69 68 69 68 69 64 69 62 61 62 64 61'
    print detect_key(example.split(' '))
