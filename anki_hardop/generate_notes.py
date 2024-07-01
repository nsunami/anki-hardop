from utils.import_utils import read_notes


def generate_notes():
    """Generate new notes file, with the new sentences fields"""
    output_filename = "output/new_notes.txt"

    notes = read_notes()
    sentence_audio_column = notes["Rank"].apply(lambda x: f"[sound:{x}.mp3]")
    notes = notes.assign(e=sentence_audio_column)

    notes.to_csv(output_filename, sep="\t", header=False, index=False)

    with open(output_filename, "r") as file:
        current_notes = file.read()

    with open(output_filename, "w") as file:
        file.write("#separator:tab\n")
        file.write("#html:true\n")
        file.write(current_notes)
