import subprocess

def train_model(dataset_id, config="3d_fullres", fold=0):
    cmd = f"nnUNetv2_train {dataset_id} {config} {fold}"
    subprocess.run(cmd, shell=True, check=True)
