#wrapper around whisper model for now, to be changed to more sota models later on \

import whisper

class Voxil():

    def __init__(self):
        print("Initializing whisper model")

        self.model = whisper.load_model("turbo")

    
    def run(self, input_path):
        result = self.model.transcribe(input_path)

        print(result['text'])
        

