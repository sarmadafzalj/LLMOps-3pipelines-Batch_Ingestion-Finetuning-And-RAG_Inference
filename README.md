# LLMOps: Feature | Inference | Finetune - 3Pipeline Architecture for LLM Based RAG Application on Tech News Architecture

**Transform your private LLM into an expert by utilizing a carefully curated dataset leveraging state-of-the-art GPT-4 and then fine-tuning with LLama2 7B.**
<table>
    <tr>
        <td width = 30%>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <p><h3>Application Overview</h3></p>
            <p>Every morning 9AM CST, fetch latest articles from Aylien tech news API. Chunk, embed and load into Vectara database and using OpenAI GPT-4 created a curated Q/A set for finetuning. Serve the on with Inference pipeline which query the vectors from Vectara database and synthesize with your privately hosted LLama2 7B. With a good amount of QA set generated with diverse articles run Fine-tuning pipeline every month and employ CI/CD to deploy updated model weights into production. Down the line in 6 months, the small LLama2 is your new expert with specialization in understanding Tech and its jargon.</p>
        </td>
    </tr>
</table>

## Objective
Automated pipelines for feature store, inference and finetuning for making your compact and private LLM (LLama2 7B) an expert on Technology. It leverages GPT-4 to curate Q/A dataset whcih is then used to finetune the LLama2 and then down the line Q/A extraction is stopped once we have optimal responses from Llama2.

## Architecture Diagram
<p align=center>
<img src="Images\3pipelines.png" alt="Your Image">
</p>

## Tech-Stack

<table>
    <tr>
        <td>
            <img src="Images\llamaindex.jpg" alt="Your Image">
        </td>
        <td>
            <img src="Images\vectara_wordmark.png" alt="Your Image">
        </td>
        <td>
            <img src="Images\meta-hero.jpg" alt="Your Image">
        </td>
        <td>
            <img src="Images\Untitled_design_(1).jpg" alt="Your Image">
        </td>
        <td>
            <img src="Images\streamlit.png" alt="Your Image">
        </td>
        <td>
            <img src="Images\quantexa.png" alt="Your Image">
        </td>
        <td>
            <img src="Images\openai.png" alt="Your Image">
        </td>
    </tr>
    <tr valign=top>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <p><b>Vectara</b></p>
            <p>Vector database for storing and querying embeddings</p>
        </td>
        <td>
            <p><b>Beam</b></p>
            <p>Infrastructure with GPUs and storage volume</p>
        </td>
        <td>
            <p><b>Llama2</b></p>
            <p>LLM for RAG and finetuning</p>
        </td>
        <td>
            <p><b>Streamlit</b></p>
            <p>Chatbot user interface</p>
        </td>
        <td>
            <p><b>Quantexa</b></p>
            <p>Data source for tech news articles</p>
        </td>
        <td>
            <p><b>OpenAI</b></p>
            <p>GPT-4 for creating Q/A dataset for finetuning</p>
        </td>
    </tr>
</table>

## How to Setup

There are total 3 apps in this project which will be deployed on Beam.
- **Feature app**: It will run as scheduler everyday 9AM. It contains ETL to grab news articles from Aylien API the using Vectara it chunks, embeds, and loads in the vectorstore. Second part of this is to use a GPT-4 to generate 5 questions and answer pair from each article and save it onto Beam storage volume as a csv file.
- **Inference app**: It is deployed as a restful API which takes user query as input then using vectara embeds it and searches relavant chunks with cosine similarity. Llama2 7B is hosted for inference which is then called to synthesize the final response.
    - Second part to this app is a streamlit chatbot UI which is not hosted on Beam but ran locally. This basically calls the inference rest api.  
- **Training app**: This is again deployed as a scheduler to be ran monthly. It uses PEFT LoRA and huggingface transformer library for finetuning, parameters and prompter is same as used for Alpaca.

To setup you need to get following Tokens and API keys and create a .env file as below and save for all the pipelines
```python
AYLIEN_USERNAME=
AYLIEN_PASSWORD=
AYLIEN_APPID=

OPENAI_API=
VECTARA_CUSTOMER_ID=
VECTARA_CORPUS_ID=
VECTARA_API_KEY=

Beam_key=

HF_key
```

Deploy each app one by one on Beam on WSL. You need beam account first and here are detail intsallation guaidance:  https://docs.beam.cloud/getting-started/installation
- Feature pipeline: beam deploy app.py:FeaturePipeline
- Inference pipeline: here we have to deploy LLM as rest api - cd inside the llama2 folder and run beam deploy app.py:generate
- Training pipeline: beam deploy app.py:train_model

Then inside the inference pipeline you can start the chatbot UI by: streamlit run app.py

## Reach out to me
- <i>Author: <b>Sarmad Afzal</b></i>
- <i>Linkedin: https://www.linkedin.com/in/sarmadafzal/</i>
- <i>Github: https://github.com/sarmadafzalj</i>
- <i>Youtube: https://www.youtube.com/@sarmadafzalj</i>
---
