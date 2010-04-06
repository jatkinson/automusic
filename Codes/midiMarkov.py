from modified_MidiToText import MidiToText
from modified_MidiInFile import MidiInFile
from MidiOutFile import MidiOutFile
from playChord import *

import sys
import random
import string

def generate_DB(midiText, d, n):
    """
        Generate and return a Markov DB (dictionary)
        - Key   : prevNote tuple (n : number of previous notes)
        - Value : nextNote tuple
    """
    
    prevNote = tuple()
    t = tuple(midiText.replace('None', ' ').split())

    # Create a dictionary of (prefix : suffix)
    for i in range(len(t) - n):
        prevNote = t[i : i+n]
        d[prevNote] = d.get(prevNote, tuple()) + (t[i+n],)

    return d


def generate_text(DB, num_notes):
    """
        Generate a new text of length (num_words)
        based on the input dictionary DB
    """
    
    # Randomly initialize prefix from DB
    prevNote = random.choice(DB.keys())
    text = ""

    # Repeat choosing a suffix from DB, and append suffix to the text
    for i in range (num_notes):
        
        # Choose next Note randomly from prevNotes DB
        nextNote = random.choice(DB.get(prevNote))

        # Add next note to the text
        text = text + " " +  nextNote

        # Get a new prefix
        prevNote = shift(prevNote, nextNote)

    return text


def shift(prefix, suffix):
    """
        Return a new prefix that contains suffix
    """
    return prefix[1:] + (suffix,)
    


def play_music(text, out_file):
    """
        Play the music based on the text
    """
    midi = MidiOutFile(out_file)
    midi.header()
    midi.start_of_track()

    for note in text.split(' '):
        if note == '': pass
        else:
            midi.update_time(0)
            midi.note_on(channel = 0, note = int(note))

            midi.update_time(48)
            midi.note_off(channel = 0, note = int(note))

    midi.update_time(0)
    midi.end_of_track()
    midi.eof()

    
    
if __name__ == '__main__':

    """
        Step 1 : Generate Markov DB (dictionary) from the file input
        Step 2 : Generate text (string) based on the DB
        Step 3 : Play Music based on the text
    """

    # get data
    test_file = 'test/midifiles/river flows in you.mid'
    
    # do parsing
    midi_in = MidiInFile(MidiToText(), test_file)
    d = dict()
    
    len_prevNotes = 2
    num_notes = 100

    # Step 1
    DB = generate_DB(midi_in.read(), d, len_prevNotes)

    # Step 2
    text = generate_text(DB, num_notes)

    # Step 3
    play_music(text, test_file.split('.')[0] + '_markoved.mid')
    
    
