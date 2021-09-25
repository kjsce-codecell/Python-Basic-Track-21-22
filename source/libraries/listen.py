'''
https://github.com/Uberi/speech_recognition
'''
import speech_recognition
from pyttsx3 import speak 

# just to know which microphone to use
for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


recognizer = speech_recognition.Recognizer()

# Obtain audio from the microphone
with speech_recognition.Microphone(device_index=2) as source:
    # recognizer.adjust_for_ambient_noise(source, 1)
    print("Listening....")
    speak("listening")

    # listen for audio
    audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

try:
    print("Recognizing...")

    # send it to Google to parse the audio to text
    query = recognizer.recognize_google(audio, language='en-in')
    print(f"You said: {query}\n ")

# error handling

# incase user said nothing
except speech_recognition.UnknownValueError:
    speak("Could not hear that, Try saying again")

# incase the computer did not have internet access
except speech_recognition.RequestError:
    speak("Make Sure that you have a good Internet connection")
    
