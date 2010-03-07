from MidiOutFile import MidiOutFile
import random

out_file = 'test.mid'
midi = MidiOutFile(out_file)

# non optional midi framework
midi.header(0, 1, 480)
midi.start_of_track()
midi.sequence_name('')
midi.tempo(750000)
midi.time_signature(4, 2, 24, 8)

# Chanel Definition
melody_ch = 0
base_ch = 1

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

def play_chord(ch, chord, duration = 350):
    for note in chord:
        midi.update_time(0)
        midi.note_on(ch, note)
        midi.update_time(duration)
        midi.note_off(ch, note)
        midi.update_time(0)

def play_note(ch, note, duration = 350):
    midi.update_time(0)
    midi.note_on(ch, note)
    midi.update_time(duration)
    midi.note_off(ch, note)
    midi.update_time(0)

def play_chord_note1(ch, scale, chord, duration = 192):
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


def play_chord_note2(ch, scale, chord, duration = 192):
    for i in range(4):
        midi.update_time(0)
        note = random.choice(scale)
        midi.note_on(0, note)
        midi.note_on(0, chord[i])

        midi.update_time(duration / 2)
        midi.note_off(0, note)
        midi.note_off(0, chord[i])
        
    for j in range(4):
        midi.update_time(j)
        midi.note_on(0,chord[j])
        midi.update_time(duration)
        midi.note_off(0, chord[j])       

                      

################# Musical events #########


### Melody
##for i in range(4 * 5):
##    note = random.choice(AMajor_Dorian)
##    play_note(base_ch, note)
##    
### Base
##for i in range(5):
##    play_chord(base_ch, ShaneChord1)
##    play_chord(base_ch, ShaneChord2)
##    play_chord(base_ch, ShaneChord3)
##    play_chord(base_ch, ShaneChord4)
##
# Mix2
for i in range (5):
    play_chord_note1(0, AMajor_Dorian1, ShaneChord1)
    play_chord_note1(0, AMajor_Dorian2, ShaneChord2)
    play_chord_note1(0, AMajor_Dorian3, ShaneChord3)
    play_chord_note1(0, AMajor_Dorian4, ShaneChord4)
##
### Mix
##for i in range (4):
##    midi.update_time(0)
##    note = random.choice(AMajor_Dorian1)
##    midi.note_on(0, note)
##    midi.note_on(0, ShaneChord1[i])
##    
##    midi.update_time(200)
##    midi.note_off(0, note)
##    midi.note_off(0, ShaneChord1[i])
##
##for i in range (4):
##    midi.update_time(0)
##    note = random.choice(AMajor_Dorian2)
##    midi.note_on(0, note)
##    midi.note_on(0, ShaneChord2[i])
##    
##    midi.update_time(200)
##    midi.note_off(0, note)
##    midi.note_off(0, ShaneChord2[i])
##
##for i in range (4):
##    midi.update_time(0)
##    note = random.choice(AMajor_Dorian3)
##    midi.note_on(0, note)
##    midi.note_on(0, ShaneChord3[i])
##    
##    midi.update_time(200)
##    midi.note_off(0, note)
##    midi.note_off(0, ShaneChord3[i])
##
##for i in range (4):
##    midi.update_time(0)
##    note = random.choice(AMajor_Dorian4)
##    midi.note_on(0, note)
##    midi.note_on(0, ShaneChord4[i])
##    
##    midi.update_time(200)
##    midi.note_off(0, note)
##    midi.note_off(0, ShaneChord4[i])
##
##
##                      
### Mix 3
##
##for i in range (5):
##    play_chord_note2(0, AMajor_Dorian1, ShaneChord1)
##    play_chord_note2(0, AMajor_Dorian2, ShaneChord2)
##    play_chord_note2(0, AMajor_Dorian3, ShaneChord3)
##    play_chord_note2(0, AMajor_Dorian4, ShaneChord4)



# non optional midi framework
midi.update_time(0)
midi.end_of_track()

midi.eof()
