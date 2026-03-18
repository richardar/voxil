
#generate a audio test file to see how good the model is and how it can be used.

import pyttsx3

print("initialising pyttsx3 for test generation")

engine = pyttsx3.init()

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

engine.save_to_file(text, "../test/test.wav")

engine.runAndWait()