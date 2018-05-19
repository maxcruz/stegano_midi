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

## Licencia
```
The MIT License (MIT)

Copyright (c) 2018 Max Cruz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

