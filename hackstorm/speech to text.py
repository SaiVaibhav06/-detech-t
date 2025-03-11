import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Sorry, there was an error with the Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    recognize_speech_from_mic()
