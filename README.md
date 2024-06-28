# Anki Hardop

<p align="center">
    <b>Learning Dutch made easier with your own voice.</b>
</p>

Generating Dutch audio files for [Anki's Frequency Dictionary of Dutch Deck](https://ankiweb.net/shared/info/1002891444), in your own voice.

## Running a script

```bash
pipenv run python script_that_you_want_to_run.py
```

## Batch converting .wav to .mp3

```bash
cd /path/to/folder/with/wav/files

mkdir mp3

for f in *.wav; do ffmpeg -i "$f" -vn -ar 44100 -ac 2 -b:a 192k "./mp3/${f%.*}.mp3"; done
```

## Updating the Anki media

All Anki media files are stored in one directory. For Mac, it is:

```
~/Library/Application Support/Anki2/User 1/collection.media/
```

After creating the mp3 files, copy and paste them into this directory.
