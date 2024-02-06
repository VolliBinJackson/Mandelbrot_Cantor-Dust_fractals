import os
from gtts import gTTS

try:
    # Set text and language
    text = input("Please Enter a text, which you want to convert to audio: ")
    language = input("Please enter the language you want to hear from the audio ('en' for english, 'de' for german... ")
    path = 'text.txt'
    with open(path, 'w') as datei:
        datei.write(text)

    # Configure and read out text
    f = open(path, "r")
    input_text = f.read().replace("\n", " ")
    voiceline = gTTS(text=input_text, lang=language, slow=False)
    voiceline.save("txt.mp3")
    os.system("start txt.mp3")
except FileNotFoundError:
    print("File not found.")