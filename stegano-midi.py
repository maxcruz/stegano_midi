"""Steganography in MIDI files: Hiding messages in MIDI songs

Usage:
  stegano-midi.py --help
  stegano-midi.py --version
  stegano-midi.py --hide --file=<file> --message=<input>...
  stegano-midi.py --reveal --file=<file> [--forget]

Options:
  --hide        Hide a message into the provided midi file
  --reveal      Reveal hidden messages
  --help        Show this screen.
  --version     Show version.

Examples:
  stegano-midi.py --hide --file=pachelbel_canon.mid --message="Top Secret"
  stegano-midi.py --reveal --file=pachelbel_canon.mid

"""

from docopt import docopt
import midi

VERSION = 1.0


# Hide a secret
def hide_message(midi_file, message):
    print ("Hide message: \"" + message + "\" in " + midi_file)
    try:

        # Read midi file
        tracks = midi.read_midifile(midi_file)

        # If the midi doesn't have tracks add one
        if len(tracks) == 0:
            tracks.append(midi.Track)

        # Instantiate a MIDI note off event, append it to the track
        off = midi.NoteOffEvent(tick=0, pitch=midi.G_3)
        tracks[0].insert(0, off)

        # Iterate message characters and insert them as program change event
        for character in message:
            change_program = midi.ProgramChangeEvent(tick=0, data=[ord(character)])
            tracks[0].insert(0, change_program)

        # Instantiate a MIDI note on event, append it to the track
        on = midi.NoteOnEvent(tick=0, pitch=midi.G_3)
        tracks[0].insert(0, on)

        # Save the pattern to disk
        midi.write_midifile(midi_file, tracks)

    except IOError:
        print ("Error reading the input file")


# Reveal a secret
def reveal_message(midi_file, forget):
    print ("Reveal message in " + midi_file)

    # Read midi file
    tracks = midi.read_midifile(midi_file)

    # Define a map and an index to store secrets
    secrets = {}
    secret_index = 0
    forget_indexes = list()

    # Iterate track events
    for event in tracks[0]:
        i = 0

        # When find on event with specific characteristics, create a list in the map
        if isinstance(event, midi.NoteOnEvent) and event.tick == 0 and event.get_pitch() == midi.G_3:
            secrets[secret_index] = list()
            forget_indexes.append(i)

        # If find program change event store the character for the word into the map
        if isinstance(event, midi.ProgramChangeEvent) and event.tick == 0:
            secrets[secret_index].append(event.data[0])
            forget_indexes.append(i)

        # When find off event with specific characteristics, increment the index to store the next secret
        if isinstance(event, midi.NoteOffEvent) and event.tick == 0 and event.get_pitch() == midi.G_3:
            secret_index += 1
            forget_indexes.append(i)

        # Increment list index
        i += 1

    # Iterate the secrets collected
    for i in secrets:
        secret = ''

        # Join characters
        for char in reversed(secrets[i]):
            secret = secret + chr(char)

        # Print the secret
        print (secret)

    # Forget secrets
    if forget:
        for i in forget_indexes:
            tracks[0].pop(i)

        midi.write_midifile(midi_file, tracks)


# Main function
if __name__ == '__main__':

    # Set version
    options = docopt(__doc__, version=VERSION)

    # Read arguments
    arguments = docopt(__doc__)

    # If the command hide is called
    if arguments['--hide']:
        hide_message(arguments['--file'], arguments['--message'][0])

    # If the command reveal is called
    if arguments['--reveal']:
        reveal_message(arguments['--file'], arguments['--forget'])
