import utils.generate_test as generate_test
import os 
import argparse
import engine

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--file_path", default=os.path.join(os.getcwd(), "test.wav"))
    
    args = parser.parse_args()

    if not os.path.exists(args.file_path):

        raise Exception(f"The Mentioned File Path Does Not Exist: {args.file_path}")
    

    engine_init = engine.Voxil()
    
    engine_init.run(args.file_path)