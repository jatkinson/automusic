# Chord Progression
ShaneChord1 = [66 - 24, 73 - 24, 78 - 24, 73 - 24]
ShaneChord2 = [62 - 24, 69 - 24, 74 - 24, 69 - 24]
ShaneChord3 = [57 - 24, 64 - 24, 69 - 24, 64 - 24]
ShaneChord4 = [64 - 24, 71 - 24, 76 - 24, 71 - 24]

# Dorian Scale
AMajor_Dorian = [57, 59, 61, 62, 64, 66, 68, 69, 71, 73, 74, 76, 78, 80]
AMajor_Dorian1 = [57, 61, 64, 66, 68, 69, 73, 76, 78, 80]
AMajor_Dorian2 = [57, 61, 62, 64, 66, 69, 73, 74, 76, 78]
AMajor_Dorian3 = [57, 61, 64, 66, 68, 69, 73, 74, 78, 80]
AMajor_Dorian4 = [57, 59, 62, 64, 68, 69, 71, 74, 76, 80]

def play_chord(midi, ch, chord, duration = 350):
    for note in chord:
        midi.update_time(0)
        midi.note_on(ch, note)
        midi.update_time(duration)
        midi.note_off(ch, note)
        midi.update_time(0)

def play_note(midi, ch, note, duration = 350):
    midi.update_time(0)
    midi.note_on(ch, note)
    midi.update_time(duration)
    midi.note_off(ch, note)
    midi.update_time(0)


def play_chord_note1(midi, ch, scale, chord, duration = 192):
    for i in range (4):
        midi.update_time(0)
        note = random.choice(scale)
        midi.note_on(0, note)
        midi.note_on(0, chord[i])

        midi.update_time(duration)
        midi.note_off(0, note)
        
    midi.note_off(0, chord[0])
    midi.note_off(0, chord[1])
    midi.note_off(0, chord[2])
    midi.note_off(0, chord[3])
