
Text to Speech converter to convert Wikipedia pages to audio files.

### How To Use :

Instructions how to use the script:

Installing Prerequisite:

```
pip install requirements.txt
```

Run the script:

```
python tts.py
```

Choose a option:

```
Choose from following:
1. TTS a text file from the machine
2. Use the URL to TTS the content
3. Exit
2
```

Provide the URL of the Wikipedia page:

```
Enter the url to scrap:
https://en.wikipedia.org/wiki/Python_(programming_language)

```

Audio encoding will start:

```

Audio Encoding Started!

```

Audio file created and ready to play:

```
Audio saved as 'output.mp3'

Enter 1 if you want to play the audio right now!
1

```

Pressing 1 would result in playing the audio file with the deafult audio player!


## Built With

* [python](https://docs.python.org/3/) - Programming Language
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web Scrapping
* [gTTS](https://gtts.readthedocs.io/en/latest/) - Google Text to Speech
