import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


class ResponseEvaluator:

    def evaluate(
        self,
        user_message,
        assistant_response
    ):

        eval_prompt = f"""
        You are evaluating an AI sales assistant.

        User Message:
        {user_message}

        Assistant Response:
        {assistant_response}

        Score the response from 0 to 1 on:

        - groundedness
        - relevance
        - confidence

        Also determine:
        - flagged (true/false)
        - reasoning

        Return STRICT JSON only.

        Example:

        {{
            "groundedness": 0.91,
            "relevance": 0.88,
            "confidence": 0.85,
            "flagged": false,
            "reasoning": "Response grounded in catalog data."
        }}
        """

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324",

            messages=[
                {
                    "role": "user",
                    "content": eval_prompt
                }
            ]
        )

        content = response.choices[0].message.content

        print("\nRAW EVAL RESPONSE:\n")
        print(content)

        try:

            cleaned_content = content.strip()

            if cleaned_content.startswith("```json"):
                cleaned_content = cleaned_content.replace(
                    "```json",
                    ""
                )

            if cleaned_content.endswith("```"):
                cleaned_content = cleaned_content.replace(
                    "```",
                    ""
                )

            cleaned_content = cleaned_content.strip()

            return json.loads(cleaned_content)

        except Exception as e:

            print("EVAL PARSING ERROR:", e)

            return {
                "groundedness": 0.5,
                "relevance": 0.5,
                "confidence": 0.5,
                "flagged": True,
                "reasoning": "Failed to parse evaluation response."
            }