#cli interface for voxil

import argparse
from voxil import asr


if __name__ == "__main__" :


    
    parser = argparse.ArgumentParser()

    parser.add_argument("--audio_path", default="../test/test.wav", help="Audio file ppath")

    parser.add_argument("--model", default="turbo", help= f"Name of the model to be used, Currently available models are {asr.AVAILABLE_MODELS}")


    parser.add_argument('--save', action=argparse.BooleanOptionalAction)

    parser.add_argument('--save_path', default="./test/")

    parser.add_argument('--format', default='text', help="Data format to save the output in, Available options are 'text' and 'json' ")
    args = parser.parse_args()
    recognisor = asr.whisper_asr(args.model)

    recognisor.run(input_path=args.audio_path, save=args.save ,save_path=args.save_path, format = args.format)