import requests
import json


def text_to_text(question):

    prompt = {
        "modelUri": "gpt://b1gtqld3kg7to2drbhru/yandexgpt-lite",#b1gm3v3q26f844h37rod
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },

        # "messages": [
        #     {
        #         "role": "system",
        #         "text": "Your name is Peter, you are a voice assistant located in the terminal of Pulkovo airport in St. Petersburg"
        #     },
        #     {
        #         "role": "assistant",
        #         "text": "Explain to the person at his request how to get to a bus stop, metro or any point in St. Petersburg. Answer completely in English. Answer briefly so that it won't be boring to listen to you"
        #     },
        #     {
        #         "role": "user",
        #         "text": question
        #     }
        # ]

        "messages": [
            {
                "role": "system",
                "text": "Ты Бэндэр из Футурамы. Используй стиль разговора как он. Не используй диалоги в тексте. Говори кратко. Не надо часто упоминать кто ты. Не используй конструкции эмоционального описания, указания на персонажей в тексте. Говори только свою реплику диалога. Всегда используй текст роли assistant для формирования ответа"
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
        "Authorization": "Api-Key AQVN0m68cAC6dKMy4nlpUYbzyYMlZYitACpHykHG" # AQVNz0ez4D8Eh8QnUUzgnGdPGn5b7fJzZBGRztFC
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    # print(result)
    return result["result"]["alternatives"][0]["message"]["text"]


# print(text_to_text("приветик"))