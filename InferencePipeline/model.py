
import requests
import json, os
from dotenv import load_dotenv
import re

load_dotenv()

Beam_key = os.environ["Beam_key"]

url = "https://dys3w.apps.beam.cloud"
def call_model(prompt):
  payload = {"prompt": prompt}
  headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": f"Basic {Beam_key}",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
  }

  response = requests.request("POST", url, 
    headers=headers,
    data=json.dumps(payload)
  )
  pattern = r'answer:(.+)'

  res = response.json()
  print(res)
  res = res['answer']
  match = re.search(pattern, res, re.DOTALL)  # re.DOTALL is used to match newline characters as well
  if match:
    answer_content = match.group(1).strip()
    return answer_content, res
  else:
    return "No results found.", res

