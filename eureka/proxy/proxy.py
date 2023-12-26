import requests
import json

url = "https://api.openai-hk.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "*********** your key of https://api.openai-hk.com/v1/chat/completions"
}

data = {
    "max_tokens": 1200,
    "model": "gpt-3.5-turbo",
    "temperature": 0.8,
    "top_p": 1,
    "presence_penalty": 1,
    "messages": [
        {
            "role": "system",
            "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."
        },
        {
            "role": "user",
            "content": "你是chatGPT多少？"
        }
    ]
}

def get_openai_response(content):
    response = requests.post(url, headers=headers, data=json.dumps(content).encode('utf-8') )
    result = response.content.decode("utf-8")
    return result



if __name__ == "__main__":
    result = get_openai_response(data)
    print(result)
