import requests, os, time, datetime
from dotenv import load_dotenv
import pandas as pd
import numpy as np
load_dotenv()

from llama_index.indices import VectaraIndex
from llama_index import Document

#setting up secrets for Vectara
VECTARA_CUSTOMER_ID=os.environ["VECTARA_CUSTOMER_ID"] 
VECTARA_CORPUS_ID=os.environ["VECTARA_CORPUS_ID"] 
VECTARA_API_KEY=os.environ["VECTARA_API_KEY"] 
os.environ['OPENAI_API_KEY'] = os.environ["OPENAI_API"]

index = VectaraIndex(vectara_api_key=VECTARA_API_KEY, vectara_customer_id=VECTARA_CUSTOMER_ID, vectara_corpus_id=VECTARA_CORPUS_ID)
query_engine = index.as_query_engine()

def get_gpt_ans(question):
    response = query_engine.query(question)

    print("Got response")
    return response

def load(documents, df):
    #we will load the documents into the Vectara Index
    index.add_documents(documents)
    df['Answers'] = df['Questions'].apply(lambda question: get_gpt_ans(question))
    return df


# print(load())
