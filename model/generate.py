import torch
import numpy as np
import pandas as pd
from trainer import Trainer
from sample import Sampler
import argparse, os
import warnings
warnings.filterwarnings('ignore')

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--modelname', type=str,
                        help="Model name without path", required=True)
    parser.add_argument('--runtype', type=str,
                        help="complete, single, cross", required=True)
    parser.add_argument('--TotalMol', type=int, default=1,
                        help="Required new molecule", required=True)
    
    args = parser.parse_args()
    
    print(args)

    model_name = args.modelname
    run_type = args.runtype
    N = args.TotalMol
    
    model = Trainer(model_name)
    
    if run_type == "complete":
        model.complete_run()
    elif run_type == "single":
        model.single_run()
    elif run_type == "cross":
        model.cross_validation()
        
    s = Sampler(model_name)
    s.sample(N=N)
        
    respath = os.path.join('evaluation', model_name, 'molecules')
    gen_fl = set()

    if os.path.exists(respath):
        fl = os.listdir(respath)

        for f in [f for f in fl if "molecules_fold_" in f]:
            new_mol = [x[0] for x in pd.read_csv(os.path.join(respath, f), header=None).values.tolist()]
            print(new_mol)
            for x in new_mol:
                gen_fl.add(x)
                
    print(gen_fl)

    