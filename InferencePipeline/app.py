from llama_index.indices import VectaraIndex
import os, time
from dotenv import load_dotenv
from model import call_model

load_dotenv()

VECTARA_CUSTOMER_ID=os.environ["VECTARA_CUSTOMER_ID"] 
VECTARA_CORPUS_ID=os.environ["VECTARA_CORPUS_ID"] 
VECTARA_API_KEY=os.environ["VECTARA_API_KEY"] 
os.environ['OPENAI_API_KEY'] = os.environ["OPENAI_API"]

index = VectaraIndex(vectara_api_key=VECTARA_API_KEY, vectara_customer_id=VECTARA_CUSTOMER_ID, vectara_corpus_id=VECTARA_CORPUS_ID)

def final_response(prompt):
    #first we get similar docs from the index
    print("doing doc search")
    docs = index.as_retriever(summary_enabled=True, similarity_top_k=3)
    sim_docs = docs.retrieve(prompt)
    sim_docs_text = [doc.text for doc in sim_docs]  
    print("got similar docs")
    #now we pass our prompt + similar docs to the llm
    prompt_2 = f"""
    You are given the the context below. Please use that context only to answer the asked question.

    context: {sim_docs_text}
    question: {prompt}

    answer:

    """

    #now invoking the llm
    print("calling model")
    output, out2 = call_model(prompt_2)
    print("got model response")
    print(output)
    print(out2)
    return output


#using chainlit UI
import streamlit as st
st.title('Ask me anything')

prompt = st.text_area("Enter your question here", "What is software sentiment")
if st.button('Submit'):
    with st.spinner('Wait for it...'):
        st.success(final_response(prompt))


    


