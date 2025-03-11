from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        text = f"Sorry, there was an error with the Google Speech Recognition service; {e}"

    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
