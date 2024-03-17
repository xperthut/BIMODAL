import torch
import numpy as np
import pandas as pd
import argparse
from main_preprocessor import preprocess_data
import warnings
warnings.filterwarnings('ignore')

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    # filename_in='../data/getter_smiles_KP_V1',starting_point='random', min_len=14, max_len=74,augmentation=10
    parser.add_argument('--filename', type=str,
                        help="File name with path", required=True)
    parser.add_argument('--modelname', type=str, default='BIMODAL',
                        required=False, help="Model name e.g., 'ForwardRNN','BIMODAL', 'FBRNN', 'NADE'")
    parser.add_argument('--starting', type=str, default='fixed',
                        required=False, help="'fixed', 'random'")
    parser.add_argument('--minlen', type=int, default=14,
                        help="Minimum length of all the strings", required=True)
    parser.add_argument('--maxlen', type=int, default=74,
                        help="Maximum length of all the strings", required=True)
    parser.add_argument('--aug', type=int, default=1,
                        help="Maximum length of all the strings", required=False)
    
    args = parser.parse_args()
    
    print(args)

    filename = args.filename
    model_name = args.modelname
    starting_point = args.starting
    minLen = args.minlen
    maxLen = args.maxlen
    augmentation = args.aug
    
    preprocess_data(filename_in=filename, model_type=model_name, starting_point=starting_point, min_len=minLen, max_len=maxLen,augmentation=augmentation)
