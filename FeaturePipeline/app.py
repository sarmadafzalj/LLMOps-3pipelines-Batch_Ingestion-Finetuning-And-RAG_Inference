from beam import App, Volume, Runtime, Image
from load import load
import logging, datetime
from transform import transform
from extract import extract
import pandas as pd
import numpy as np
import os, time
volume_path = "./finetuning_data"

app = App(
    name="FeaturePipeline",
     runtime=Runtime(
        cpu=2,
        memory="4Gi",
        image=Image(
            python_version="python3.10",
            python_packages="requirements.txt",
        ),
    ),
    volumes=[
        Volume(
            name="finetuning_data",
            path=volume_path,
        )
    ],
)


@app.schedule(when="*/10 * * * *")
def FeaturePipeline():
    try:
        print(f"Start - Extraction of Data")
        articles = extract()
        print(f"End - Extraction of Data")
        print(f"Start - Transformation of Data")
        questions_df, documents = transform(articles)
        print(f"End - Transformation of Data")
        print(f"Start - Loading of Data")
        df = load(documents, questions_df)
        current_datetime = datetime.datetime.now()
        csv_data = df.to_csv(index=False)
        formatted_datetime = current_datetime.strftime("%Y-%b-%d %H:%M:%S")
        with open(f"{volume_path}/finetune_data_{formatted_datetime}.csv", "w") as f:
            f.write(csv_data)
        print("loaded successfully")
    except Exception as e:
        logging.error("Error: %s", e)
        print("Error: ", e)
    

