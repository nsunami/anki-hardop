import os
import re


def complete_parentheses(text):
    completed_text = re.sub(r"(?<!\()(.)(\))", r"(\1)", text)
    return completed_text


def remove_html_tags(text):
    text_without_tags = re.sub(r"<([^>]+)>", " ", text)
    return text_without_tags


def get_dir_filename_without_extension(file_path):
    file_dir, _ = os.path.split(file_path)
    filename = os.path.basename(file_path)  # Get the file name from the path
    name_without_ext = os.path.splitext(filename)[
        0
    ]  # Split the file name and extension
    return file_dir, name_without_ext
