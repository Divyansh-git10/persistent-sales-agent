from app.agents.agent import SalesAgent

agent = SalesAgent()

response = agent.chat(
    user_id="divyansh",
    message="Does that also include audit logs?"
)

print(response)