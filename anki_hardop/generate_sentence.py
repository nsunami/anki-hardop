from TTS.api import TTS
from os.path import exists
from utils.audio_utils import convert_to_mp3


def generate_sentence(
    sentence: str,
    output_filename: str,
    api: TTS,
    output_dir: str = "output",
    speaker_wav: str = "speaker/female.wav",
):

    output_path = f"{output_dir}/{output_filename}.wav"
    file_exists = exists(output_path)

    if file_exists:
        print(f"⏭️ File for the input. {sentence}, exists on {output_path}. Skipping...")
        return
    print(f"⌛ Generating: {sentence} -> {output_path}")

    api.tts_to_file(
        sentence, speaker_wav=speaker_wav, file_path=output_path, language="nl"
    )

    convert_to_mp3(output_path)
