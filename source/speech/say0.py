'''
https://github.com/nateshmbhat/pyttsx3
'''

import pyttsx3

# to initialize the library
# why? because thats just how the programmer designed it
engine = pyttsx3.init()

# I can use this engine to say things
engine.say("Chef Cities dot com is a great website!")

# then I will run this engine and wait for it before my program quits
engine.runAndWait()

