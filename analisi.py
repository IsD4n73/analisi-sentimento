from feel_it.feel_it import SentimentClassifier
from feel_it import EmotionClassifier
from gtts import gTTS
from translate import Translator
import speech_recognition as sr
import os

translator= Translator(to_lang="Italian")
r = sr.Recognizer()

emotion_classifier = EmotionClassifier()
sentiment_classifier = SentimentClassifier()



with sr.Microphone() as source:
    print("Di una frase da analizzare... (Hai 5 secondi)")
    try:
        audio_data = r.record(source, duration=5)
        text = r.recognize_google(audio_data, language="it-IT")
        print("Testo da analizzare: " + text + "\n\n")

        emozione = emotion_classifier.predict([text])
        sentimento = sentiment_classifier.predict([text])

        sentimento_it = translator.translate(str(sentimento[0]))
        emozione_it = translator.translate(str(emozione[0]))


        print("Emozione analizzata: " + emozione_it + "\nSentimento analizzato: " + sentimento_it)

        text_to_say = "Emozione analizzata: " + emozione_it + "Sentimento analizzato: " + sentimento_it
        voice = gTTS(text=text_to_say, lang="it", slow=False)

        voice.save("tts.mp3")
        os.system("mpg321 tts.mp3")
        
    except:
        print("Non siamo riusciti ad analizzare l'audio")