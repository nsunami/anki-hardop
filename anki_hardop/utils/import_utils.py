import pandas as pd
import io


def extract_words_from_mp3_files_list(mp3_files_list: str = "data/audio_list.txt"):
    """Extract a Dutch word from the list of mp3 filenames, formatted 'Nl-[word].mp3'"""
    with open(mp3_files_list, "r") as file:
        audio_files = file.readlines()
    words = []
    for i, audio_file in enumerate(audio_files):
        current_word = audio_file.removeprefix("Nl-").removesuffix(".mp3\n")
        words.append(current_word)

    return words


def read_notes(notes_file: str = "data/anki/freq_dict_dutch_notes.txt"):
    """Import the Notes export from Anki and convert it to pandas DataFrame"""
    with open(notes_file, "r") as file:
        notes_lines = file.readlines()

    ANKI_NOTES_HEADER_LENGTH = 3
    notes_raw = notes_lines[ANKI_NOTES_HEADER_LENGTH:]

    notes_header = [
        "Rank",
        "Word",
        "Part-of-Speech",
        "Definition",
        "Dutch",
        "English",
        "Freq",
        "Word Audio",
        "Tags",
    ]
    notes_df = pd.read_table(io.StringIO("".join(notes_raw)), names=notes_header)

    return notes_df


def load_sentences(notes_file: str = "data/freq_dict_dutch_notes.txt"):
    """From the Notes, extract the Rank (ID) and Dutch sentences"""
    notes = read_notes(notes_file=notes_file)
    sentences_raw = notes[["Rank", "Dutch"]]
    return sentences_raw
