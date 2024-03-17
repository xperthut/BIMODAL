#!/bin/bash

# Adapt according to your installation.
CONDA_BASE_DIR=~/software/Miniconda3

# Activate the conda environment.
source "$CONDA_BASE_DIR/etc/profile.d/conda.sh"

source activate Torch

python preprocessing/preprocess_main.py --filename $1 --modelname $2 --starting $3 --minlen $4 --maxlen $5 --aug $6
