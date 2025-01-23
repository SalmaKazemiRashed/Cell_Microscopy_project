#!/usr/bin/env bash
#SBATCH --gpus 4
#SBATCH -A project_name
#SBATCH -t 3:00:00
#SBATCH -n 5
./epoch_run.sh
