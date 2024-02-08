from math import ceil

from beam import App, Runtime, Image, Volume
from helpers import get_newest_checkpoint, base_model
from training import train, load_models
from datasets import load_dataset, DatasetDict, Dataset
#from inference import call_model
import pandas as pd
import numpy as np
import os
beam_ft_data_volume = "./finetuning_data"

# The environment your code runs on 
app = App(
    "llama-lora",
    runtime=Runtime(
        cpu=4,
        memory="32Gi",
        gpu="A100-80",
        image=Image(
            python_version="python3.10",
            python_packages="requirements.txt",
        ),
    ),
    # Mount Volumes for fine-tuned models and cached model weights
    volumes=[
        Volume(name="checkpoints", path="./checkpoints"),
        Volume(name="pretrained-models", path="./pretrained-models"),
        Volume(name="finetuning_data", path=beam_ft_data_volume)
    ],
)


# Fine-tuning
@app.run()
def train_model():
    # Trained models will be saved to this path
    beam_volume_path = "./checkpoints"
    
    csv_files = [file for file in os.listdir(beam_ft_data_volume) if file.endswith(".csv")]
    combined_df = pd.DataFrame()
    dfs = []

    for csv_file in csv_files:
        file_path = os.path.join(beam_ft_data_volume, csv_file)
        df = pd.read_csv(file_path)
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.reset_index(drop=True, inplace=True)

    combined_df = combined_df.drop('Finetuned', axis =1)
    combined_df.rename(columns={"Questions": "instruction", "Answers": "output"}, inplace=True)
    combined_df['input'] = np.nan

    # Load dataset -- for this example, we'll use the vicgalle/alpaca-gpt4 dataset hosted on Huggingface:
    # https://huggingface.co/datasets/vicgalle/alpaca-gpt4
    dataset = DatasetDict({
        "train": Dataset.from_pandas(combined_df),
    })
    
    # Adjust the training loop based on the size of the dataset
    samples = len(dataset["train"])
    val_set_size = ceil(0.1 * samples)

    train(
        base_model=base_model,
        val_set_size=val_set_size,
        data=dataset,
        output_dir=beam_volume_path,
    )


# # Inference
# @app.rest_api()
# def run_inference(**inputs):
#     # Inputs passed to the API
#     input = inputs["input"]

#     # Grab the latest checkpoint
#     checkpoint = get_newest_checkpoint()
    
#     # Initialize models with latest fine-tuned checkpoint
#     models = load_models(checkpoint=checkpoint)

#     model = models["model"]
#     tokenizer = models["tokenizer"]
#     prompter = models["prompter"]

#     # Generate text response
#     response = call_model(
#         input=input, model=model, tokenizer=tokenizer, prompter=prompter
#     )
#     return response