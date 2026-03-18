#asr module: whisper for now, to be changed with something sota soon

import whisper
import os



AVAILABLE_MODELS = ['tiny', 'base', 'small', 'medium', 'large', 'turbo']
class whisper_asr():

    def __init__(self, model = "turbo"):
        self.available_models = AVAILABLE_MODELS

        if model not in self.available_models:
            raise Exception(f"Invalid model name mentioned: {model} \n Available models are {self.available_models}")
        
        print(f"Initializing whisper model: {model}")

        self.model = whisper.load_model(model)

    
    def run(self, input_path = "../test/test.wav", save=False, save_path = "../test"):
        result = self.model.transcribe(input_path)


        if save:
            with open(os.path.join(save_path, 'output_file.txt'), 'w') as file:
                file.writelines(result['text'])
            
            print("File created and saved")

        
                

        return result['text']
    
    
    

        



