#!/bin/bash

# Adapt according to your installation.
CONDA_BASE_DIR=~/software/Miniconda3

# Activate the conda environment.
source "$CONDA_BASE_DIR/etc/profile.d/conda.sh"

source activate Torch

python preprocessing/preprocess_main.py --filename $1 --minlen $2 --maxlen $3
