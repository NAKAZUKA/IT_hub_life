import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')
text = os.getenv('TEXT')
# ques = 'Радиус земли'


def get_gpt_response(question):

    prompt = {
        "modelUri": "gpt://b1gtqld3kg7to2drbhru/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Тебя зовут Бендер из мультика футурама, ты должен помогать студентам и отвечать на их вопросы"
            },
            {
                "role": "assistant",
                "text": text
            },
            {
                "role": "user",
                "text": question
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key " + token
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.text

    return json.loads(result)["result"]["alternatives"][0]["message"]["text"]


# if __name__ == "__main__":
#     print(get_gpt_response(ques))
