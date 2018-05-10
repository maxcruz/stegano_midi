# Steganography in MIDI files

Steganography is dealing with the study and application of techniques that allow hiding messages or objects, inside others, called carriers, so that their existence is not perceived. This script is for academic purposes.

This program hide messages inside of MIDI files. MIDI files have events, most of them can be heard, but someones only are used to control configurations in the device. This script abuse the message "Program Change"  to hide a short note in the MIDI file.

## Dependencies

docopt For the command line interface
python-midi To manipulate the midi file

## Usage

Print the help for the command:
```
stegano-midi.py --help
```

Print the version
```
stegano-midi.py --version
```

Hide a message in the MIDI file
```
stegano-midi.py --hide --file=<file> --message=<input>...

# Example
stegano-midi.py --hide --file=pachelbel_canon.mid --message="Top Secret"
```

Reveal message hidden in the file
```
stegano-midi.py --reveal --file=<file> [--forget]

# Example
stegano-midi.py --reveal --file=pachelbel_canon.mid
```

Forget parameter reveal the message and remove it from the file
