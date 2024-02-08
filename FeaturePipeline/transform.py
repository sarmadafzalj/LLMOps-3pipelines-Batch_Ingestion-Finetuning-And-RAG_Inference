import requests, os, time, datetime
from dotenv import load_dotenv
load_dotenv()

import pandas as pd
import numpy as np
import ast

from llama_index import Document

import openai
from openai import OpenAI
openai.api_key = os.environ["OPENAI_API"]

def transform(articles):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%b-%d")

    documents = [Document(text=t, metadata={"Article_Date": formatted_datetime}) for t in articles]

    #Transform Step2: extracting questions from articles
    system_prompt = """
    You are an AI Based Question Generator. Given the following Article, please generate 5 questions.
    Questions should be specific to the article and should be answerable from the article.
                                                                            
    Give response in the form of list. See the example below for formatting response:
                                        
    example: ["What is the name of the company?", "What is the name of the CEO?"]

    Make sure that it is "" and NOT ''.
    Do not write anything other than the questions wapped in [] and seperated by ,.                                     
    """

    questions_df = pd.DataFrame(columns = ['Questions', 'Answers', 'Finetuned'])
    for article in articles:
        client = OpenAI(api_key=os.environ["OPENAI_API"])

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": article}
            ]
        )


        qns = completion.choices[0].message.content
        qns = ast.literal_eval(qns)
        for q in qns:
            questions_df.loc[len(questions_df)] = [q, 0, 0]

    return questions_df, documents
