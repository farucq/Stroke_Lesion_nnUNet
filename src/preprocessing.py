import os
import subprocess

def run_preprocessing(dataset_id, config="3d_fullres"):
    cmd = f"nnUNetv2_plan_and_preprocess -d {dataset_id} -c {config}"
    subprocess.run(cmd, shell=True, check=True)
