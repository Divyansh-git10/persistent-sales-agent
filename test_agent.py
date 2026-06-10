from app.agents.agent import SalesAgent

agent = SalesAgent()

response = agent.chat(
    user_id="divyansh",
    message="Which plan includes SSO?"
)

print(response)