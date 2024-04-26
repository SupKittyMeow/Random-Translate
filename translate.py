import googletrans
import random

translator = googletrans.Translator()
newSentence = ""

while True:
    i = 0
    responce = input('Say something to translate!\n')
    languagesToTranslate = int(input("How many times do you want it to translate? (MUST BE A NUMBER)\n"))
    while i < languagesToTranslate:
        newSentence = translator.translate(responce, dest=random.choice(list(googletrans.LANGUAGES))).text
        print('Progres: ' + str(i) + '/' + str(languagesToTranslate))
        i += 1
    print(newSentence)