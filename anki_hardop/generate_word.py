from TTS.api import TTS
from os.path import exists

api = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def generate_word(
        word: str,
        api: TTS = api,
        output_dir: str = "output",
        output_prefix: str = "NL-",
        speaker_wav: str = "speaker/female.wav"
        ):
    output_path = f"{output_dir}/{output_prefix}{word}.wav"

    file_exists = exists(output_path)

    if(file_exists):
        print(f"⏭️ File for the input. {word}, exists on {output_path}. Skipping...")
        return 
    print(f"⌛ Generating: {word} -> {output_path}")
    api.tts_to_file(
        word,
        speaker_wav=speaker_wav,
        file_path=output_path,
        language="nl"
    )