from utils.import_utils import load_sentences
from generate_sentence import generate_sentence
from utils.string_utils import complete_parentheses, remove_html_tags

from TTS.api import TTS


def generate_sentences(
    notes_file: str = "data/freq_dict_dutch_notes.txt",
    output_dir: str = "sentences",
    speaker_wav: str = "speaker/pinay_english_dynamic.wav",
):

    api = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    sentences = load_sentences(notes_file=notes_file)

    for index, row in sentences.iterrows():
        rank_card_id = row["Rank"]
        sentence = row["Dutch"]

        print(f"{index} / {len(sentences)}")

        sentence = complete_parentheses(sentence)
        sentence = remove_html_tags(sentence)

        generate_sentence(
            api=api,
            sentence=sentence,
            output_filename=rank_card_id,
            output_dir=output_dir,
            speaker_wav=speaker_wav,
        )
