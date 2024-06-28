import argparse
from anki_hardop import main


def parse_args():
    parser = argparse.ArgumentParser(description="MyPackage CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    parser.add_argument("--option", type=str, help="An option for the main function")
    # Sentence
    sentence_parser = subparsers.add_parser(
        "sentence", help="Generate sentences from an Anki note file"
    )
    sentence_parser.add_argument("sentence", type=str, help="Anki note file")

    # Word
    word_parser = subparsers.add_parser(
        "word", help="Generate words given an Anki note file"
    )
    word_parser.add_argument(type=str, help="Generate sentence given an Anki note file")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "sentence":
        generate_sentences(args.sentence)
    main(option=args.option)


if __name__ == "__main__":
    main()
