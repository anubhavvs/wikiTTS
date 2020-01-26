from gtts import gTTS
import os
import bs4
import requests

language = "en"


def texttospeech():
    data = open("data.txt", "r", encoding="utf-8")
    textdata = data.read().replace("\n", " ")
    output = gTTS(text=textdata, lang=language, slow=False)
    print("Audio Encoding Started!")
    output.save("output.mp3")
    print("Audio saved as 'output.mp3'\n")
    play = int(input("Enter 1 if you want to play the audio right now!\n"))
    if play == 1:
        os.system("start output.mp3")
    else:
        print("Audio can be played form the same directory!\n")
    data.close()


def webscrap(x):
    res = requests.get(x)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    data = open("data.txt", "a", encoding="utf-8")
    for i in soup.find_all('p'):
        data.write(str(i.text))
    data.close()
    texttospeech()


choice = 1

while choice == 1:
    choice = int(input(
        "Choose from following:\n"
        "1. TTS a text file from the machine\n"
        "2. Use the URL to TTS the content\n"
        "3. Exit\n"
    ))

    if choice == 1:
        flag = int(input("Store the text as 'data.txt' file in the same directory as this script!\n"
                         "Press 1 after you have created the file!\n"))
        if flag == 1:
            texttospeech()

    if choice == 2:
        url = input("Enter the url to scrap:\n")
        webscrap(url)

    if choice == 3:
        print("Program closing.\n")
        choice = 0

    else:
        print("Only choose from the list!\n")
