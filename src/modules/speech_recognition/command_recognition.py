import speech_recognition as sr

def recognize_commands(audio_data):
    # Initialize the recognizer
    r = sr.Recognizer()

    # Recognize the commands
    try:
        command = r.recognize_google(audio_data)
        return command.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
