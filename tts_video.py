import requests
import base64
from dotenv import load_dotenv
import os
import json

load_dotenv()

username = os.getenv("VIDEO_API_USERNAME")
password = os.getenv("VIDEO_API_PASSWORD")

class VideoGenerator:
    def __init__(self, api_key):

        auth_string = f"{username}:{password}"
        self.auth_header = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        print("Authorization header:", f"Basic {self.auth_header}")

    def generate_video(self, input_text, source_url):
        url = "https://api.d-id.com/talks"

        payload = {
            "script": {
                "type": "text",
                "subtitles": "false",
                "provider": {
                    "type": "microsoft",
                    "voice_id": "en-US-JennyNeural"
                },
                "ssml": "false",
                "input": input_text
            },
            "config": {
                "fluent": "false",
                "pad_audio": "0.0"
            },
            "source_url": source_url
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Basic ZGhhcm1hbnNodXM4MzAzQGdtYWlsLmNvbQ:GyXBps2rWHCQSKgAJPCkx"  
        }

        response = requests.post(url, json=payload, headers=headers)
        _response = json.loads(response.text)
        print("Response: ",_response)
        while _response["status"] != "created":
            response = requests.post(url, json=payload, headers=headers)
            _response = json.loads(response.text)

        talk_id = json.loads(response.text)['id']

        talk_url = f"{url}/{talk_id}"

        headers = {
            "accept": "application/json",
            "authorization": "Basic ZGhhcm1hbnNodXM4MzAzQGdtYWlsLmNvbQ:GyXBps2rWHCQSKgAJPCkx"
        }

        response = requests.get(talk_url, headers=headers)
        video_response = json.loads(response.text)

        while video_response["status"] != "done":
            response = requests.get(talk_url, headers=headers)
            video_response = json.loads(response.text)

        video_url = video_response["result_url"]
        return video_url
