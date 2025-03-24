import numpy as np
import sounddevice as sd

sample_rate = 44100  
duration = 0.5  

A4_freq = 440.0
semitone_ratio = 2 ** (1/12)

note_offsets = {
    "c": -9,
    "c#": -8,
    "d": -7,
    "d#": -6,
    "e": -5,
    "f": -4,
    "f#": -3,
    "g": -2,
    "g#": -1,
    "a": 0,
    "a#": 1,
    "b": 2
}

notes = {}

# Generate notes across octaves 1 to 7
for octave in range(1, 8):
    for note, offset in note_offsets.items():
        note_name = f"{note}{octave}"
        frequency = A4_freq * (semitone_ratio ** (offset + (octave - 4) * 12))
        notes[note_name] = frequency

def play_tone(frequency, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    sd.play(wave, sample_rate)
    sd.wait()

while True:
    text = input("Enter notes (like a5 d5 a5 d5) or 'quit' to exit: ").lower()
    if text == "quit":
        break

    note_list = text.split()
    
    for note in note_list:
        if note in notes:
            play_tone(notes[note], duration)
        else:
            print(f"Invalid note: {note}. Use format like c4, g#5, etc.")
            break
