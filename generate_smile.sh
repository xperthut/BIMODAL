#!/bin/bash

# Adapt according to your installation.
CONDA_BASE_DIR=~/software/Miniconda3

# Activate the conda environment.
source "$CONDA_BASE_DIR/etc/profile.d/conda.sh"

source activate Torch

python model/generate.py --modelname $1 --runtype $2 --TotalMol $3
