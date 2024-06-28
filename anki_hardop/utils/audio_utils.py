import ffmpeg
import os
from utils.string_utils import get_dir_filename_without_extension


def convert_to_mp3(input_wav: str):
    file_dir, filename = get_dir_filename_without_extension(input_wav)
    output_mp3_path = os.path.join(file_dir, f"{filename}.mp3")
    {ffmpeg.input(input_wav).output(output_mp3_path, ac=2, audio_bitrate="192k").run()}
