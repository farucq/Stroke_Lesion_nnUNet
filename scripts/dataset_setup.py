import os

os.environ["nnUNet_raw"] = "./data/raw"
os.environ["nnUNet_preprocessed"] = "./data/processed"
os.environ["nnUNet_results"] = "./outputs"

print("Environment variables set successfully")
