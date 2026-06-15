from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_ai_tutor(user_message, memory):

    prompt = f"""
    You are a Korean Hangul tutor.

    Student weak letters:
    {memory['weak_letters']}

    Student bad habits:
    {memory['bad_habits']}

    Student message:
    {user_message}

    Give personalized tutoring advice.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": "You are a helpful Korean tutor."
            },

            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content