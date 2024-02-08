from beam import App, Runtime, Image, Output, Volume, VolumeType

import os
import torch
from transformers import (
    GenerationConfig,
    LlamaForCausalLM,
    LlamaTokenizer,
)

base_model = "meta-llama/Llama-2-13b-chat-hf"

app = App(
    name="llama2",
    runtime=Runtime(
        cpu=1,
        memory="32Gi",
        gpu="A10G",
        image=Image(
            python_packages=[
                "accelerate",
                "transformers",
                "torch",
                "sentencepiece",
                "protobuf",
                "bitsandbytes",
                "peft"
            ],
        ),
    ),
    volumes=[
        Volume(
            name="model_weights",
            path="./model_weights",
            volume_type=VolumeType.Persistent,
        )
    ],
)


@app.rest_api()
def generate(**inputs):
    prompt = inputs["prompt"]

    tokenizer = LlamaTokenizer.from_pretrained(
        base_model,
        cache_dir="./model_weights",
        use_auth_token=os.environ["HUGGINGFACE_API_KEY"],
    )
    model = LlamaForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.float16,
        device_map="auto",
        cache_dir="./model_weights",
        load_in_4bit=True,
        use_auth_token=os.environ["HUGGINGFACE_API_KEY"],
    )

    tokenizer.bos_token_id = 1
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to("cuda")

    generation_config = GenerationConfig(
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        max_length=512,
    )

    with torch.no_grad():
        generation_output = model.generate(
            input_ids=input_ids,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=128,
            early_stopping=True,
        )

    s = generation_output.sequences[0]
    decoded_output = tokenizer.decode(s, skip_special_tokens=True).strip()

    print(decoded_output)

    return {"answer": decoded_output}

    # # Write text output to a text file, which we'll retrieve when the async task completes
    # output_path = "output.txt"
    # with open(output_path, "w") as f:
    #     f.write(decoded_output)