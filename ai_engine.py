import openai

openai.api_key = "your API Key"

PROMPT = "Kamu adalah virtual pet lucu, jawab singkat dan santai."

class AIEngine:
    def ask(self, text):
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": text}
            ]
        )
        return res.choices[0].message.content
