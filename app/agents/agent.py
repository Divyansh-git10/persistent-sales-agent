import uuid
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.tools.memory_tool import get_user_memory
from app.tools.catalog_tool import CatalogTool
from app.memory.sqlite_memory import SQLiteMemory
from app.agents.prompts import SYSTEM_PROMPT
from app.agents.evaluator import ResponseEvaluator

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

catalog_tool = CatalogTool()

memory = SQLiteMemory()

evaluator = ResponseEvaluator()


class SalesAgent:

    def chat(self, user_id, message):

        session_id = str(uuid.uuid4())

        user_memory = get_user_memory(user_id)

        catalog_results = catalog_tool.search_catalog(message)

        catalog_context = "\n".join(catalog_results)

        prompt = f"""
        Previous User Memory:
        {user_memory}

        Relevant Catalog Information:
        {catalog_context}

        User Question:
        {message}
        """

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324",

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        assistant_response = response.choices[0].message.content

        eval_result = evaluator.evaluate(
            message,
            assistant_response
        )

        memory.save_message(
            user_id=user_id,
            role="user",
            content=message,
            session_id=session_id
        )

        memory.save_message(
            user_id=user_id,
            role="assistant",
            content=assistant_response,
            session_id=session_id
        )

        return {
            "response": assistant_response,

            "eval": eval_result,

            "tools_called": [
                "search_catalog",
                "get_user_memory"
            ],

            "session_id": session_id
        }