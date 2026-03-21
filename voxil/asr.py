#asr module: whisper for now, to be changed with something sota soon

import whisper
import os
from dataclasses import dataclass, asdict, field
from typing import List, Optional, ClassVar
import json
import logging
import json
from pprint import pprint

#configure logging

logging.basicConfig(level=logging.INFO)


@dataclass
class asr_schema:
    id: int
    text: str
    start:float
    end:float
    speaker: Optional[str] = None

@dataclass
class asr_result:
    model: str
    result: list = field(default_factory=list)
    


AVAILABLE_MODELS = ['tiny', 'base', 'small', 'medium', 'large', 'turbo']
class whisper_asr():

    #initialize
    def __init__(self, model = "turbo", ):
        self.available_models = AVAILABLE_MODELS

        if model not in self.available_models:
            raise Exception(f"Invalid model name mentioned: {model} \n Available models are {self.available_models}")
        
        logging.info(f"Initializing whisper model: {model}")
        self.model_name = model
        self.model = whisper.load_model(model)

    #running the model
    def run(self, input_path = "../test/test.wav", save=False, save_path = "../test", format = 'text'):
        result = self.model.transcribe(input_path)



        

        asr_result_obj = asr_result(model=self.model_name)
        
 

        for i,segment in enumerate(result['segments']):


        
            temp_asr_schema = asr_schema(id = i, text = segment['text'], start=segment['start'], end = segment['end'])
      
            asr_result_obj.result.append(asdict(temp_asr_schema))


        if save:

            if format == 'text':
                op_path = os.path.join(save_path, 'output_file.txt')
                with open(op_path, 'w') as file:
                    file.writelines(result['text'])
                
                logging.info(f"Text file created and saved at {op_path}")

            elif format == 'json' :
                op_path = os.path.join(save_path, 'output_file.json')
                with open(op_path, 'w') as file:
                    json.dump(asdict(asr_result_obj), file, ensure_ascii= False, indent=4)
                
                logging.info(f"Json file created and saved at {op_path}")

        return asr_result_obj
    
    
    

        



