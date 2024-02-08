import requests, os, time, datetime
from dotenv import load_dotenv
load_dotenv()

#credentials for the Aylien News API
username = os.environ["AYLIEN_USERNAME"]
password = os.environ["AYLIEN_PASSWORD"]
AppID = os.environ["AYLIEN_APPID"]

def extract():
	#Requesting a bearer token from oauth endpoint
	#Review the docs for detailed authentication workflows docs.aylien.com/newsapi/v6
	token = requests.post("https://api.aylien.com/v1/oauth/token", auth=(username, password), data={"grant_type": "password"}).json()["access_token"]
	print(token)
	#Passing the token as a header with App Id
	headers = {"Authorization": "Bearer {}".format(token), "AppId":"d1ae1185"}
	
	#V6 URL
	url = 'https://api.aylien.com/v6/news/stories?aql=industries:({{id:in.tech}}) AND language:(en) AND text: (tech, google, openai, microsoft, meta, apple, amazon) AND categories:({{taxonomy:aylien AND id:ay.appsci}}) AND sentiment.title.polarity:(negative neutral positive)&cursor=*&published_at.end=NOW&published_at.start=NOW-1DAYS/DAY'
	
	response = requests.get(url, headers=headers)
	data = response.json()
	print(data)
	stories = data['stories']
	combined_text_list = []
	for story in stories:
		body = story['body']
		combined_text_list.append(body)
            
	return combined_text_list

