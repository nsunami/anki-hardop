from utils.import_utils import extract_words_from_mp3_files_list
from generate_word import generate_word


def generate_words(
    mp3_files_list: str = "data/audio_list.txt",
    speaker_wav: str = "speaker/pinay_english_dynamic.wav",
    output_dir: str = "words",
):

    words = extract_words_from_mp3_files_list(mp3_files_list=mp3_files_list)

    for word in words:
        generate_word(word, output_dir=output_dir, speaker_wav=speaker_wav)
