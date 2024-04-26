import googletrans
import random

translator = googletrans.Translator()
newSentence = ""

while True:
    i = 0
    # responce = input('Say something to translate!\n')
    # languagesToTranslate = int(input("How many times do you want it to translate? (MUST BE A NUMBER)\n"))
    responce = "We're no strangers to love You know the rules and so do I (do I) A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you"
    languagesToTranslate = 100
    while i < languagesToTranslate:
        newSentence = translator.translate(responce, dest=random.choice(list(googletrans.LANGUAGES))).text
        print('Progres: ' + str(i) + '/' + str(languagesToTranslate))
        i += 1
    print(newSentence)
