import json
import random
import string
import http.client


class BAIChat:
    def generate(prompt: str, max_tokens: int = None) -> str:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Host": "chatbot.theb.ai",
            "Origin": "https://chatbot.theb.ai",
            "Referer": "https://chatbot.theb.ai",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
            "Content-Type": "application/json",
        }
        conn = http.client.HTTPSConnection('chatbot.theb.ai')
        prompt = prompt.replace('"', "\n")

        chat_id = f"chatcmpl-"+str("".join(random.choice(string.ascii_letters) for i in range(15)))

        payload = json.dumps(
            {"prompt": prompt, "options": {"parentMessageId": chat_id}}
        )
        conn.request('POST', '/api/chat-process', payload,  headers=headers)

        return [json.loads(line) for line in conn.getresponse().read().decode('utf-8').splitlines()][-1]["text"]

